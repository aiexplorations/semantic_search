from fastapi import APIRouter, HTTPException
import os
import requests
import zipfile
from bs4 import BeautifulSoup
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.http.models import PointStruct

router = APIRouter()

# Constants
GUTENBERG_ROBOT_URL = "https://www.gutenberg.org/robot/harvest?filetypes[]=txt&filetypes[]=zip"
DOWNLOAD_DIR = "downloads"
QDRANT_HOST = "localhost"
QDRANT_PORT = 6333
INDEX_NAME = "books_index"

# Initialize Qdrant client
qdrant_client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)

# Initialize embedding model
model = SentenceTransformer('BAAI/bge-large-en-v1.5')  

def fetch_gutenberg_manifest():
    response = requests.get(GUTENBERG_ROBOT_URL)
    response.raise_for_status()
    return response.text

def parse_gutenberg_manifest(manifest_html):
    soup = BeautifulSoup(manifest_html, 'html.parser')
    links = [a['href'] for a in soup.find_all('a', href=True) if a['href'].endswith('.zip')]
    return links

def download_and_unzip(url, download_dir):
    local_filename = os.path.join(download_dir, url.split('/')[-1])
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    with zipfile.ZipFile(local_filename, 'r') as zip_ref:
        zip_ref.extractall(download_dir)
    os.remove(local_filename)

def load_text_files(download_dir):
    text_files = [os.path.join(download_dir, f) for f in os.listdir(download_dir) if f.endswith('.txt')]
    documents = []
    for file_path in text_files:
        with open(file_path, 'r', encoding='utf-8') as file:
            documents.append(file.read())
    return documents

def compute_embeddings(documents):
    return model.encode(documents)

def upload_to_qdrant(embeddings, documents):
    points = [
        PointStruct(id=i, vector=embedding, payload={"content": document})
        for i, (embedding, document) in enumerate(zip(embeddings, documents))
    ]
    qdrant_client.upsert(collection_name=INDEX_NAME, points=points)

@router.post("/upload_books")
async def upload_books():
    try:
        os.makedirs(DOWNLOAD_DIR, exist_ok=True)
        
        manifest_html = fetch_gutenberg_manifest()
        links = parse_gutenberg_manifest(manifest_html)
        
        for link in links:
            download_and_unzip(link, DOWNLOAD_DIR)
        
        documents = load_text_files(DOWNLOAD_DIR)
        embeddings = compute_embeddings(documents)
        upload_to_qdrant(embeddings, documents)
        
        return {"message": "Documents have been successfully uploaded to Qdrant."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))