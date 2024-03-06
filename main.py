from PIL import Image
import pytesseract

image = Image.open('image-7.jpeg')

text = pytesseract.image_to_string(image)

print(text)