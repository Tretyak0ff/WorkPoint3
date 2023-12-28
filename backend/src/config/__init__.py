from pathlib import Path
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


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

    public_api: PublicApiSettings = PublicApiSettings()


ROOT_PATH = Path(__file__).parent.parent

settings = Settings(
    root_dir=ROOT_PATH,
    src_dir=ROOT_PATH / "",
)
