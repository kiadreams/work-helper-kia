from __future__ import annotations

import flet as ft

from src.gui_flet.employee_view import EmployeeView
from src.gui_flet.main_menu_view import MainMenuView
from src.gui_flet.protocol_view import ProtocolView
from src.gui_flet.report_view import ReportView
from src.gui_flet.route_data import AppRoute


class MainWindow:
    VIEWS = {
        AppRoute.MAIN_MENU_VIEW.value: MainMenuView,
        AppRoute.EMPLOYEE_VIEW.value: EmployeeView,
        AppRoute.REPORT_VIEW.value: ReportView,
        AppRoute.PROTOCOL_VIEW.value: ProtocolView,
    }

    def __init__(self, page: ft.Page) -> None:
        self.page = page
        self.page.on_route_change = self._route_change
        self.page.on_view_pop = self._go_back
        self.page.views.clear()
        self.page.views.append(MainMenuView(page, AppRoute.MAIN_MENU_VIEW.value))
        self.page.window.visible = True

    def _route_change(self, event: ft.RouteChangeEvent | None = None) -> None:
        route = ""
        self.page.views.clear()
        self.page.views.append(MainMenuView(self.page, AppRoute.MAIN_MENU_VIEW.value))
        if event:
            route = event.route
        match route:
            case AppRoute.EMPLOYEE_VIEW.value:
                self.page.views.append(
                    self.VIEWS[route](self.page, AppRoute.EMPLOYEE_VIEW.value)
                )
            case AppRoute.REPORT_VIEW.value:
                self.page.views.append(
                    self.VIEWS[route](self.page, AppRoute.REPORT_VIEW.value)
                )
            case AppRoute.PROTOCOL_VIEW.value:
                self.page.views.append(
                    self.VIEWS[route](self.page, AppRoute.PROTOCOL_VIEW.value)
                )
        self.page.update()

    async def _go_back(self, event: ft.ViewPopEvent) -> None:
        if len(self.page.views) > 1:
            penultimate_view = self.page.views[-2]
            await self.page.push_route(penultimate_view.route)
