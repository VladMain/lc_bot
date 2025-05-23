import threading
from interface.models.animated_box import animate_boxes


class AnimationController:
    def __init__(self, page, red_box, blue_box, logger):
        self.page = page
        self.red_box = red_box
        self.blue_box = blue_box
        self.logger = logger
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
            self.logger.debug('Анимация выключена')
            self.stop_animation_flag.set()
        else:
            self.logger.debug('Анимация включена')
            self.stop_animation_flag.clear()
            self.start_animation()