import flet as ft

from interface.pages.main import main

ASSETS_DIR = 'assets'

if __name__ == '__main__':
    ft.app(target=main, assets_dir=ASSETS_DIR)
