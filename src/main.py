from __future__ import annotations

import flet as ft

from src.database.db_manager import DatabaseManager
from src.gui_flet.main_window import MainWindow
from src.settings import settings

app_db = DatabaseManager(settings)


def setup_window(page: ft.Page) -> None:
    page.window.width = 1024
    page.window.height = 800
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
