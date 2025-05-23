import pytesseract
import os
import sys
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract\tesseract.exe'


def image_to_text(image_name: str, image_dir: str = 'images') -> str:
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    image_path = (os.path.join(base_path, image_dir, image_name))

    image = Image.open(image_path)
    text: str = pytesseract.image_to_string(image, lang='rus')
    return text
