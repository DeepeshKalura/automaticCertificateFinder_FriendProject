import os
import io

from dotenv import load_dotenv, find_dotenv
from google_mine import create_service
from googleapiclient.http import MediaIoBaseDownload


load_dotenv(find_dotenv())
SCOPE = ['https://www.googleapis.com/auth/drive.readonly']
API_NAME = 'drive'
API_VERSION = 'v3'

drive_service = create_service(os.getenv('CLIENT_SECRET_FILE'), API_NAME, API_VERSION, SCOPE)

print(dir(drive_service))

folder_link = "https://drive.google.com/drive/folders/1my5S5mOPaIk7jkQOv-P62_dpLwAmFpnm"
folder_id = folder_link.split('/')[-1]
# print(folder_id)

page_token = None
results = drive_service.files().list(
    spaces='drive',
    fields="files(id, name)",
    pageToken=page_token
).execute()

print("I got excuted")
files = results.get('files', [])


for file in files:
    print("Lol never come inside")
    print(file['name'], file['id'])




# try :
#     request = service.files().get_media(fileId = folderId)
#     fh = io.BytesIO()
#     downloader = MediaIoBaseDownload(fh, request)

#     done = False 

#     while done is False:
#         status , done = downloader.next_chunk()

#     with open('2.pdf', 'wb') as f:
#         f.write(fh.getvalue())

# except Exception as e:
#     print(f"{e}")



