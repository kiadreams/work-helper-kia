from __future__ import annotations
from typing import AsyncIterator

from dishka import Provider, Scope, provide, AsyncContainer, from_context
import flet as ft
from sqlmodel.ext.asyncio.session import AsyncSession

from src.gui_flet.main_menu_view import MainMenuView
from src.database.db_manager import DatabaseManager
from src.gui_flet.main_window import MainWindow
from src.settings import Settings


class AppProvider(Provider):
    scope = Scope.APP

    @provide
    def get_settings(self) -> Settings:
        return Settings()  # type: ignore[call-arg]

    @provide
    def get_db_manager(self, settings: Settings) -> DatabaseManager:
        return DatabaseManager(settings)


class SessionProvider(Provider):
    scope = Scope.SESSION
    page = from_context(provides=ft.Page)

    @provide
    def get_main_window(
            self, page: ft.Page, session_container: AsyncContainer
    ) -> MainWindow:
        return MainWindow(page=page, session_container=session_container)

    @provide
    def get_main_menu_view(
            self, page: ft.Page, session_container: AsyncContainer
    ) -> MainMenuView:
        return MainMenuView(page=page)


class RequestProvider(Provider):
    scope = Scope.REQUEST

    @provide
    async def get_session(self, db: DatabaseManager) -> AsyncIterator[AsyncSession]:
        async with db.connection() as conn:
            yield conn
