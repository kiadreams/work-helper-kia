from __future__ import annotations

from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    db_file_name: str
    database_url: str

    model_config = SettingsConfigDict(
        env_file=Path(__file__).resolve().parent.parent / ".env",
        env_file_encoding="utf-8",
    )

    @property
    def project_dir(self) -> Path:
        return Path(__file__).resolve().parent


settings = Settings()  # type: ignore[call-arg]

if __name__ == "__main__":
    print(settings.project_dir)
    print(settings.database_url)
    print(settings.db_file_name)
