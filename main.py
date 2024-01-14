import fitz 
import os
import glob
from PIL import Image
from pytesseract import pytesseract
 
freindName = "Deepesh"

count = 0

# TODO: pdf images --> image modify kerna hai --> text extract --> search

# generate image from pdf


doc = fitz.open('1-100-1.pdf') 
for page in doc: 
	pix = page.get_pixmap(matrix=fitz.Identity, dpi=None,colorspace=fitz.csRGB, clip=None, alpha=False, annots=True) 
	pix.save("samplepdfimage%i.jpg" % page.number) # save file 

# Save image
	
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

print(text)





# Searching the text

# for filename in glob.glob('dataset/*.txt'):
#     with open(filename, 'r') as f:
#         content = f.read()
#         count += 1
#         if freindName in content:
#             print(freindName + " is in " + filename)

# print("Done")
# print("Total files: " + str(count))
	

# old way to extract image from pdf I don't like it 
# reader = pypdf.PdfReader('1-100-1.pdf')
# page = reader.pages[0]
# count = 0

# for image in page.images:

#     with open(str(count) + image.name, "wb") as fp:
#         fp.write(image.data)
#         count += 1