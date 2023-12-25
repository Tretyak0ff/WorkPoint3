import pathlib
from environs import Env
from loguru import logger
from pydantic_settings import BaseSettings


BASE_DIR = pathlib.Path(__file__).parent.parent
env = Env()
Env.read_env(BASE_DIR / '.env')


class Settings(BaseSettings):
    debug: bool = env('DEBUG', defaut=False)
    title: str = env('NAME_APP', defaut=None)


setting: Settings = Settings()
logger.debug((setting, BASE_DIR))
