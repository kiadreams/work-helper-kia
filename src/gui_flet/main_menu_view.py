# from __future__ import annotations
#
# import flet as ft
# from gui_flet.route_data import AppRoute
#
#
# class MainMenuView(ft.View):
#     def __init__(self, page: ft.Page) -> None:
#         super().__init__()
#         self.app_page = page
#         self.route = AppRoute.MAIN_MENU_VIEW
#         self._setup_view()
#
#     def _setup_view(self) -> None:
#         self.controls = [
#             ft.Container(
#                 content=ft.Column([
#                     ft.Button("Персонал", on_click=self._click_employee_button),
#                     ft.Button("Отчеты", on_click=self._click_report_button),
#                     ft.Button("Протоколы", on_click=self._click_protocol_button),
#                 ])
#             )
#         ]
#
#     def _click_employee_button(self, event: ft.Event) -> None:
#         self.page.navigate(AppRoute.EMPLOYEE_VIEW)
#
#     def _click_report_button(self) -> None:
#         self.page.navigate(AppRoute.REPORT_VIEW)
#
#     def _click_protocol_button(self) -> None:
#         self.page.navigate(AppRoute.PROTOCOL_VIEW)