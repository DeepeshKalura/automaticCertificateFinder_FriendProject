import fitz 
from PIL import Image
from pytesseract import pytesseract
 
freindName = "Deepesh"


def pdf_to_image_text():
	doc = fitz.open('checking.pdf')
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

	# Extract text from image
	pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
	img = Image.open("samplepdfimage0.jpg")
	text = pytesseract.image_to_string(img)  
	return text


