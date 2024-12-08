from pathlib import Path

from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from fastapi.templating import Jinja2Templates


app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent

templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates')))
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

from .routers import routers
for router in routers:
    app.include_router(router)
