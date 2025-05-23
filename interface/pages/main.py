import flet as ft
from math import pi

from bot.actions.bot_state import change_bot_state
from bot.bot_control import run_bot
from interface.utils.animation_handler import AnimationController
from interface.utils.theme_changer import theme_changed

from interface.models.animated_box import AnimatedBox
from utils.binding import bind_window, WINDOW
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

    binded_window_title = ft.Text(
        "Нет привязанного окна",
        size=14,
        color=ft.Colors.BLACK,
        weight="bold",
        italic=True
    )

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
            ft.Text("Бот", size=20),
            ft.Switch("Включить бота",
                      value=False,
                      on_change=lambda e: change_bot_state(e, animation_controller)),
            ft.ElevatedButton("Нажать 2")
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

    bind_button = ft.ElevatedButton(
        "Привязать",
        width=130,
        height=30,
        on_click=bind_window,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=5),
            padding=10,
            side=ft.BorderSide(1, ft.Colors.GREY_600)
        )
    )

    tab3_content = ft.Column(
        [
            ft.Text("Привязать окно:", size=20),
            ft.Row(  # Используем Row для размещения элементов в одной строке
                controls=[
                    bind_button,
                    ft.Container(  # Контейнер для красивого отображения текста
                        content=binded_window_title,
                        padding=ft.padding.only(left=20, right=20),
                        border=ft.border.all(1, ft.Colors.GREY_600),
                        border_radius=5,
                        bgcolor=ft.Colors.GREY_100,
                        height=30,
                        alignment=ft.alignment.center
                    )
                ],
                alignment=ft.MainAxisAlignment.START,
                spacing=10
            )
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

    page.binded_window_title = binded_window_title
    page.bind_button = bind_button
    page.add(main_content)
