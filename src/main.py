from __future__ import annotations

import flet as ft

from src.database.db_manager import DatabaseManager
from src.gui_flet.main_window import MainWindow
from src.settings import settings

app_db = DatabaseManager(settings)


def setup_window(page: ft.Page) -> None:
    page.window.width = 1024
    page.window.height = 800
    page.title = "Рабочий помощник КИА"
    page.window.title_bar_hidden = True
    page.run_task(page.window.center)
    if page.web:
        page.run_task(ft.BrowserContextMenu().disable)


ft.run(
    before_main=setup_window,
    main=MainWindow,
    view=ft.AppView.FLET_APP_HIDDEN,
)

# # Проверка работы БАЗЫ ДАННЫХ В АСИНХРОННОМ РЕЖИМЕ
# import asyncio
#
# from sqlmodel import select
#
# from src.domain.models import Employee
# from src.database.db_manager import DatabaseManager
# from src.settings import settings
#
# app_db = DatabaseManager(settings)
# app_sessionmaker = app_db.connection
#
#
# async def insert_employee() -> None:
#     async with app_sessionmaker() as conn:
#         employee = Employee(name="Igor", last_name="Igor")
#         conn.add(employee)
#         await conn.commit()
#
#
# async def show_all_employees() -> None:
#     async with app_sessionmaker() as conn:
#         stmt = select(Employee).order_by(Employee.last_name)
#         results = await conn.exec(stmt)
#         employees = results.all()
#         for employee in employees:
#             print(employee.name)
#
#
# async def main() -> None:
#     await insert_employee()
#     await show_all_employees()
#
#
# asyncio.run(main())
