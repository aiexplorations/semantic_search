from qdrant_client import QdrantClient, models
from sentence_transformers import SentenceTransformer
import requests
import json
import utils
import pandas as pd
import prettytable
from tabulate import tabulate

print("*** Book Search App ***")
print("Search the contents of over 50,000 books using fast vector search")

user_query = input("Enter search query (3 results maximum) ")

result = requests.get(url=f"http://127.0.0.1:8888/search/{user_query}")
formatted_results = utils.format_results(result)


result_df = pd.DataFrame.from_dict(
            formatted_results, 
            orient="index"
            ).sort_values(by="Score", 
            ascending=False)[['Title', 'Author', 'Blurb', 'Score']]



print(tabulate(result_df, headers="keys", tablefmt="psql"))