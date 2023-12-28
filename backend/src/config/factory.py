from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from loguru import logger

__all__ = ("create_app",)


@asynccontextmanager
async def connection_database(app: FastAPI):
    logger.debug("Он стартапп")
    yield
    logger.debug("Конец")


def create_app(**kwargs,) -> FastAPI:
    app = FastAPI(lifespan=connection_database)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:8080"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],)

    @app.get("/")
    def main_page() -> dict:
        return {
            "message": "this is the root directory"
        }
    return app
