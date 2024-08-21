import uvicorn
from fastapi import FastAPI
from qdrant_client import QdrantClient, models
from sentence_transformers import SentenceTransformer
import json
import streamlit as st


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/search/{user_query}")
async def search(user_query, 
        num_results=3):

    '''
    Perform a query on the database
    '''

    encoder = SentenceTransformer("all-MiniLM-L6-v2")

    QC = QdrantClient("http://localhost:6333")


    hits = QC.search(
    collection_name="Blurb",
    query_vector=encoder.encode(f"{user_query}").tolist(),
    limit=3,
    )
    
    payloads = [hit.payload for hit in hits]
    scores = [hit.score for hit in hits]
    
    results = {}
    count = 0
    for payload, score in zip(payloads, scores):
        
        payload.update({"Score":score})
        results.update({count:payload})
        count = count+1

    return results

if __name__ == "__main__":
    uvicorn.run('backend:app', host="127.0.0.1", port=8888, reload=True)
