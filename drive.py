import requests 
from io import StringIO


googleDrive = "https://drive.google.com/drive/folders/1my5S5mOPaIk7jkQOv-P62_dpLwAmFpnm"
response = requests.get(googleDrive).text

with open('googleDrive.html', 'w') as f:
    f.write(response)




