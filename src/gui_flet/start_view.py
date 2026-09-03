from __future__ import annotations

import flet as ft
from flet import View, control


class StartView(ft.View):
    def __init__(self, page: ft.Page) -> None:
        self.app_page = page
        self.route = "/start_view"
        self._setup_view()

    def _setup_view(self) -> None:
        self.controls = [
            ft.Container(
                content=ft.Column([
                    ft.Button(content="Персонал"),
                    ft.Button(content="Отчеты"),
                    ft.Button(content="Протоколы"),
                ])
            )
        ]


# def start_view(page: ft.Page):
#     view = ft.View(
#         route="/",
#         controls=[
#             ft.Container(
#                 content=ft.Column([
#                     ft.Button(content="Персонал"),
#                     ft.Button(content="Отчеты"),
#                     ft.Button(content="Протоколы"),
#                 ])
#             )
#         ]
#     )
#     return view


