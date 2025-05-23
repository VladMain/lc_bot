import threading
import time
import flet as ft
from math import pi
from interface.utils.theme_changer import theme_changed

from interface.models.animated_box import AnimatedBox, animate_boxes


def main(page: ft.Page):
    # Флаг для управления анимацией
    animation_active = True

    def on_window_event(e):
        nonlocal animation_active
        if e.data == "close":
            animation_active = False

    # Настройки страницы
    page.title = "Last Chaos Bot"
    page.window_width = 150
    page.window_height = 200
    page.padding = 20
    page.on_window_event = on_window_event

    # Функция для изменения вкладок
    def change_tab(e):
        tab1_content.visible = e.control.selected_index == 0
        tab2_content.visible = e.control.selected_index == 1
        tab3_content.visible = e.control.selected_index == 2
        page.update()

    # Создаем анимированные боксы
    red_box = AnimatedBox("#e9665a", None, 0)
    blue_box = AnimatedBox("#7df6dd", "#23262a", pi / 4)

    animated_box = ft.Stack(controls=[red_box, blue_box])

    # Содержимое вкладок
    tab1_content = ft.Column(
        [
            ft.Text("Содержимое первой вкладки", size=20),
            ft.ElevatedButton("Кнопка 1", on_click=lambda e: print("Кнопка 1 нажата"))
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
            ft.Image(src="https://picsum.photos/200/300", width=200, height=150),
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
            ft.Tab(text="Третья"),
        ],
        expand=1,
    )

    page.theme_mode = ft.ThemeMode.LIGHT
    switch = ft.Switch(label="Light theme", on_change=theme_changed)

    # Добавляем элементы на страницу
    page.add(
        animated_box,
        ft.Text("Приложение с вкладками", size=24, weight="bold"),
        tabs,
        tab1_content,
        tab2_content,
        tab3_content,
        switch
    )

    # Запускаем анимацию в потоке
    threading.Thread(
        target=animate_boxes,
        args=(page, lambda: animation_active, red_box, blue_box),
        daemon=True
    ).start()
