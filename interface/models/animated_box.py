from flet import Container, border, alignment
import time
from math import pi


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


def animate_boxes(page):
    clock_wise_rotate = pi / 4
    counter_clock_wise_rotate = -pi * 2

    red_box = page.controls[0].controls[0]
    blue_box = page.controls[0].controls[1]

    counter = 0
    while page:
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