import pytesseract
import os
import sys
import numpy as np
from PIL import Image, ImageGrab
from utils.logger import logger


pytesseract.pytesseract.tesseract_cmd = r'E:\Tesseract\tesseract.exe'


def image_to_text(image_name: str = '', image_dir: str = 'images', make_screenshot: bool = True, window=None) -> str:
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    image_path = os.path.join(base_path, image_dir, image_name)

    if make_screenshot and window:

        # Делаем скриншот области экрана, где находится окно
        screenshot = ImageGrab.grab(bbox=(window.left, window.top, window.left + window.width, window.top + window.height))
        # Распознаём текст (можно указать несколько языков: 'eng+rus')
        text = pytesseract.image_to_string(screenshot, lang='rus')
        return text
    elif make_screenshot:
        logger.warning("Активное окно не найдено!")
    else:
        image = Image.open(image_path)
        text: str = pytesseract.image_to_string(image, lang='rus')
        return text
