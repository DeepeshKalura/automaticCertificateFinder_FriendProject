import os
import io

from dotenv import load_dotenv, find_dotenv
from google_mine import create_service

load_dotenv(find_dotenv())
SCOPE = ["https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/drive.readonly"]
API_NAME = 'drive'
API_VERSION = 'v3'

drive_service = create_service('credentials.json', API_NAME, API_VERSION, SCOPE)

# simple create the folder in drive

folderIWillCreate =  ["TeraName", "MeraName", "SabkaName"]

for folder in folderIWillCreate:
    file_metadata = {
        "name": folder,
        "mimeType": "application/vnd.google-apps.folder",
        "parents": "My Drive"
    }

    drive_service.files().create(body=file_metadata).execute()

print("Done, Now Check the google drive")




