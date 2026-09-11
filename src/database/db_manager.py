from __future__ import annotations

from typing import TYPE_CHECKING

from sqlmodel import create_engine, Session

if TYPE_CHECKING:
    from src.settings import Settings


class DatabaseManager:
    def __init__(self, settings: Settings) -> None:
        self.database_url: str = settings.database_url
        self.project_dir = settings.project_dir
        self.db_engine = create_engine(self.database_url, echo=False)
        self.create_database_dir()

    def create_database_dir(self) -> None:
        if self.database_url.startswith("sqlite:///"):
            rel_path = self.database_url.replace("sqlite:///", "")
            abs_db_path = self.project_dir.parent / rel_path
            abs_db_path.parent.mkdir(parents=True, exist_ok=True)

    def get_session(self) -> Session:
        return Session(bind=self.db_engine)
