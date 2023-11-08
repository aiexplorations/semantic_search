import pandas as pd
import numpy as np
import json
from qdrant_client import models, QdrantClient
from sentence_transformers import SentenceTransformer

'''
Note: An instance of Qdrant on local on port 6333 is used in this POC. The Qdrant client configurations may need to be updated in any larger scale implementation of this application.
'''


# Modify the corpus size to persist more or fewere books' records to the vector DB
corpus_size=20000

# data loaded from Kaggle into the data directory is accessed here
df = pd.read_csv("../data/books_with_blurbs.csv", header=0).head(corpus_size)

# persist data as JSON for later use to upload to Qdrant
df.to_json("data.json", orient="records")


# Loading the JSON from disk to prepare a JSON object for the Qdrant Client
# This step may be unnecessary but is useful to demonstrate to those using an on-disk JSON

with open("data.json",) as f:
    data_json = json.load(f)

# We use Mini LM as the embedding model for the vector database
encoder = SentenceTransformer("all-MiniLM-L6-v2")

# change the below configuration to connect to your existing Qdrant instance
QC = QdrantClient("http://localhost:6333")

def create_new_collection_and_upload_vectors(QC, data, shards, collection_name, collection_field, encoder):
    
    '''
    Helper function to load data into Qdrant
    1. Deletes existing collections with a given collection name in Qdrant
    2. Uploads records from the JSON created
    '''

    #delete existing collection
    QC.delete_collection(collection_name=f"{collection_name}")
    
    #create collection with same name
    QC.create_collection(
        collection_name=f"{collection_name}",
        vectors_config=models.VectorParams(
            size=encoder.get_sentence_embedding_dimension(),  # Vector size is defined by used model
            distance=models.Distance.COSINE,),
        shard_number= shards,
        )
    
    #upload records using the encoder model supplied
    QC.upload_records(
        collection_name=f"{collection_name}",
        records=[
            models.Record(
                id=idx, vector=encoder.encode(record[f"{collection_field}"]).tolist(), payload=record
            )
            for idx, record in enumerate(data_json)
        ],
    )


# Defining the collections we want to create in Qdrant

collections = {
    "Title": "Title",
    "ISBN": "ISBN",
    "Author": "Author",
    "Publisher": "Publisher",
    "Blurb": "Blurb"
}

for collection_name, collection_field in collections.items():
    create_new_collection_and_upload_vectors(QC=QC, 
                                             data=data_json,
                                             shards=8,
                                             collection_name=collection_name, 
                                             collection_field=collection_field, 
                                             encoder=encoder)
    


