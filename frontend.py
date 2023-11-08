import streamlit as st
import requests
import json
import utils
import pandas as pd



st.title("Book Search App")
st.write("Search over 50,000 books for topics of your interest!")

search_term = st.text_input(label="Enter search terms here")

if st.button("Search"):
    result = requests.get(url=f"http://127.0.0.1:8888/search/{search_term}")
    formatted_results = utils.format_results(result)
    st.dataframe(
        pd.DataFrame.from_dict(
            formatted_results, 
            orient="index"
            ).sort_values(by="Score", ascending=False)[['Title', 'Author', 'Blurb', 'Score']])
    #st.dataframe(pd.read_json(formatted_results))
    st.text("Tip: Double click on the shortened blurb to read it in full.")
    