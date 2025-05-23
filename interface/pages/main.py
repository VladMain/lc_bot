import flet as ft
from math import pi

from interface.utils.animation_handler import AnimationController
from interface.utils.theme_changer import theme_changed

from interface.models.animated_box import AnimatedBox
from utils.logger import logger


def main(page: ft.Page):

    # Настройки страницы
    page.title = "Last Chaos Bot"
    page.window_always_on_top = True
    page.window.width = 400
    page.window.height = 700
    page.window.always_on_top = True
    page.window.min_width = 400  # Запрещаем изменение размера меньше минимального
    page.window.min_height = 700
    page.padding = 10  # Уменьшаем внутренние отступы
    page.theme_mode = ft.ThemeMode.LIGHT

    # Функция для изменения вкладок
    def change_tab(e):
        tab1_content.visible = e.control.selected_index == 0
        tab2_content.visible = e.control.selected_index == 1
        tab3_content.visible = e.control.selected_index == 2
        page.update()

    # Создаем анимированные боксы
    red_box = AnimatedBox("#bcbcbc", None, 0)
    blue_box = AnimatedBox("#bcbcbc", "#23262a", pi / 4)

    animation_controller = AnimationController(
        page=page,
        red_box=red_box,
        blue_box=blue_box
    )

    animated_box = ft.Stack(controls=[red_box, blue_box])

    # Содержимое вкладок
    tab1_content = ft.Column(
        [
            ft.Text("Содержимое первой вкладки", size=20),
            ft.ElevatedButton("Кнопка 1", on_click=animation_controller.switch_logo_animation)
        ],
        visible=True
    )

    tab2_content = ft.Column(
        [
            ft.Text("Содержимое второй вкладки", size=20),
            ft.TextField(label="Поле ввода"),
            ft.Checkbox(label="Чекбокс", value=False)
        ],
        visible=False
    )

    tab3_content = ft.Column(
        [
            ft.Text("Содержимое третьей вкладки", size=20),
            ft.Text("Это демонстрационное изображение")
        ],
        visible=False
    )

    # Создаем вкладки
    tabs = ft.Tabs(
        selected_index=0,
        on_change=change_tab,
        tabs=[
            ft.Tab(text="Первая"),
            ft.Tab(text="Вторая"),
            ft.Tab(text="Настройки"),
        ],
        expand=0,
    )

    switch = ft.Switch(label="Light theme", on_change=theme_changed)

    main_content = ft.Column(
        controls=[
            animated_box,
            ft.Text("Бот", size=24, weight="bold"),
            tabs,
            ft.Container(
                content=ft.Column(
                    controls=[tab1_content, tab2_content, tab3_content],
                    scroll=ft.ScrollMode.AUTO,
                    expand=True
                ),
                expand=True
            ),
            # Переключатель внизу с отступом сверху
            ft.Divider(),
            ft.Container(
                content=switch,
                padding=ft.padding.only(top=10),
                alignment=ft.alignment.center
            )
        ],
        expand=True
    )

    page.add(main_content)
