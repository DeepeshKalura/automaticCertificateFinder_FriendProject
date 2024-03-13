import base64
import streamlit as st

def remove_query_param(url: str, param: str) -> str:
    """
    Removes the specified query parameter from the given URL.

    Args:
        url (str): The URL from which the query parameter needs to be removed.
        param (str): The query parameter to be removed.

    Returns:
        str: The updated URL with the query parameter removed.
    """
    param_start = url.find(param)
    
    if param_start != -1:
        param_end = url.find('&', param_start)
        if param_end == -1:
            param_end = len(url)
        else:
            param_end += 1 
        url = url[:param_start] + url[param_end:]
    
    return url


def displayPDF(file):
    """
    Display a PDF file in the streamlit app.

    Parameters:
    file (str): The path to the PDF file.
def displayPDF(file):

    Returns:
    None
    """
    try:
        with open(file, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="600" type="application/pdf">'
        st.markdown(pdf_display, unsafe_allow_html=True)
    except Exception as e:

        st.write(f"{e}")