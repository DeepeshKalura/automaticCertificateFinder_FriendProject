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
        print('Download Progress {0} %'.format(status.progress() * 100))

    fh.seek(0)

    with open('checking.pdf', 'wb') as f:
        f.write(fh.read())
        f.close()


    
def folder_to_files(folder_id, friend_name):
    
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

                if(name == friend_name):
                    return True

        except Exception as e:
                print(e)
    return False

    

folder_id = "1my5S5mOPaIk7jkQOv-P62_dpLwAmFpnm"
found = folder_to_files(folder_id, "Deepesh Kalura")

if(found):
    print("checking done")
else:
    print("not found")



