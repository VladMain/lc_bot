import time
import pyautogui
from bot.actions.find import get_path, find


ASSETS_BASE_DIR = 'assets/'


def run_bot(e, animation_controller):
    animation_controller.switch_logo_animation()

    eng_pressf_1080 = get_path('pressfeng.png')
    cycles = 0

    # TODO: change locateOnScreen on locateOnWindow and find a way to bind a window with exact title
    while e.data == 'true' and cycles < 10000:
        print(cycles)
        ore_list1 = []
        for ore in ore_list1:
            ore_result = find(ore, min_search_time=0.1, confidence=0.55)
            if ore_result:
                pyautogui.hotkey('F')
                break
        time.sleep(2)
        cycles += 1
