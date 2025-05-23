import pygetwindow as pgw
import time
from utils.logger import logger


WINDOW = None


def bind_window(e):
    bind_button_previous_text = e.page.bind_button.text
    try:
        global WINDOW
        e.page.bind_button.text = 'ЖМИ НА ОКНО'
        e.page.update()
        current_window = pgw.getActiveWindow()
        while pgw.getActiveWindow() == current_window:
            time.sleep(0.1)
        WINDOW = pgw.getActiveWindow()
        logger.debug(f'Привязано окно: "{WINDOW.title}"')
        e.page.bind_button.text = bind_button_previous_text
        e.page.binded_window_title.value = WINDOW.title
        e.page.update()
    except IndexError:
        logger.error('Окно не найдено!')
        e.page.binded_window_title.value = "Окно не найдено"
        e.page.update()
