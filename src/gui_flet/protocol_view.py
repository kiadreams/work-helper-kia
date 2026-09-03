from __future__ import annotations

import flet as ft

from gui_flet.route_data import AppRoute


class ProtocolView(ft.View):
    def __init__(self) -> None:
        super().__init__()
        self.route = AppRoute.PROTOCOL_VIEW
        self._setup_view()

    def _setup_view(self) -> None:
        self.controls = [
            ft.Container(
                content=ft.Column([
                    ft.Button("Назад", on_click=self._click_come_back_button),
                ])
            )
        ]

    def _click_come_back_button(self) -> None:
        print("come back")
        self.page.navigate(AppRoute.MAIN_WINDOW)
