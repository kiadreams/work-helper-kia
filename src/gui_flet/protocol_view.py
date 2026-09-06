from __future__ import annotations

import flet as ft

from src.gui_flet.common_component import BaseViewComponent


class ProtocolView(BaseViewComponent):
    def __init__(self, page: ft.Page, route: str) -> None:
        super().__init__(page, route)
