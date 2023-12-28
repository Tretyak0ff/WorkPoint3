from fastapi import FastAPI
from src.config import settings
from src.config.factory import create_app


app: FastAPI = create_app(debug=settings.debug)
