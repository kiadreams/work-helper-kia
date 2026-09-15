from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import event
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession

if TYPE_CHECKING:
    from src.settings import Settings
    from sqlalchemy.ext.asyncio import AsyncEngine
    from pathlib import Path


class DatabaseManager:
    def __init__(self, app_settings: Settings) -> None:
        self.app_settings = app_settings
        self.create_database_dir(app_settings.database_url, app_settings.project_dir)
        self.db_engine = self.create_db_engine(app_settings.database_url)
        self.connection = self.create_sessionmaker()

    @staticmethod
    def create_db_engine(db_url: str) -> AsyncEngine:
        async_engine = create_async_engine(
            db_url,
            echo=True,
            connect_args={
                # Важно для Flet: разрешаем разным асинхронным задачам
                # использовать один и тот же движок
                "check_same_thread": False,
                "timeout": 10,  # Ждем до 10 сек, если база занята
            },
        )

        @event.listens_for(async_engine.sync_engine, "connect")
        def set_sqlite_pragma(dbapi_connection, connection_record):
            # Переключаем SQLite в режим WAL на уровне драйвера
            cursor = dbapi_connection.cursor()
            cursor.execute("PRAGMA journal_mode=WAL")
            cursor.execute("PRAGMA synchronous=NORMAL")
            cursor.close()

        return async_engine

    @staticmethod
    def create_database_dir(db_url: str, project_dir_path: Path) -> None:
        if db_url.startswith("sqlite+aiosqlite:///"):
            rel_path = db_url.replace("sqlite+aiosqlite:///", "")
            abs_db_path = project_dir_path.parent / rel_path
            abs_db_path.parent.mkdir(parents=True, exist_ok=True)

    def create_sessionmaker(self) -> async_sessionmaker[AsyncSession]:
        db_sessionmaker = async_sessionmaker(
            bind=self.db_engine,
            class_=AsyncSession,
            expire_on_commit=False,
        )
        return db_sessionmaker
