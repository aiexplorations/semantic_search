# Semantic Search

This is a simple semantic search application which implements a vector similarity based approach for searching a corpus of records, mostly books with blurbs, ISBN and other details.

The user can submit a query to the application via a command line, and the app picks up search terms as arguments and finds the nearest books to the text supplied, using the input provided by the user.


## Application details

The application consists of

### A database 
1. A Qdrant vector store deployed on a local docker container (deployed at application startup)
2. A Python script for downloading a dataset (Only needs to be run when dataset is updated)
3. A Python script for loading vectors computed from the data, into Qdrant, into specific collections (Also run when dataset is updated)
4. Methods for specifying the model used for embedding computation

### A backend
1. A Python script which implements a FastAPI server with one endpoint, that receives requests from a front end, and connects to the Qdrant backend database
2. Compute a vector / embedding based on user queries, and use this to perform similarity searches on Qdrant
2. Some utilities for simple tasks that are performed on the backend

### A front end
1. A streamlit front-end that opens up in a browser, and connects with the aforementioned backend
2. Ability to receive any user input in the form of text, and vectorize it, and search on Qdrant via the backend
2. Display capability on the front-end for tabular search results


### Dataset
The 57000 books dataset on Kaggle with metadata and blurbs:  
https://www.kaggle.com/datasets/jdobrow/57000-books-with-metadata-and-blurbs/ 

### Embedding model
Since this is a really simple app, the idea was to use Mini LM to get the job done.

## Installation and Configuration
0. Clone the repo and set up a Python virtual environment using the requirements file
1. Run a local instance of Qdrant with the default settings to get it running on localhost:6333
2. Run the python script for data download - **takes a few minutes**
3. Run the python script for Qdrant data loading - **may take several minutes**
4. Run the Python backend server

You should now be able to run the frontend server via Streamlit, or run the CLI to search your 50k books.

## Things to Work on
1. Exception handling and unit tests
2. Containerization with Dockerfiles and Docker compose
    1. Front end container
    2. Backend container
    3. Qdrant container
    4. Container for data download and vector computation
3. Easier Deployability via a CI/CD pipelineand handling of app variables

