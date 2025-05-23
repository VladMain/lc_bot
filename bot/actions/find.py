import pyautogui
import os
import sys
from utils.logger import logger


ASSETS_BASE_DIR = os.path.join('assets', 'images')


def get_path(relative_path, directory=''):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    return os.path.join(base_path, ASSETS_BASE_DIR, directory, relative_path)


# TODO: change locateOnScreen on locateOnWindow and find a way to bind a window with exact title
def find(image: str, min_search_time: float, confidence: float):
    image_name = image.split("/")[-1]
    logger.debug(f'Find {image_name} with minimal search time = {min_search_time} and confidence = {confidence}')
    result = None
    try:
        result = pyautogui.locateOnScreen(image, minSearchTime=min_search_time, confidence=confidence)
    except pyautogui.ImageNotFoundException:
        logger.warning(f'NOT FOUND {image_name}')
    return result
