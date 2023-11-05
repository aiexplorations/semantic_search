from qdrant_client import QdrantClient, models
from sentence_transformers import SentenceTransformer
import logging
import json

user_query = input("Enter search query ")

num_results = input("Enter number of results ")

encoder = SentenceTransformer("all-MiniLM-L6-v2")

QC = QdrantClient("http://localhost:6333")

hits = QC.search(
    collection_name="Blurb",
    query_vector=encoder.encode(user_query).tolist(),
    limit=num_results,
)


for i, hit in enumerate(hits):
    print(f"Result #{i+1}",
          "score:", hit.score,
          json.dumps(hit.payload["Title"]),
          json.dumps(hit.payload["Author"]),
          json.dumps(hit.payload["Blurb"]),
          "\n"
         )
