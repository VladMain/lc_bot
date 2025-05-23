import time

import pyautogui
from bot.actions.find import get_path, find
from ocr.utils.recognition import image_to_text
from utils.logger import logger
from interception

p1_food_image = get_path('p1_food.png', directory='items')


def feed_pet(window):

    hungry_text = 'Сытость '
    is_hungry = True
    count = 0

    while is_hungry and count < 10:
        full_text = image_to_text(make_screenshot=True, window=window)
        try:
            if full_text.find(hungry_text):
                current_hungry = int(full_text[full_text.find(hungry_text) + 8:].split('/')[0])
                logger.debug(f'Сытость питомца - {current_hungry}')
                if current_hungry > 100 or current_hungry < 0:
                    count += 1
                    continue
                elif current_hungry > 95:
                    is_hungry = False
                else:
                    p1_food = find(p1_food_image)
                    if p1_food:
                        logger.debug('Кушаем еду')
                        click(p1_food, window)
                        continue
                    else:
                        logger.warning('Не найдена еда для п1 питомцев!')
        except Exception:
            pass
        time.sleep(2)
        count += 1
