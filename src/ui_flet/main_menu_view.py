from collections.abc import Callable
from typing import Any

import flet as ft
from flet import CrossAxisAlignment

from src.ui_flet.common_component import BaseViewComponent
from src.ui_flet.route_data import AppRoute
from src.viewmodel.main_menu_viewmodel import MainMenuViewModel


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


@ft.component
def MainMenu():
    company_list_model = MainMenuViewModel()
    main_container = ft.Container()
    button_container = ft.Container()
    main_column = ft.Column(
        horizontal_alignment=CrossAxisAlignment.CENTER,
    )
    button_column = ft.Column(
        margin=200,
        horizontal_alignment=CrossAxisAlignment.CENTER,
    )

    button_column.controls = [
        ft.Text("Главное меню"),
        menu_button("ПЕРСОНАЛ", lambda: ft.context.page.navigate("/employees")),
        menu_button("ОТЧЕТЫ", lambda: ft.context.page.navigate("/reports")),
        menu_button("ПРОТОКОЛЫ", lambda: ft.context.page.navigate("/reports")),
    ]
    button_container.content = button_column
    main_column.controls = [
        CompanyDropdownList(company_list_model),
        button_container
    ]
    main_container.content = main_column
    return main_container


@ft.component
def CompanyDropdownList(company_list: MainMenuViewModel) -> ft.Control:
    company_list, _ = ft.use_state(company_list)

    def handle_change(event: ft.Event) -> None:
        selected_id = int(event.control.value)
        company_list.selected_company = next(
            (company for company in company_list.companies if company.id == selected_id),
            None,
        )

    dropdown_options = [
        ft.DropdownOption(key=str(company.id), text=company.name)
        for company in company_list.companies
    ]
    row = ft.Row(alignment=ft.MainAxisAlignment.END, run_alignment=ft.MainAxisAlignment.END)
    company_dropdown_list = ft.Dropdown(
        label="Выбери компанию",
        value=(str(company_list.selected_company.id) if company_list.selected_company else None),
        options=dropdown_options,
        on_select=handle_change,
        width=220,
    )
    row.controls.append(company_dropdown_list)
    return row


def menu_button(button_name: str, on_click_func: Callable[[], Any]) -> ft.Button:
    button = ft.Button(width=200, height=50)
    button.content = button_name
    button.on_click = on_click_func
    return button
