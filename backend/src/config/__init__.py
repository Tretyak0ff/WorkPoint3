from pathlib import Path
from typing import Literal
from loguru import logger
from pydantic import ConfigDict, BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
# BaseConfig, BaseModel, BaseSettings


# class PublicApiSettings(BaseModel):
#     """Configure public API settings."""

#     name: str = "Backend"
#     urls: APIUrlsSettings = APIUrlsSettings()


# # Database Settings
# class DatabaseSettings(BaseModel):
#     name: str = "db.sqlite3"

#     @property
#     def url(self) -> str:
#         return f"sqlite+aiosqlite:///./{self.name}"


# class KafkaSettings(BaseModel):
#     bootstrap_servers: str = "localhost:9092"


# # Logging Settings
# class LoggingSettings(BaseModel):
#     """Configure the logging engine."""

#     # The time field can be formatted using more human-friendly tokens.
#     # These constitute a subset of the one used by the Pendulum library
#     # https://pendulum.eustace.io/docs/#tokens
#     format: str = "{time:YYYY-MM-DD HH:mm:ss} | {level: <5} | {message}"

#     # The .log filename
#     file: str = "backend"

#     # The .log file Rotation
#     rotation: str = "1MB"

#     # The type of compression
#     compression: str = "zip"


# class AccessTokenSettings(BaseModel):
#     secret_key: str = "invaliad"
#     ttl: int = 100  # seconds


# class RefreshTokenSettings(BaseModel):
#     secret_key: str = "invaliad"
#     ttl: int = 100  # seconds


# class AuthenticationSettings(BaseModel):
#     access_token: AccessTokenSettings = AccessTokenSettings()
#     refresh_token: RefreshTokenSettings = RefreshTokenSettings()
#     algorithm: str = "HS256"
#     scheme: str = "Bearer"


# # Settings are powered by pydantic
# # https://pydantic-docs.helpmanual.io/usage/settings/
# class Settings(BaseSettings):
#     debug: bool = True

#     # Project file system
#     root_dir: Path
#     src_dir: Path

#     # Infrastructure settings
#     database: DatabaseSettings = DatabaseSettings()

#     # Application configuration
#     public_api: PublicApiSettings = PublicApiSettings()
#     logging: LoggingSettings = LoggingSettings()
#     authentication: AuthenticationSettings = AuthenticationSettings()

#     class Config(BaseConfig):
#         env_nested_delimiter: str = "__"
#         env_file: str = ".env"

class APIUrlsSettings(BaseModel):
    docs_url: str = "/docs"
    redoc_url: str = "/redoc"


class PublicApiSettings(BaseModel):
    urls: APIUrlsSettings = APIUrlsSettings()


class Settings(BaseSettings):
    root_dir: Path
    src_dir: Path

    backend_name: str
    backend_host: str
    backend_port: int
    backend_debug: str

    db_name: str
    db_host: str
    db_port: int
    db_user: str
    db_password: str

    pg_admin_port: int
    pg_admin_email: str
    pg_admin_password: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_nested_delimiter="__",
    )


ROOT_PATH = Path(__file__).parent.parent

settings = Settings(
    root_dir=ROOT_PATH,
    src_dir=ROOT_PATH / "",
)
logger.debug(settings)
