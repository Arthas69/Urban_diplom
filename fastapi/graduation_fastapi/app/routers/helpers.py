from datetime import datetime, timezone, timedelta
from typing import Annotated

import jwt
from fastapi import Depends, HTTPException, status
from jwt import InvalidTokenError
from pydantic import ValidationError
from sqlalchemy import select, insert
from sqlalchemy.orm import Session
from secrets import compare_digest

from app.backend.depends_db import get_db
from app.config import ALGORITHM, SECRET_KEY
from app.main import oauth2_scheme
from app.models import User
from app.schemas import TokenData, UserCreate, Event, EventCreate


def get_user(
        db: Annotated[Session, Depends(get_db)],
        username: str):
    return db.scalar(select(User).where(username == User.username))


def authenticate_user(db: Annotated[Session, Depends(get_db)], username: str, password: str):
    user = get_user(db, username)
    if not user:
        return False
    if not compare_digest(password, user.password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(
        db: Annotated[Session, Depends(get_db)],
        token: Annotated[str, Depends(oauth2_scheme)]):

    authenticate_value = "Bearer"
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": authenticate_value},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except (InvalidTokenError, ValidationError):
        raise credentials_exception
    user = get_user(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


def create_user(
        db: Annotated[Session, Depends(get_db)],
        user_data: UserCreate):
    db.execute(insert(User).values(
        username=user_data.username,
        password=user_data.password
    ))
    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction_id': 'Successful'
    }


def get_events(db: Annotated[Session, Depends(get_db)], user_data: User):
    return db.scalars(select(Event).where(Event.owner_id == user_data.id)).all()


def create_event(db: Annotated[Session, Depends(get_db)], event: EventCreate, user_id: int):
    db_event = Event(**event.dict(), owner_id=user_id)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction_id': 'Successful'
    }