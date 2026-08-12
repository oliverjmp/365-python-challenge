from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    app_env: str = Field(default="development", validation_alias="APP_ENV")
    database_url: str = Field(..., validation_alias="DATABASE_URL")
    api_secret_key: str = Field(..., validation_alias="API_SECRET_KEY")
    max_connections: int = Field(default=10, validation_alias="MAX_CONNECTIONS")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"