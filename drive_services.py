import os
import io

from dotenv import load_dotenv, find_dotenv
from google_mine import create_service
from googleapiclient.http import MediaIoBaseDownload

from pdf_to_text import pdf_to_image_text

load_dotenv(find_dotenv())
SCOPE = ["https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/drive.appdata",  "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive.metadata", "https://www.googleapis.com/auth/drive.metadata.readonly",  "https://www.googleapis.com/auth/drive.readonly"]
API_NAME = 'drive'
API_VERSION = 'v3'

drive_service = create_service(os.getenv("CLIENT_SECRET_FILE"), API_NAME, API_VERSION, SCOPE)


def get_pdf_from_link (file_id):
    request = drive_service.files().get_media(fileId = file_id)

    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fd=fh, request=request)

    done = False

    while not done:
        status , done = downloader.next_chunk()

    fh.seek(0)

    with open('checking.pdf', 'wb') as f:
        f.write(fh.read())
        f.close()


  
def folder_to_certificate(folder_id , friend_name ) -> bool:
    """
    This function checks if a given friend's name is in any of the PDF files in a specific Google Drive folder.

    But this function is very expensive in terms of time and resources.

    Therefore, I need hasing to make it faster.
    
    """
    
    found = False 
    query = f"'{folder_id}' in parents and mimeType = 'application/pdf'"
    nextPageToken = "FirstTime"
    while nextPageToken != None:
        try:
            if(nextPageToken == "FirstTime"):
                response =  drive_service.files().list(q=query, orderBy="name").execute()
            else:
                response =  drive_service.files().list(q=query, pageToken=nextPageToken, orderBy="name").execute()
            
            nextPageToken = response.get('nextPageToken')
            files = response.get('files')

            for file in files:
                # download the file
                get_pdf_from_link(file.get('id'))
                name = pdf_to_image_text()

                if((name.lower()) == (friend_name.lower())):
                    print("Found")
                    return True
        except Exception as e:
                print(e)
    return found


def convert_folder_link_to_id(folder_link):
    folder_id = folder_link.split('/')[-1]
    return folder_id


def get_pdf_from_file_id(file_id):
    request = drive_service.files().get_media(fileId = file_id)

    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fd=fh, request=request)

    done = False

    while not done:
        status , done = downloader.next_chunk()

    fh.seek(0)

    with open('checking.pdf', 'wb') as f:
        f.write(fh.read())
        f.close()

