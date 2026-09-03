from __future__ import annotations

import flet as ft
from flet.controls.material import switch

from .start_view import StartView

# Импортируем функции наших страниц из папки views


APP_VIEWS = {
    "/start_view": StartView,
    "/employees": "22222",
    "/reports": "33333",
    "/protocols": "44444",
}


class MainWindow:

    def __init__(self, page: ft.Page):
        self.page = page
        self._setup_view()

    def _setup_view(self):
        self.page.title = "Рабочий помощник КИА"
        self.page.views.append(StartView(self.page))


# def main_window(page: ft.Page):
#     page.title = "Рабочий помощник КИА"
#
#     view_area = ft.Container()
#
#     def route_change(e: ft.RouteChangeEvent):
#         # Берем нужную страницу из словаря по текущему маршруту page.route
#         # Если маршрут не найден, по умолчанию откроется главная "/"
#         view_builder = APP_VIEWS.get(e.route, start_view)
#
#         # Вызываем функцию, передавая туда page, и добавляем результат в стек
#         page.views.append(view_builder(page))
#         page.update()
#
#     def view_pop(e: ft.ViewPopEvent):
#         page.views.pop()
#         top_view = page.views[-1]
#         page.go(top_view.route)
#
#     page.on_route_change = route_change
#     page.on_view_pop = view_pop
#
#     # Запускаем стартовый маршрут
#     page.go(page.route)


if __name__ == "__main__":
    ft.app(target=main_window)
