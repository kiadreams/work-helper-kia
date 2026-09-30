import flet as ft

from src.ui_flet.common_component import BaseViewComponent


class ProtocolView(BaseViewComponent):
    def __init__(self, page: ft.Page, route: str) -> None:
        super().__init__(page, route)


@ft.component
def Protocols():
    button_back = ft.Button("Back", on_click=lambda: ft.context.page.navigate('/'))
    container = ft.Container(
        content=ft.Column(
            controls=[ft.Text("Protocols"), button_back]
        )
    )
    return container
