import threading
from bot.bot_control import run_bot
from utils.window import Window
from utils.logger import logger


def change_bot_state(event, animation_controller):
    window = Window().window
    if not window:
        logger.warning('Сперва привяжите окно игры!')
        event.control.value = False
        return
    animation_controller.switch_logo_animation()
    if event.data == 'true':
        event.page.bot_state = True
        threading.Thread(target=run_bot, args=(event, window), daemon=True).start()
    else:
        event.page.bot_state = False
