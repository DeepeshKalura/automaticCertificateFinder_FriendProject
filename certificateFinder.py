import streamlit as st
import app.drive_services as ds
import app.cache as cache
from app.helper import displayPDF

    
st.title("Certificate Finder")

st.write("This is a simple web app to help you find your certificate")


google_drive_link = st.text_input("Paste the google drive folder link")

try :
    folder_id = ds.convert_folder_link_to_id(google_drive_link)
except Exception as e:
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