from __future__ import annotations

import flet as ft

# from src.gui_flet.common_component import BaseViewComponent


# class EmployeeView(BaseViewComponent):
#     def __init__(self, page: ft.Page, route: str) -> None:
#         super().__init__(page, route)
        # self.file_picker = ft.FilePicker()
        # self.app_page.services.append(self.file_picker)
        # self.controls.append(EmployeeTable(self.file_picker))
        # self.controls.append(EmployeePhoto(self.file_picker, 70))
        # self.controls.append(EmployeeDataArea(self.file_picker))


# class EmployeeTable(ft.ListView):
#     def __init__(self, file_picker: ft.FilePicker) -> None:
#         super().__init__()
#         self._file_picker = file_picker
#         self.expand = True
#         self.scroll = ft.Scrollbar(
#             thumb_visibility=False,
#             thickness=15,
#             radius=5,
#         )
#         # self.data_area = EmployeeDataArea(file_picker, photo_size=70)
#         for _ in range(20):
#             data_area = EmployeeDataArea(file_picker, photo_size=70)
#             self.controls.append(data_area)
#
#
#
# class EmployeeDataArea(ft.Container):
#     def __init__(self, file_picker: ft.FilePicker, photo_size: int = 50) -> None:
#         super().__init__()
#         self.photo_size = photo_size
#         self._file_picker = file_picker
#         self.border = ft.Border.all(width=2, color=ft.Colors.BLUE_400)
#         self.person_area = ft.Row(expand=True, wrap=False)
#         self.person_photo = EmployeePhoto(file_picker, photo_size)
#         self.person_area.controls.append(self.person_photo)
#         self.person_area.controls.append(ft.Text("Александр"))
#         self.content = self.person_area
#
#
# class EmployeePhoto(ft.GestureDetector):
#
#     def __init__(self, file_picker: ft.FilePicker, photo_size: int) -> None:
#         super().__init__()
#         self._file_picker = file_picker
#         self.photo_size = photo_size
#         self.selected_photo_path = ""
#         self.person_icon = self._create_icon()
#         self.person_photo = ft.Image(
#             src="",
#             width=photo_size,
#             height=photo_size,
#             fit=ft.BoxFit.COVER,
#             border_radius=photo_size // 10,
#             visible=False
#         )
#         self.photo_area_stack = ft.Stack(
#             width=photo_size,
#             height=photo_size,
#         )
#         self.photo_area_stack.controls.append(self.person_photo)
#         self.photo_area_stack.controls.append(self.person_icon)
#
#         self.mouse_cursor = ft.MouseCursor.CLICK
#         self.on_tap = self._choose_person_photo
#         self.content = self.photo_area_stack
#
#     async def _choose_person_photo(self, event: ft.TapEvent) -> None:
#         file_list_result = await self._file_picker.pick_files(
#             allow_multiple=False,
#             allowed_extensions=["jpg", "jpeg", "png"],
#         )
#         if file_list_result:
#             first_file = file_list_result[0]
#             if first_file.path:
#                 print(first_file.path)
#                 self.selected_photo_path = first_file.path
#                 self.selected_photo_path = first_file.path
#                 self.person_photo.src = first_file.path
#                 self.person_photo.visible = True
#                 self.person_icon.visible = False
#
#     def _create_icon(self) -> ft.Container:
#         icon_container = ft.Container(
#             width=self.photo_size,
#             height=self.photo_size,
#             alignment=ft.Alignment.CENTER,
#             border=ft.Border.all(width=2, color=ft.Colors.GREY_200),
#             border_radius=self.photo_size // 10,
#         )
#         icon_container.content = ft.Icon(icon=ft.Icons.PERSON_ADD)
#         return icon_container
