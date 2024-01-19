import os
import io

from dotenv import load_dotenv, find_dotenv
from google_mine import create_service
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload

load_dotenv(find_dotenv())
SCOPE = ["https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/drive.readonly"]
API_NAME = 'drive'
API_VERSION = 'v3'

drive_service = create_service('credentials.json', API_NAME, API_VERSION, SCOPE)

# simple upload file in the folder

folder_id = "1B5iwnts7AYoYeQc9-5oQaZp2qLfMW22b"
file_metadata = {
    'name': '1-100-1.pdf',
    'mineType': 'application/pdf',
    'parents': [folder_id] 
}

try:

    media = MediaFileUpload('1-100-1.pdf', mimetype='application/pdf')
except Exception as e:
    
    print(f"media is not right:  {e}")

try:
    file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print(file)
except Exception as e:
    print(f"file is not right: {e}")