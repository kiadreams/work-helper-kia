from __future__ import annotations

import flet as ft

from gui_flet.route_data import AppRoute
from gui_flet.common_view_component import BottomBar, TopAppBar


class MainMenuView(ft.View):
    def __init__(self) -> None:
        super().__init__(route=AppRoute.MAIN_MENU_VIEW.value)
        self._setup_view()

    def _setup_view(self) -> None:
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.appbar = self._add_top_app_bar()
        self._create_main_menu_button()
        self.bottom_appbar = self._add_bottom_bar()

    async def _click_employee_button(self, event: ft.Event) -> None:
        await self.page.push_route(AppRoute.EMPLOYEE_VIEW.value)

    async def _click_report_button(self, event: ft.Event) -> None:
        await self.page.push_route(AppRoute.REPORT_VIEW.value)

    async def _click_protocol_button(self, event: ft.Event) -> None:
        await self.page.push_route(AppRoute.PROTOCOL_VIEW.value)

    def _create_main_menu_button(self) -> None:
        self.controls = [
            ft.Container(
                width=500,
                height=200,
                border=ft.Border.all(2, ft.Colors.BLUE_GREY_200),
                border_radius=10,
                padding=5,
                content=ft.Column([
                    ft.Button(content=ft.Text("Персонал"),
                              style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)),
                              expand=True,
                              on_click=self._click_employee_button),
                    ft.Button(content=ft.Text("Отчеты"),
                              style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)),
                              expand=True,
                              on_click=self._click_report_button),
                    ft.Button(content=ft.Text("Протоколы"),
                              style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)),
                              expand=True,
                              on_click=self._click_protocol_button),
                ],
                    horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                    spacing=5),
            )
        ]

    @staticmethod
    def _add_bottom_bar() -> ft.BottomBar:
        bottom_bar = BottomBar()
        bottom_bar.home_button.visible = False
        return bottom_bar

    @staticmethod
    def _add_top_app_bar() -> ft.AppBar:
        app_bar = TopAppBar()
        return app_bar
