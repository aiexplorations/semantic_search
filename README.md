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

## Things to Work on
1. Containerization with Dockerfiles and Docker compose
2. Easier Deployability and handling of variables
3. Exception Handling
4. Test cases and automation

