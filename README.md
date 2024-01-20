#  Certificate Finder

# Get Started

### Install Python 
I was using Python 3.11.5 that I will recommend to use.

### Create Virtual Environment
Create a virtual environment using the following command:
```bash
python -m venv .venv
```

### Activate Virtual Environment
Activate the virtual environment using the following command:
```bash
.venv\Scripts\activate
```
```powershell
.venv\Scripts\activate.bat
```

### Install Dependencies
Install the dependencies using the following command:
```bash
pip install -r requirements.txt
```

## Note important things
- You need to install tesseract and add it to your path.
- You need to ccreate .env file and add the following variables:
```.env
CLIENT_SECRET_FILE = "ask me for this file ok"
TESSERACT_CMD = "Remeber to install and add the path"
```

## Issue
If any issue arrive please contact me at: deepeshkalurs@gmail.com