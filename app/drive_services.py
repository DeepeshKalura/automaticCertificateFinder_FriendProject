import os
import io
from typing import Optional
from dotenv import load_dotenv, find_dotenv
from googleapiclient.http import MediaIoBaseDownload

from app.google_mine import create_service
from app.helper import remove_query_param
from app.pdf_to_text import ocr_pdf_to_image_text

load_dotenv(find_dotenv())
SCOPE = ["https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/drive.appdata",  "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive.metadata", "https://www.googleapis.com/auth/drive.metadata.readonly",  "https://www.googleapis.com/auth/drive.readonly"]
API_NAME = 'drive'
API_VERSION = 'v3'

drive_service = create_service(os.getenv("CLIENT_SECRET_FILE"), API_NAME, API_VERSION, SCOPE)

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
                try:
                    get_pdf_from_file_id(file.get('id'))
                    name = ocr_pdf_to_image_text().lower()
                except Exception as e:
                    continue
                if((friend_name in name)):
                    return True

        except Exception as e:
                raise(e)
    return found

def folder_to_list_of_certificate(folder_id:str , friend_name:str, next_page_token ) -> list[list: str]:
    query = f"'{folder_id}' in parents and mimeType = 'application/pdf'"

    if(next_page_token == None):
        response =  drive_service.files().list(q=query, orderBy="name").execute()
    else:
        response =  drive_service.files().list(q=query, pageToken=next_page_token, orderBy="name").execute()

    next_page_token = response.get('nextPageToken')
    files = response.get('files')

    return [files, next_page_token]

   








def convert_folder_link_to_id(folder_link: str) -> str:
    """
    Converts a Google Drive folder link to its corresponding folder ID.

    Args:
        folder_link (str): The Google Drive folder link to be converted.

    Returns:
        str: The folder ID extracted from the folder link.

    Raises:
        ValueError: If the provided link is not a valid Google Drive folder link.
    """
    if "https://drive.google.com/drive/folders/" in folder_link:
        if "?usp=drive_link" in folder_link:
            folder_link = remove_query_param(folder_link, "?usp=drive_link")
     
        folder_id = folder_link.split('/')[-1]
        if(folder_id == "folder"):
            ValueError("Smart Hora Hai Londey, Kuch toh sahi daal.")
        return folder_id
    else:
        raise ValueError("The provided link is not a valid Google Drive folder link.")




def get_pdf_from_file_id(file_id: str):
    """
    Retrieves a PDF file from Google Drive based on the provided file ID.

    Args:
        file_id (str): The ID of the file to retrieve.

    Returns:
        None
    """
    request = drive_service.files().get_media(fileId=file_id)

    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fd=fh, request=request)

    done = False

    while not done:
        status, done = downloader.next_chunk()

    fh.seek(0)

    with open('checking.pdf', 'wb') as f:
        f.write(fh.read())
        f.close()

