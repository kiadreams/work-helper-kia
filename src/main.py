# import flet as ft
#
# from src.database.db_manager import DatabaseManager
# from src.ui_flet.main_window import MainWindow
# from src.settings import settings
# from src.ui_flet.main_menu_view import CompanyNameArea, CompanyDropdownList
# from viewmodel.company_viewmodel import CompanyListViewModel
#
# app_db = DatabaseManager(settings)
#
#
# def setup_window(page: ft.Page) -> None:
#     page.window.width = 1024
#     page.window.height = 800
#     page.title = "Рабочий помощник КИА"
#     page.window.title_bar_hidden = True
#     page.run_task(page.window.center)
#     if page.web:
#         page.run_task(ft.BrowserContextMenu().disable)
#
#
# # def main_entrypoint(page: ft.Page) -> None:
# #     # MainWindow(page, app_db)
# #     page.render(CompanyNameArea)
#
#
# def main_entry_component(page: ft.Page) -> None:
#     companies = CompanyListViewModel()
#     company_list = CompanyDropdownList
#     page.window.visible = True
#     page.render(company_list, companies)
#
#
# ft.run(
#     before_main=setup_window,
#     # main=main_entrypoint,
#     main=main_entry_component,
#     view=ft.AppView.FLET_APP_HIDDEN,
# )
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
#
#
#
# Проверка создания шапки протокола:
from src.infrastructure.protocol_templates.template_render import (
    create_headline_template,
)
from pathlib import Path

template_file_path = (
    Path(__file__).parent / "infrastructure/protocol_templates/protocol_headline.docx"
)
target_file_path = Path(__file__).parent.parent / "result.docx"
create_headline_template(template_file_path, target_file_path)
