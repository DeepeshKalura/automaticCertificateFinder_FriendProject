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

# download this file folder 

# First with the file link 

file_id = '10n2-mQLoLftelod-Mu1EefUFOLjfRHK5'

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
    
print(f'folder id is :  {folder_id}')

response =  drive_service.files().list(q=f"'{folder_id}' in parents and mimeType = 'application/pdf'").execute()

for file in response.get('files', []):
    print(f"Found file: {file.get('name')} with id: {file.get('id')}")
