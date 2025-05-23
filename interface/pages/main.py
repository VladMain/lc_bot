import threading

import flet as ft

from math import pi
from interface.models.animated_box import AnimatedBox, animate_boxes


def main(page: ft.Page):
    # Настройки страницы
    page.title = "Приложение с вкладками"
    page.window_width = 600
    page.window_height = 400
    page.padding = 20

    # Функция для изменения вкладок
    def change_tab(e):
        # Скрываем все вкладки
        tab1_content.visible = False
        tab2_content.visible = False
        tab3_content.visible = False

        # Показываем выбранную вкладку
        if e.control.selected_index == 0:
            tab1_content.visible = True
        elif e.control.selected_index == 1:
            tab2_content.visible = True
        elif e.control.selected_index == 2:
            tab3_content.visible = True

        page.update()

    animated_box = ft.Stack(
        controls=[
            AnimatedBox("#e9665a", None, 0),
            AnimatedBox("#7df6dd", "#23262a", pi / 4)
        ]
    )

    # Содержимое вкладок
    tab1_content = ft.Column(
        [
            ft.Text("Содержимое первой вкладки", size=20),
            ft.ElevatedButton("Кнопка 1", on_click=lambda e: print("Кнопка 1 нажата"))
        ],
        visible=True  # Первая вкладка видна по умолчанию
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

    # Добавляем элементы на страницу
    page.add(
        animated_box,
        ft.Text("Приложение с вкладками", size=24, weight="bold"),
        tabs,
        tab1_content,
        tab2_content,
        tab3_content,
    )

    threading.Thread(target=animate_boxes, args=(page,)).start()
