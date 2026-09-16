import flet as ft

from src.ui_flet.common_component import BaseViewComponent


class ReportView(BaseViewComponent):
    def __init__(self, page: ft.Page, route: str) -> None:
        super().__init__(page, route)
