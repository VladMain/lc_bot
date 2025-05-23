import pygetwindow as pgw
import time
from utils.logger import logger
from utils.window import Window


WINDOW = Window()


def bind_window(e):
    bind_button_previous_text = e.page.bind_button.text
    try:
        e.page.bind_button.text = 'ЖМИ НА ОКНО'
        e.page.update()
        current_window = pgw.getActiveWindow()
        while pgw.getActiveWindow() == current_window:
            time.sleep(0.1)
        WINDOW.set_window(pgw.getActiveWindow())
        window = WINDOW.window
        logger.debug(f'Привязано окно: "{window.title}"')
        e.page.bind_button.text = bind_button_previous_text
        e.page.binded_window_title.value = window.title
        e.page.update()
    except IndexError:
        logger.error('Окно не найдено!')
        e.page.binded_window_title.value = "Окно не найдено"
        e.page.update()
