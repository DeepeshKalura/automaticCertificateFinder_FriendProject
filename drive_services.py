import os
import io
from urllib.parse import urlparse, parse_qs
from dotenv import load_dotenv, find_dotenv
from google_mine import create_service
from googleapiclient.http import MediaIoBaseDownload
import cache
from pdf_to_text import pdf_to_image_text
from logs import infoLog, errorLog, criticalLog

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
    infoLog("Start searching for the certificate")
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
                try:
                    get_pdf_from_file_id(file.get('id'))
                    name = pdf_to_image_text().lower()
                    cache.insert_file(file_id=file.get('id'), name=name, file_name=file.get('name'), folder_id=folder_id)
                except Exception as e:
                    errorLog(f"Error getting the pdf from link {e}")
                    continue
                if((friend_name in name)):
                    infoLog("Certificate found")
                    return True

        except Exception as e:
                errorLog(f"Error getting the pdf from link {e}")
    return found



def convert_folder_link_to_id(folder_link):
    infoLog("Start Converting the folder link to folder id")
    try:
        parsed_url = urlparse(folder_link)
        query_params = parse_qs(parsed_url.query)

        if 'usp' in query_params:
            folder_link = folder_link.split('?')[0]
        if not folder_link.startswith("https://drive.google.com/drive/folders/"):
            raise ValueError("Invalid folder link format. Must start with 'https://drive.google.com/drive/folders/'.")

        folder_id = folder_link.split('/')[-1]
        
        if not folder_id:
            criticalLog("Invalid folder link. Unable to extract folder ID.")
            raise ValueError("Invalid folder link. Unable to extract folder ID.")

        infoLog("Folder link converted to folder ID successfully")
        return folder_id

    except ValueError as ve:
        errorLog(f"Error converting folder link to ID: {ve}")
        raise ve

    except Exception as e:
        errorLog(f"Error converting folder link to ID: {e}")
        raise ValueError(f"Error converting folder link to ID: {e}")




def get_pdf_from_file_id(file_id):
    infoLog("Start getting the pdf from link")
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
    infoLog("PDF downloaded successfully")

