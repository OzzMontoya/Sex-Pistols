from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Teknocity API"
    database_url: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/teknocity"
    city: str = "Guadalajara"
    websocket_channel: str = "traffic-updates"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


@lru_cache
def get_settings() -> Settings:
    return Settings()
