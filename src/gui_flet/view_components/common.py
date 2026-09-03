from __future__ import annotations

import flet as ft

from gui_flet.route_data import AppRoute


class BottomBar(ft.BottomAppBar):

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
        self.page.navigate(AppRoute.MAIN_WINDOW)

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


class TopAppBar(ft.AppBar):
    def __init__(self):
        super().__init__()
        self._setup_components()

    def _setup_components(self):
        self.title = ft.Text("Рабочий помощник КИА")

# def main(page: ft.Page):
#     page.title = "AppBar Example"
#
#     def handle_checked_item_click(e: ft.Event[ft.PopupMenuItem]):
#         e.control.checked = not e.control.checked
#
#     page.appbar = ft.AppBar(
#         leading=ft.Icon(ft.Icons.PALETTE),
#         leading_width=40,
#         title=ft.Text("AppBar Example"),
#         center_title=False,
#         bgcolor=ft.Colors.BLUE_GREY_400,
#         actions=[
#             ft.IconButton(ft.Icons.WB_SUNNY_OUTLINED),
#             ft.IconButton(ft.Icons.FILTER_3),
#             ft.PopupMenuButton(
#                 key="popup",
#                 items=[
#                     ft.PopupMenuItem(content="Item 1"),
#                     ft.PopupMenuItem(),  # divider
#                     ft.PopupMenuItem(
#                         content="Checked item",
#                         checked=False,
#                         on_click=handle_checked_item_click,
#                     ),
#                 ],
#             ),
#         ],
#     )
#     page.add(ft.SafeArea(content=ft.Column(controls=[ft.Text("Body!")])))