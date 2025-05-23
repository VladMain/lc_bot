import pygetwindow as pgw
import time

from utils.logger import get_logger

WINDOW = None
logger = get_logger()


def bind_window():
    try:
        global WINDOW
        current_window = pgw.getActiveWindow()
        while pgw.getActiveWindow() == current_window:
            time.sleep(0.1)
        WINDOW = pgw.getActiveWindow()
        logger.debug(f'Locked window: {WINDOW.title}')
    except IndexError:
        print("Window not found!")