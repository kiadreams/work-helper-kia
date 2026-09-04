from __future__ import annotations

import flet as ft

from src.gui_flet.route_data import AppRoute
from src.gui_flet.view_components.common import BottomBar, TopAppBar


class EmployeeView(ft.View):
    def __init__(self) -> None:
        super().__init__()
        self.route = AppRoute.EMPLOYEE_VIEW.value
        self._setup_view()

    def _setup_view(self) -> None:
        self.appbar = self._add_top_app_bar()
        self.bottom_appbar = self._add_bottom_bar()

    @staticmethod
    def _add_bottom_bar() -> ft.BottomBar:
        bottom_bar = BottomBar()
        return bottom_bar

    @staticmethod
    def _add_top_app_bar() -> ft.AppBar:
        app_bar = TopAppBar()
        return app_bar