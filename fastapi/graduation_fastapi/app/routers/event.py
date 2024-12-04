from datetime import datetime
from typing import Annotated

from fastapi import APIRouter, Depends, status, Form, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.backend.depends_db import get_db
from app.main import templates
from app.models import User, Event
from app.routers.helpers import get_current_user, create_event, get_events
from app.schemas import EventCreate

router = APIRouter(prefix='/events', tags=['events'])


@router.post("/")
async def create_event_view(
        title: Annotated[str, Form()],
        description: Annotated[str, Form()],
        db: Annotated[Session, Depends(get_db)],
        current_user: Annotated[User, Depends(get_current_user)]):
    event = EventCreate(title=title, description=description, datetime=datetime.now())
    create_event(db, event, current_user.id)
    return RedirectResponse(url="/events/", status_code=status.HTTP_303_SEE_OTHER)


@router.get("/create_event")
async def create_event_page(request: Request, current_user: Annotated[User, Depends(get_current_user)]):
    return templates.TemplateResponse("create_event.html", {"request": request})


@router.get("/")
async def read_events(db: Annotated[Session, Depends(get_db)], current_user: Annotated[User, Depends(get_current_user)]):
    events = get_events(db, current_user)
    return events
