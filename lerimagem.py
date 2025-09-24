
import pytesseract as ocr

from PIL import Image


phrase = ocr.image_to_string(Image.open('PHDR_Auto1.jpg'), lang='por')
print(phrase)

