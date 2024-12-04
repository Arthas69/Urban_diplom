from typing import Annotated

from fastapi import Depends, APIRouter, Request
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session

from app.backend.depends_db import get_db
from app.main import templates, oauth2_scheme
from app.models import User, Event
from app.routers.helpers import get_current_user


router = APIRouter(prefix='/users', tags=['users'])


@router.get("/me")
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user.username


@router.get("/dashboard/", response_class=HTMLResponse)
async def dashboard(request: Request, token: Annotated[str, Depends(oauth2_scheme)]):
    user = get_current_user(Session(), token=token)
    return templates.TemplateResponse("dashboard.html", {"request": request, "user": user})
