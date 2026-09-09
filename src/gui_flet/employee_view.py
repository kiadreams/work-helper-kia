from __future__ import annotations

import flet as ft

from gui_flet.ui_protocols.entities import EmployeeUIEntity
from src.gui_flet.common_component import BaseViewComponent


class EmployeeView(BaseViewComponent):
    def __init__(self, page: ft.Page, route: str) -> None:
        super().__init__(page, route)
        self.padding = 33
        self.spacing = 50
        self.file_picker = ft.FilePicker()
        self.app_page.services.append(self.file_picker)
        self.selected_employee_item = EmployeeDataItem()
        self.employee_list = EmployeeTable()
        self._setting_area(self.selected_employee_item)

        self.controls.append(self.selected_employee_item)
        self.controls.append(self.employee_list)
        for i in range(30):
            employee_item = EmployeeDataItem()
            employee_photo = EmployeePhoto(self.file_picker, photo_size=77)
            employee_item.add_data(employee_photo, i + 1)
            self.employee_list.add_item(employee_item)
            self.app_page.update()

    def select_employee(self) -> None:
        pass

    @staticmethod
    def _setting_area(area: ft.Container) -> None:
        area.border = ft.Border.all(width=5, color=ft.Colors.BLACK)
        area.border_radius = 10
        area.height = 100


class EmployeeTable(ft.Container):
    def __init__(self) -> None:
        super().__init__()
        self.padding = 20
        self.border = ft.Border.all(width=2, color=ft.Colors.GREY_800)
        self.border_radius = 10
        self.expand = True
        self.element_list = ft.ListView()
        self.element_list.scroll = ft.Scrollbar(
            thumb_visibility=False,
            thickness=15,
            radius=5,
        )
        self.content = self.element_list

    def add_item(self, employee_item: EmployeeDataItem) -> None:
        self.element_list.controls.append(employee_item)


class EmployeeDataItem(ft.Container):
    def __init__(self) -> None:
        super().__init__()
        self.border = ft.Border.all(width=2, color=ft.Colors.BLUE_400)
        self.employee_area = ft.Row(expand=True, wrap=False)
        self.content = self.employee_area

    def add_data(self, employee_data: ft.Control, number: int = 0) -> None:
        if number:
            number_badge = self._create_list_number(number)
            self.employee_area.controls.append(number_badge)
        self.employee_area.controls.append(employee_data)

    @staticmethod
    def _create_list_number(number: int) -> ft.CircleAvatar:
        number_badge = ft.CircleAvatar(
            content=ft.Text(value=str(number), color=ft.Colors.WHITE, size=12),
            bgcolor=ft.Colors.BLUE_400,
            radius=14,
        )
        return number_badge


class EmployeePhoto(ft.Container):
    def __init__(self, file_picker: ft.FilePicker, photo_size: int) -> None:
        super().__init__()
        self._file_picker = file_picker
        self.last_photo_path = ""
        self.photo_size = photo_size
        self.employee_icon = self._create_icon()
        self.employee_photo = ft.Image(
            src=self.last_photo_path,
            width=photo_size,
            height=photo_size,
            fit=ft.BoxFit.COVER,
            border_radius=photo_size // 10,
            visible=False,
        )
        self.photo_area_stack = ft.Stack(
            width=photo_size,
            height=photo_size,
        )
        self.photo_area_stack.controls.append(self.employee_photo)
        self.photo_area_stack.controls.append(self.employee_icon)

        # self.context_menu = ft.ContextMenu(self.photo_area_stack)
        self.context_menu = self._create_context_menu(self.photo_area_stack)
        self.mouse_cursor = ft.MouseCursor.CLICK
        self.content = self.context_menu

    def _create_context_menu(self, element: ft.Control) -> ft.ContextMenu:
        menu = ft.ContextMenu(
            content=element,
            primary_trigger=ft.ContextMenuTrigger.DOWN,
        )
        menu.primary_items.append(self._add_photo_menu_item())
        return menu

    async def _select_photo(self, event: ft.Event) -> None:
        file_list_result = await self._file_picker.pick_files(
            allow_multiple=False,
            allowed_extensions=["jpg", "jpeg", "png"],
        )
        if file_list_result:
            first_file = file_list_result[0]
            if first_file.path:
                self.last_photo_path = first_file.path
                self.employee_photo.src = first_file.path
                self.employee_photo.visible = True
                self.employee_icon.visible = False
                if len(self.context_menu.primary_items) < 2:
                    self.context_menu.primary_items.append(
                        self._delete_photo_menu_item()
                    )

    def _delete_photo(self, event: ft.Event) -> None:
        self.last_photo_path = ""
        self.employee_icon.visible = True
        self.employee_photo.visible = False
        if len(self.context_menu.primary_items) > 1:
            self.context_menu.primary_items = [self._add_photo_menu_item()]

    def _create_icon(self) -> ft.Container:
        icon_container = ft.Container(
            width=self.photo_size,
            height=self.photo_size,
            alignment=ft.Alignment.CENTER,
            border=ft.Border.all(width=2, color=ft.Colors.GREY_200),
            border_radius=self.photo_size // 10,
            tooltip="Выбрать фото",
        )
        icon_container.content = ft.Icon(icon=ft.Icons.PERSON_ADD)
        return icon_container

    def _add_photo_menu_item(self):
        item_menu = ft.PopupMenuItem(
            content="Выбрать фотографию",
            icon=ft.Icons.ACCOUNT_BOX,
            on_click=self._select_photo,
        )
        return item_menu

    def _delete_photo_menu_item(self):
        item_menu = ft.PopupMenuItem(
            content="Удалить фотографию",
            icon=ft.Icons.DELETE,
            on_click=self._delete_photo,
        )
        return item_menu


class EmployDataBox(ft.Container):
    def __init__(self, employee: EmployeeUIEntity):
        super().__init__()
        self.first_row = ft.Row()
        self.second_row = ft.Row()
