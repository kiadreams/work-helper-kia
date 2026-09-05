from __future__ import annotations

from typing import Callable, Any

import flet as ft

from src.gui_flet.route_data import AppRoute
from src.gui_flet.common_view_component import BottomBar, TopAppBar


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
        container = MainMenuContainer(border_radius=15)
        container.create_button_name("ПЕРСОНАЛ", self._click_employee_button)
        container.create_button_name("ОТЧЕТЫ", self._click_report_button)
        container.create_button_name("ПРОТОКОЛЫ", self._click_protocol_button)
        self.controls = [container]

    @staticmethod
    def _add_bottom_bar() -> ft.BottomBar:
        bottom_bar = BottomBar()
        bottom_bar.home_button.visible = False
        return bottom_bar

    @staticmethod
    def _add_top_app_bar() -> ft.AppBar:
        app_bar = TopAppBar()
        return app_bar


class MainMenuContainer(ft.Container):
    def __init__(self,
                 width: int = 500,
                 height: int = 200,
                 border_radius: int = 10,
                 padding: int = 5) -> None:
        super().__init__()
        self.width = width
        self.height = height
        self.border_radius = border_radius
        self.padding = padding
        # self.border
        self.column = self.create_column()
        self._setup_view()

    def _setup_view(self) -> None:
        self.content = self.column
        self.border = ft.Border.all(2, ft.Colors.BLUE_GREY_200)

    @staticmethod
    def create_column() -> ft.Column:
        column = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            spacing=5,
        )
        return column

    def create_button_name(
            self,
            name_value: str,
            on_click_method: Callable[[ft.Event], Any]
    ) -> None:
        button = ft.Button(
            content=ft.Text(
                value=name_value,
                weight=ft.FontWeight.NORMAL,
            ),
            on_click=on_click_method,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)),
            expand=True,
        )
        self.column.controls.append(button)


class CompanyNameArea(ft.Row):
    def __init__(self, name: str) -> None:
        super().__init__()