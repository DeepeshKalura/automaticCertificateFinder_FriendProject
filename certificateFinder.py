import base64
import streamlit as st
import drive_services as ds
from logs import  infoLog, errorLog, criticalLog
import cache

def displayPDF(file):
    """
    Display a PDF file in the streamlit app.

    Parameters:
    file (str): The path to the PDF file.

    Returns:
    None
    """
    try:
        with open(file, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="600" type="application/pdf">'
        st.markdown(pdf_display, unsafe_allow_html=True)
        infoLog("PDF displayed successfully")
    except Exception as e:

        st.write(f"{e}")
        errorLog(f"Error displaying PDF {e}")
    
st.title("Certificate Finder")

st.write("This is a simple web app to help you find your certificate")


google_drive_link = st.text_input("Paste the google drive folder link")

try :
    infoLog("Start Converting the folder link to folder id")
    folder_id = ds.convert_folder_link_to_id(google_drive_link)
    infoLog("Folder link converted to folder id successfully")
except Exception as e:
    errorLog(f"Error converting folder link to ID")
    st.write(f"{e}")
    st.stop()

friend_name = st.text_input("Enter your friend's name")
friend_name = friend_name.lower()

if st.button("Find"):
    with st.spinner("Finding your certificate...."):

        response = cache.folder_id_exists(folder_id)

        if (not response):
            cache.insert_folder(folder_id)
            if (ds.folder_to_certificate(folder_id, friend_name)):
                st.success("Certificate found!")
                displayPDF("checking.pdf")
            else:
                st.error("There is no certificate for this name")
        else:
            value = cache.file_exists(friend_name, folder_id)
            if (value is None):
                if (ds.folder_to_certificate(folder_id, friend_name)):
                    st.success("Certificate found!")
                    displayPDF("checking.pdf")
            else:
                ds.get_pdf_from_link(response[0])
                st.success("Certificate found!")
                displayPDF("checking.pdf")
    criticalLog("End of the program")