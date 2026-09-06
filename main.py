from __future__ import annotations
import flet as ft
import asyncio

from src.gui_flet.main_window import MainWindow


def setup_window(page: ft.Page):
    page.window.width = 1600
    page.window.height = 1200
    page.title = "Рабочий помощник КИА"
    page.window.title_bar_hidden = True
    page.run_task(page.window.center)
    if page.web:
        page.run_task(ft.BrowserContextMenu().disable)


ft.run(
    before_main=setup_window,
    main=MainWindow,
    view=ft.AppView.FLET_APP_HIDDEN,
)



