from __future__ import annotations

from typing import Callable, Any

import flet as ft

from src.gui_flet.common_component import BaseViewComponent
from src.gui_flet.route_data import AppRoute


class MainMenuView(BaseViewComponent):
    def __init__(self, page: ft.Page, route: str) -> None:
        super().__init__(page, route)
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.vertical_alignment = ft.MainAxisAlignment.START
        self.app_bottom_appbar.home_button.visible = False

        self.controls.append(self._add_company_name_area())
        self.controls.append(ft.Container(expand=True))
        self.controls.append(self._add_main_menu_button())
        self.controls.append(ft.Container(expand=True))

    async def _click_employee_button(self, event: ft.Event) -> None:
        await self.page.push_route(AppRoute.EMPLOYEE_VIEW.value)

    async def _click_report_button(self, event: ft.Event) -> None:
        await self.page.push_route(AppRoute.REPORT_VIEW.value)

    async def _click_protocol_button(self, event: ft.Event) -> None:
        await self.page.push_route(AppRoute.PROTOCOL_VIEW.value)

    def _add_main_menu_button(self) -> ft.Container:
        container = MainMenuContainer(border_radius=15)
        container.create_button_name("ПЕРСОНАЛ", self._click_employee_button)
        container.create_button_name("ОТЧЕТЫ", self._click_report_button)
        container.create_button_name("ПРОТОКОЛЫ", self._click_protocol_button)
        return container

    @staticmethod
    def _add_company_name_area() -> ft.Row:
        company_area = CompanyNameArea()
        company_area.set_list_item("Кубанское ПМЭС", "1")
        company_area.set_list_item("Ростовское ПМЭС", "2")
        return company_area


class MainMenuContainer(ft.Container):
    def __init__(
        self,
        width: int = 500,
        height: int = 200,
        border_radius: int = 10,
        padding: int = 5,
    ) -> None:
        super().__init__()
        self.width = width
        self.height = height
        self.border_radius = border_radius
        self.padding = padding
        self.column = self.create_column()
        self.border = ft.Border.all(2, ft.Colors.BLUE_GREY_200)

        self.content = self.column

    @staticmethod
    def create_column() -> ft.Column:
        column = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            spacing=5,
        )
        return column

    def create_button_name(
        self, name_value: str, on_click_method: Callable[[ft.Event], Any]
    ) -> None:
        button = ft.Button(
            content=ft.Text(
                value=name_value,
                weight=ft.FontWeight.BOLD,
            ),
            on_click=on_click_method,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)),
            expand=True,
        )
        self.column.controls.append(button)


class CompanyNameArea(ft.Row):
    def __init__(self) -> None:
        super().__init__()
        self._company_list = ft.Dropdown(
            width=220, text="Выберите компанию", value="1", label="Компания"
        )
        self.alignment = ft.MainAxisAlignment.END
        self.run_alignment = ft.MainAxisAlignment.END

        self.controls.append(self._company_list)

    def set_list_item(self, company_name: str, company_id: str) -> None:
        list_item = ft.DropdownOption(text=company_name, key=company_id)
        self._company_list.options.append(list_item)
