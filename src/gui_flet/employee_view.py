from __future__ import annotations

import flet as ft
from flet.controls import border

from gui_flet.route_data import AppRoute


class EmployeeView(ft.View):
    def __init__(self) -> None:
        super().__init__()
        self.route = AppRoute.EMPLOYEE_VIEW
        self._setup_view()

    def _setup_view(self) -> None:
        self.controls = [
            ft.Container(
                border=ft.Border.all(2, ft.Colors.BLUE_GREY_200),
                content=ft.Column([
                    ft.Button("Назад", on_click=self._click_come_back_button),
                ])
            )
        ]

    def _click_come_back_button(self) -> None:
        print("come back")
        self.page.navigate(AppRoute.MAIN_WINDOW)