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


# Create an API router for the authentication endpoints
router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login/")
async def login_with_token(
        db: Annotated[Session, Depends(get_db)],
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    """
    Authenticates a user with the provided username and password.
    If authentication is successful, the access_token will be returned
    """

    # Authenticate the user. If it fails, raise an error
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    # If authentication is successful, create an access token.
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=access_token_expires,
    )

    # Return the access token as a response.
    return Token(access_token=access_token, token_type="bearer")


@router.get("/register/", response_class=HTMLResponse)
async def register_page(request: Request):
    """
    Returns a HTML registration page.
    """
    return templates.TemplateResponse("register.html", {"request": request})


@router.post("/register/")
async def register(
        username: Annotated[str, Form()],
        password: Annotated[str, Form()],
        db: Annotated[Session, Depends(get_db)]) -> RedirectResponse:
    """
    Registers a new user in the database.
    """
    user = UserCreate(username=username, password=password)

    # Check if the username already exists in the database.
    db_user = get_user(db, user.username)

    # If it does, raise an error.
    if db_user:
        raise HTTPException(status_code=400, detail="Username already taken")

    # If not, create the user and return a success message.
    create_user(db, user)

    # Redirect the user to the login page.
    return RedirectResponse(url="/login/", status_code=status.HTTP_201_CREATED)


@router.get("/login/", response_class=HTMLResponse)
async def login_page(request: Request):
    """
    Returns a HTML login page.
    """
    return templates.TemplateResponse("login.html", {"request": request})
