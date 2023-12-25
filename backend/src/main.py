from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def create():

    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:8080"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/")
    def home() -> dict:
        return {
            "message": "this is the root directory"
        }

    return app
