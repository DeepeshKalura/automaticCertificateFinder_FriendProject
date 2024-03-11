import fitz 
from PIL import Image
from pytesseract import pytesseract
import os
from dotenv import load_dotenv, find_dotenv
# from app.logs import infoLog, errorLog, criticalLog


load_dotenv(find_dotenv())

def pdf_to_image_text() -> str:
	# infoLog("Start converting the pdf to image and then extract the text")
	"""
	Converts a PDF file to image and extracts text from the image.

	Returns:
		str: The extracted text from the PDF image.
	"""
	try:
		doc = fitz.open('checking.pdf')
	except Exception as e:
		# errorLog(f"File not found {e}")
		raise f"File not found {e}"
	for page in doc: 
		pix = page.get_pixmap(matrix=fitz.Identity, dpi=None,colorspace=fitz.csRGB, clip=None, alpha=False, annots=True) 
		pix.save("samplepdfimage%i.jpg" % page.number) 
	im = Image.open("samplepdfimage0.jpg")
	width, height = im.size
	left = width / 8
	top = height / 2.2
	right = width  - width/8
	bottom = height - height/2.4
	im1 = im.crop((left, top, right, bottom))
	im1.save('samplepdfimage0.jpg')
	pytesseract.tesseract_cmd = os.getenv('TESSERACT_CMD')
	img = Image.open("samplepdfimage0.jpg")
	text = pytesseract.image_to_string(img)
	# infoLog("PDF converted to image and text extracted successfully") 
	return text.strip()
