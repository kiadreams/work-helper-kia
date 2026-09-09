from __future__ import annotations

import flet as ft

from src.gui_flet.route_data import AppRoute


class BaseViewComponent(ft.View):
    def __init__(self, page: ft.Page, route: str) -> None:
        super().__init__()
        self.route = route
        self.app_page = page
        self.app_appbar = AppAppBar()
        self.app_bottom_appbar = AppBottomAppBar()
        self.appbar = self.app_appbar
        self.bottom_appbar = self.app_bottom_appbar


class AppBottomAppBar(ft.BottomAppBar):
    def __init__(self):
        super().__init__()
        self.home_button = self._create_home_button()
        self.settings_button = self._create_settings_button()
        self.exit_button = self._create_exit_button()
        self._setup_components()

    def _setup_components(self):
        self.content = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            controls=[self.home_button, self.settings_button, self.exit_button],
        )

    def _click_come_home_button(self) -> None:
        self.page.navigate(AppRoute.MAIN_MENU_VIEW)

    async def _exit_from_app(self) -> None:
        await self.page.window.close()

    def _create_exit_button(self) -> ft.IconButton:
        exit_button = ft.IconButton(ft.Icons.EXIT_TO_APP)
        exit_button.on_click = self._exit_from_app
        return exit_button

    def _create_home_button(self) -> ft.IconButton:
        home_button = ft.IconButton(ft.Icons.HOME)
        home_button.on_click = self._click_come_home_button
        return home_button

    @staticmethod
    def _create_settings_button() -> ft.IconButton:
        settings_button = ft.IconButton(ft.Icons.SETTINGS)
        return settings_button


class AppAppBar(ft.AppBar):
    def __init__(self):
        super().__init__()
        self._setup_components()

    def _setup_components(self):
        self.title = ft.WindowDragArea(
            content=ft.Container(
                content=ft.Text(
                    "РАБОЧИЙ ПОМОЩНИК КИА",
                    align=ft.Alignment.CENTER,
                    weight=ft.FontWeight.BOLD,
                ),
            ),
            expand=True,
        )
        self.bgcolor = ft.Colors.BLUE_100
        self.actions = self._add_action_button()
        self.automatically_imply_leading = False

    def did_mount(self) -> None:
        super().did_mount()
        if len(self.page.views) > 1:
            self.leading_width = 110
            self.leading = ft.Row(
                controls=[
                    self._create_arrow_back_button(),
                    self._create_minimize_button(),
                ],
                spacing=0,
            )
        else:
            self.leading = self._create_minimize_button()
        self.page.update()

    def _add_action_button(self) -> list[ft.Control]:
        return [self._create_maximize_button(), self._create_exit_button()]

    def _create_arrow_back_button(self) -> ft.IconButton:
        arrow_back_button = ft.IconButton(
            icon=ft.Icons.ARROW_BACK,
            tooltip="Назад",
            on_click=self._come_arrow_back,
        )
        return arrow_back_button

    def _create_maximize_button(self) -> ft.IconButton:
        icon_button_maximize = ft.IconButton(
            icon=ft.Icons.MAXIMIZE,
            tooltip="Развернуть",
            on_click=self._maximize_window,
        )
        return icon_button_maximize

    def _create_exit_button(self) -> ft.IconButton:
        icon_button_close = ft.IconButton(
            icon=ft.Icons.CLOSE,
            tooltip="Закрыть",
            on_click=self._exit_from_app,
        )
        return icon_button_close

    def _create_minimize_button(self) -> ft.IconButton:
        icon_button_minimize = ft.IconButton(
            icon=ft.Icons.MINIMIZE,
            tooltip="Свернуть",
            on_click=self._minimize_window,
        )
        return icon_button_minimize

    def _come_arrow_back(self, event: ft.Event) -> None:
        self.page.navigate(self.page.views[-2].route)

    def _minimize_window(self, event: ft.Event) -> None:
        self.page.window.minimized = True

    def _maximize_window(self, event: ft.Event) -> None:
        self.page.window.maximized = not self.page.window.maximized

    async def _exit_from_app(self, event: ft.Event) -> None:
        await self.page.window.close()
