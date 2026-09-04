from __future__ import annotations

import flet as ft

from gui_flet.main_menu_view import MainMenuView
from gui_flet.route_data import AppRoute
from gui_flet.employee_view import EmployeeView
from gui_flet.report_view import ReportView
from gui_flet.protocol_view import ProtocolView


class MainWindow:
    VIEWS = {
        AppRoute.MAIN_MENU_VIEW.value: MainMenuView,
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
        self.page.views.clear()
        self.page.views.append(MainMenuView())
        self.page.window.visible = True

    def _route_change(self, event: ft.RouteChangeEvent | None = None) -> None:
        route = ""
        self.page.views.clear()
        self.page.views.append(MainMenuView())
        if event:
            route = event.route
        match route:
            case AppRoute.EMPLOYEE_VIEW.value:
                self.page.views.append(self.VIEWS[route]())
            case AppRoute.REPORT_VIEW.value:
                self.page.views.append(self.VIEWS[route]())
            case AppRoute.PROTOCOL_VIEW.value:
                self.page.views.append(self.VIEWS[route]())
        self.page.update()

    async def _go_back(self, event: ft.ViewPopEvent) -> None:
        if len(self.page.views) > 1:
            penultimate_view = self.page.views[-2]
            await self.page.push_route(penultimate_view.route)

    def _set_window_config(self) -> None:
        self.page.window.alignment = ft.Alignment.CENTER
        self.page.title = "Рабочий помощник КИА"
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.vertical_alignment = ft.CrossAxisAlignment.CENTER
        self.page.window.title_bar_hidden = True
