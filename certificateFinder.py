import streamlit as st
import app.drive_services as ds
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
        pass