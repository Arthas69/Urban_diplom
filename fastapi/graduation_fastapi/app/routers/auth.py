from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, HTTPException, Depends, status, Form, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.backend.depends_db import get_db
from app.config import ACCESS_TOKEN_EXPIRE_MINUTES
from app.main import templates
from app.routers.helpers import create_access_token, authenticate_user, get_user, create_user
from app.schemas import Token, UserCreate

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login/")
async def login_with_token(
    db: Annotated[Session, Depends(get_db)],
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=access_token_expires,
    )
    return Token(access_token=access_token, token_type="bearer")


@router.get("/register/", response_class=HTMLResponse)
async def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@router.post("/register/")
async def register(
        username: Annotated[str, Form()],
        password: Annotated[str, Form()],
        db: Annotated[Session, Depends(get_db)]):
    user = UserCreate(username=username, password=password)
    print(Token)
    db_user = get_user(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already taken")
    create_user(db, user)
    return RedirectResponse(url="/login/", status_code=status.HTTP_303_SEE_OTHER)


@router.get("/login/", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})
