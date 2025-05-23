import threading
from bot.bot_control import run_bot


def change_bot_state(event, animation_controller):
    animation_controller.switch_logo_animation()
    if event.data == 'true':
        event.page.bot_state = True
        threading.Thread(target=run_bot, args=(event,), daemon=True).start()
    else:
        event.page.bot_state = False
