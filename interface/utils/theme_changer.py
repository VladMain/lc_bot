import flet as ft


def theme_changed(event: ft.ControlEvent) -> None:
    event.page.theme_mode = (
        ft.ThemeMode.DARK
        if event.page.theme_mode == ft.ThemeMode.LIGHT
        else ft.ThemeMode.LIGHT
    )
    event.control.label = (
        "Light theme" if event.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
    )
    event.page.update()
