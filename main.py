from __future__ import annotations

import flet as ft
from src.gui_flet.main_window import MainWindow


ft.run(
    MainWindow,
    view=ft.AppView.FLET_APP_HIDDEN,
    # view=ft.AppView.WEB_BROWSER
)
