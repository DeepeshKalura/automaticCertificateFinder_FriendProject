import os
import io

from dotenv import load_dotenv, find_dotenv
from google_mine import create_service
from googleapiclient.http import MediaIoBaseDownload

load_dotenv(find_dotenv())
SCOPE = ["https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/drive.appdata",  "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive.metadata", "https://www.googleapis.com/auth/drive.metadata.readonly",  "https://www.googleapis.com/auth/drive.readonly"]
API_NAME = 'drive'
API_VERSION = 'v3'

drive_service = create_service(os.getenv("CLIENT_SECRET_FILE"), API_NAME, API_VERSION, SCOPE)

folder_id = "1my5S5mOPaIk7jkQOv-P62_dpLwAmFpnm"

# First with the file link 

def get_pdf_from_link (file_id):

    # file_id = '10n2-mQLoLftelod-Mu1EefUFOLjfRHK5'

    request = drive_service.files().get_media(fileId = file_id)

    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fd=fh, request=request)

    done = False

    while not done:
        status , done = downloader.next_chunk()
        print('Download Progress {0} %'.format(status.progress() * 100))


    fh.seek(0)

    with open('downloadPdf.pdf', 'wb') as f:
        f.write(fh.read())
        f.close()


# I have to find the file_id  from the folder_id
    
def folder_to_files_code(folder_id):
    query = f"'{folder_id}' in parents and mimeType = 'application/pdf'"
    count = 0
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
                # print(f"file name is : {file.get('name')} and id is : {file.get('id')}")
                count += 1
            
        except Exception as e:
            print(e)
