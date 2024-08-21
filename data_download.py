import os
import kaggle
import constants
import zipfile
import logging

DATA_FOLDER = "data"
DATASET_NAME = "jdobrow/57000-books-with-metadata-and-blurbs"

FILENAME = "57000-books-with-metadata-and-blurbs.zip"
PARENT_DIR = "/home/rajesh/github"


# Exporting Kaggle credentials for downloading a dataset
kaggle_creds = constants.kaggle
os.system(f"export KAGGLE_USERNAME={kaggle_creds['username']}")
os.system(f"export KAGGLE_KEY={kaggle_creds['key']}")

# Creating a path where to download Kaggle data
path = os.path.join(PARENT_DIR, DATA_FOLDER)

if not os.path.exists(path):
    os.mkdir(path)
    logging.warning("Data directory created")

elif os.path.exists(path):
    logging.warning("Data directory exists")
    

    if not os.path.exists(os.path.join(path,FILENAME)):
        os.chdir(path)
        logging.warning("No data in data directory. Downloading...")
    
    csv_present=False
    for i in os.listdir(path):
        if i.endswith(".csv"):
            csv_present=True

    if csv_present == False:    

        # Downloading and unzipping Kaggle dataset
        os.system(f"kaggle datasets download -d {DATASET_NAME}") 
        with zipfile.ZipFile(os.path.join(path,FILENAME), 'r') as zObject:
            zObject.extractall(path=path)
        if os.path.exists(os.path.join(path,FILENAME)):
            logging.warning("Data downloaded and extracted")


