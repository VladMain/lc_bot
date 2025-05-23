import threading

from flet import Container, border, alignment, Page
import time
from math import pi

from utils.logger import get_logger


log = get_logger()


class AnimatedBox(Container):
    def __init__(self, border_color, bg_color, rotate_angle):
        super().__init__(
            width=48,
            height=48,
            border=border.all(2.5, border_color),
            bgcolor=bg_color,
            border_radius=2,
            rotate=rotate_angle,
            alignment=alignment.center,
            animate_rotation=700,
        )


def animate_boxes(page: Page, red_box: AnimatedBox, blue_box: AnimatedBox,
                  stop_event: threading.Event = True):
    clock_wise_rotate = pi / 4
    counter_clock_wise_rotate = -pi * 2

    counter = 0
    while not stop_event.is_set():
        try:
            if 0 <= counter <= 4:
                red_box.rotate = counter_clock_wise_rotate
                blue_box.rotate = clock_wise_rotate

                page.update()

                clock_wise_rotate += pi / 2
                counter_clock_wise_rotate -= pi / 2

                counter += 1
                time.sleep(0.7)

            if 5 <= counter <= 9:
                clock_wise_rotate -= pi / 2
                counter_clock_wise_rotate += pi / 2

                red_box.rotate = counter_clock_wise_rotate
                blue_box.rotate = clock_wise_rotate

                page.update()

                counter += 1
                time.sleep(0.7)

            if counter > 9:
                counter = 0
        except Exception as e:
            log.error(f"Animation stopped: {e}")
            break
