import base64
import streamlit as st
import drive_services as ds

def displayPDF(file):
    # Opening file from file path
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="600" type="application/pdf">'

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)

    
st.title("Certificate Finder")

st.write("This is a simple web app to help you find your certificate")


google_drive_link = st.text_input("Paste the google drive folder link")

try :
    folder_id = ds.convert_folder_link_to_id(google_drive_link)
except Exception as e:
    st.write(f"{e}")
    st.stop()

friend_name = st.text_input("Enter your friend's name")

if st.button("Find"):
    with st.spinner("Finding your certificate...."):

        if (ds.folder_to_certificate(folder_id, friend_name)):
            st.success("Certificate found!")
            displayPDF("checking.pdf")
        else:
            st.error("There is no certificate for this name")