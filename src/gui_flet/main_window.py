from __future__ import annotations

import flet as ft
from flet.controls import border_radius

from src.gui_flet.route_data import AppRoute
from src.gui_flet.employee_view import EmployeeView
from src.gui_flet.report_view import ReportView
from src.gui_flet.protocol_view import ProtocolView




class MainWindow:
    _VIEWS = {
        AppRoute.EMPLOYEE_VIEW.value: EmployeeView,
        AppRoute.REPORT_VIEW.value: ReportView,
        AppRoute.PROTOCOL_VIEW.value: ProtocolView,
    }


    def __init__(self, page: ft.Page) -> None:
        self.page = page
        self._setup_view()
        self.page.on_route_change = self.route_change

    def _setup_view(self) -> None:
        self.page.title = "Рабочий помощник КИА"
        self.page.controls = [
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
        print(len(self.page.views))
        # self.page.views.append(self.VIEWS.get(AppRoute.MAIN_MENU_VIEW)())
        print(len(self.page.views))

    def route_change(self, event: ft.RouteChangeEvent) -> None:
        print("вызов маршрутизации")
        # Берем нужную страницу из словаря по текущему маршруту page.route
        # Если маршрут не найден, по умолчанию откроется главная "/"
        view_builder = self._VIEWS.get(event.route, self)
        existed_view = self._find_existed_view(event.route)
        if existed_view:
            self.page.views.remove(existed_view)
            self.page.views.append(existed_view)
        else:
            self.page.views.append(view_builder())
        self.page.update()
        print(len(self.page.views))

    def _find_existed_view(self, rote: str) -> ft.View | None:
        existed_views = None
        for view in self.page.views:
            if view.route == rote:
                existed_views = view
        return existed_views

    def _click_employee_button(self) -> None:
        self.page.navigate(AppRoute.EMPLOYEE_VIEW)

    def _click_report_button(self) -> None:
        self.page.navigate(AppRoute.REPORT_VIEW)

    def _click_protocol_button(self) -> None:
        self.page.navigate(AppRoute.PROTOCOL_VIEW)
