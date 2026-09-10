from __future__ import annotations

from sqlmodel import create_engine

from src.settings import settings


class DatabaseManager:
    def __init__(self) -> None:
        self.db_file_name: str = settings.db_file_name
        self.database_url: str = settings.database_url
        self.project_dir = settings.project_dir
        self.db_engine = create_engine(self.database_url, echo=False)

    def create_database_dir(self) -> None:
        if self.database_url.startswith("sqlite:///"):
            rel_path = self.database_url.replace("sqlite:///", "")
            abs_db_path = self.project_dir / rel_path
            abs_db_path.parent.mkdir(parents=True, exist_ok=True)
