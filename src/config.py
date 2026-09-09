from __future__ import annotations

from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    database_url: str

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8"
    )


settings = Settings()

# 🔥 Автоматическое создание папки data, если её ещё нет
if settings.database_url.startswith("sqlite:///"):
    # Извлекаем путь к файлу (убираем "sqlite:///")
    rel_path = settings.database_url.replace("sqlite:///", "")
    abs_db_path = BASE_DIR / rel_path

    # Создаем родительскую папку (data/)
    abs_db_path.parent.mkdir(parents=True, exist_ok=True)

if __name__ == '__main__':
    print(BASE_DIR / ".env")