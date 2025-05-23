import threading
from interface.models.animated_box import animate_boxes
from utils.logger import get_logger


log = get_logger()


class AnimationController:
    def __init__(self, page, red_box, blue_box):
        self.page = page
        self.red_box = red_box
        self.blue_box = blue_box
        self.stop_animation_flag = threading.Event()
        self.stop_animation_flag.set()

    def start_animation(self):
        threading.Thread(
            target=animate_boxes,
            args=(self.page, self.red_box, self.blue_box, self.stop_animation_flag),
            daemon=True
        ).start()

    def switch_logo_animation(self, event):
        if not self.stop_animation_flag.is_set():
            log.debug('Анимация выключена')
            self.stop_animation_flag.set()
        else:
            log.debug('Анимация включена')
            self.stop_animation_flag.clear()
            self.start_animation()
        self.recolor_boxes()

    def recolor_boxes(self):
        if self.red_box.border.bottom.color == '#bcbcbc':
            log.debug('Красим лого в цветное')
            self.red_box.border.bottom.color = '#e9665a'
            self.red_box.border.top.color = '#e9665a'
            self.red_box.border.left.color = '#e9665a'
            self.red_box.border.right.color = '#e9665a'

            self.blue_box.border.bottom.color = '#7df6dd'
            self.blue_box.border.top.color = '#7df6dd'
            self.blue_box.border.left.color = '#7df6dd'
            self.blue_box.border.right.color = '#7df6dd'
            self.blue_box.bgcolor = '#38761d'
        else:
            log.debug('Красим лого в серый')
            self.red_box.border.bottom.color = '#bcbcbc'
            self.red_box.border.top.color = '#bcbcbc'
            self.red_box.border.left.color = '#bcbcbc'
            self.red_box.border.right.color = '#bcbcbc'

            self.blue_box.border.bottom.color = '#bcbcbc'
            self.blue_box.border.top.color = '#bcbcbc'
            self.blue_box.border.left.color = '#bcbcbc'
            self.blue_box.border.right.color = '#bcbcbc'
            self.blue_box.bgcolor = '#23262a'
