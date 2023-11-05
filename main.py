from fastapi import FastAPI
from qdrant_client import QdrantClient, models
from sentence_transformers import SentenceTransformer
import json


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

encoder = SentenceTransformer("all-MiniLM-L6-v2")

QC = QdrantClient("http://localhost:6333")

@app.get("/search/{user_query}")
async def search(user_query, 
        qdrant_client=QC, 
        num_results=3, 
        encoder=encoder):

    '''
    Perform a query on the database
    '''

    hits = qdrant_client.search(
    collection_name="Blurb",
    query_vector=encoder.encode(
        "").tolist(),
    limit=3,
    )

    print(type(hits))

    for i, hit in enumerate(hits):
        print(f"Result #{i+1}",
              "score:", hit.score, 
              json.dumps(hit.payload["Title"]),
              json.dumps(hit.payload["Author"]),
              json.dumps(hit.payload["Blurb"]),
              "\n"
             )

    return [hit.payload for hit in hits]
