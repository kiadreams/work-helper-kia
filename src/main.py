# import flet as ft
#
# from database.db_manager import DatabaseManager
# from settings import settings
# from ui_flet.employee_view import Employees
# from ui_flet.main_menu_view import MainMenu
# from ui_flet.protocol_view import Protocols
# from ui_flet.report_view import Reports
#
# app_db = DatabaseManager(settings)
#
#
# def setup_window(page: ft.Page) -> None:
#     page.window.width = 1024
#     page.window.height = 800
#     page.title = "Рабочий помощник КИА"
#     # page.window.title_bar_hidden = True
#     page.run_task(page.window.center)
#     if page.web:
#         page.run_task(ft.BrowserContextMenu().disable)
#
#
# @ft.component
# def App() -> ft.SafeArea:
#     router = ft.Router(
#         [
#             ft.Route(index=True, component=MainMenu),
#             ft.Route(path="/employees", component=Employees, children=[]),
#             ft.Route(path="/reports", component=Reports, children=[]),
#             ft.Route(path="/reports", component=Protocols, children=[]),
#         ]
#     )
#     return ft.SafeArea(content=router)
#
#
# def main(page: ft.Page) -> None:
#     page.window.visible = True
#     page.render(App)
#
#
# ft.run(before_main=setup_window, main=main, view=ft.AppView.FLET_APP_HIDDEN)

#
#
#
# # Проверка работы БАЗЫ ДАННЫХ В АСИНХРОННОМ РЕЖИМЕ
# import asyncio
#
# from src.database.db_manager import DatabaseManager
# from src.repository.company_repo import CompanyRepository
# from src.settings import settings
# # from src.assets.db_test_data.db_table_data import test_employees, test_companies
#
# app_db = DatabaseManager(settings)
# repo = CompanyRepository(app_db)
#
#
# async def main() -> None:
#     # await repo.add_employees(test_employees)
#     # await repo.add_companies(test_companies)
#     all_employees = await repo.get_all_employees()
#     all_companies = await repo.get_all_companies()
#     for employee in all_employees:
#         print(employee)
#     print()
#     for company in all_companies:
#         print(company)
#
#
# asyncio.run(main())

from infrastructure.protocol_templates.headline_section import HeadlineSection

class ExampleData:
    def __init__(self):
        self._title = "Загловок"

    @property
    def title(self) -> str:
        return self._title


headline = HeadlineSection(ExampleData())
headline.build()
headline.save_to("example.docx")