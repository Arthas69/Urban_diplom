from typing import Annotated

from fastapi import Depends, APIRouter, Request
from fastapi.responses import HTMLResponse

from app.main import templates
from app.models import User
from app.routers.helpers import get_current_user


# Define an API router for users
router = APIRouter(prefix='/users', tags=['users'])


@router.get("/me")
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user.username


@router.get("/dashboard/", response_class=HTMLResponse)
async def dashboard(request: Request, current_user: Annotated[User, Depends(get_current_user)]):
    return templates.TemplateResponse("dashboard.html", {"request": request, "user": current_user})
