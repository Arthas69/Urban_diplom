from pathlib import Path

from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from fastapi.templating import Jinja2Templates


# Create main app and resolve path to the root directory
app = FastAPI()
BASE_DIR = Path(__file__).resolve().parent

# Define the path to the template files
templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates')))

# Define the OAuth2 Bearer token scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


# Include the routers from the different modules and enable them for our application
from .routers import routers
for router in routers:
    app.include_router(router)
