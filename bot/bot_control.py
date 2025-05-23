import time
import pyautogui
from bot.actions.find import get_path, find
from utils.logger import logger


def run_bot(e):

    drake_rawr_emotion = get_path('rawr_emotion.png', directory='pets\p1\drake')
    cycle = 0

    while e.page.bot_state and cycle < 10000:
        logger.debug(f'Бот включен: {cycle}с')
        if find(drake_rawr_emotion, min_search_time=0.1, confidence=0.55):
            logger.debug(f'Found image: {drake_rawr_emotion}')
            pyautogui.hotkey('I')
        time.sleep(2)
        cycle += 1
