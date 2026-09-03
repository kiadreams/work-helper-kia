from __future__ import annotations

import flet as ft

from gui_flet.view_components.common import BottomBar, TopAppBar
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
        self.page.on_route_change = self._route_change
        self.page.on_view_pop = self._go_back

    def _setup_view(self) -> None:
        self._set_window_config()
        self.page.appbar = self._add_top_app_bar()
        self._create_main_menu_button()
        self.page.bottom_appbar = self._add_bottom_bar()
        self.page.window.visible = True

    def _route_change(self, event: ft.RouteChangeEvent | None = None) -> None:
        route = AppRoute.MAIN_WINDOW
        if event:
            route = event.route
        view_builder = self._VIEWS.get(route, self)
        existed_view = self._find_existed_view(route)
        if existed_view:
            self.page.views.remove(existed_view)
            self.page.views.append(existed_view)
        else:
            self.page.views.append(view_builder())
        self.page.update()

    def _go_back(self) -> None:
        print("вызвали")
        self._route_change()

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

    def _set_window_config(self) -> None:
        self.page.window.alignment = ft.Alignment.CENTER
        self.page.title = "Рабочий помощник КИА"
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.vertical_alignment = ft.CrossAxisAlignment.CENTER
        self.page.window.title_bar_hidden = True

    def _create_main_menu_button(self) -> None:
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

    @staticmethod
    def _add_bottom_bar() -> ft.BottomBar:
        bottom_bar = BottomBar()
        bottom_bar.home_button.visible = False
        return bottom_bar

    @staticmethod
    def _add_top_app_bar() -> ft.AppBar:
        app_bar = TopAppBar()
        return app_bar