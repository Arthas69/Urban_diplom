from datetime import datetime
from typing import Annotated

from fastapi import APIRouter, Depends, status, Form, Request, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy import select, update
from sqlalchemy.orm import Session

from app.backend.depends_db import get_db
from app.main import templates
from app.models import User, Event
from app.routers.helpers import get_current_user, create_event, get_events
from app.schemas import EventCreate, EventUpdate

router = APIRouter(prefix='/events', tags=['events'])


@router.post("/")
async def create_event_view(
        title: Annotated[str, Form()],
        description: Annotated[str, Form()],
        db: Annotated[Session, Depends(get_db)],
        current_user: Annotated[User, Depends(get_current_user)]):
    event = EventCreate(title=title, description=description, datetime=datetime.now())
    create_event(db, event, current_user.id)
    return RedirectResponse(url="/events/", status_code=status.HTTP_201_CREATED)


@router.get("/")
async def read_events(
        db: Annotated[Session, Depends(get_db)],
        current_user: Annotated[User, Depends(get_current_user)]):
    events = get_events(db, current_user)
    return events


@router.get("/create_event")
async def create_event_page(request: Request,
                            db: Annotated[Session, Depends(get_db)],
                            current_user: Annotated[User, Depends(get_current_user)]):
    events = get_events(db, current_user)
    return events
    # return templates.TemplateResponse("create_event.html", {"request": request})


@router.put("/update_event")
async def update_event_view(
        db: Annotated[Session, Depends(get_db)],
        event_id: int,
        new_event: EventUpdate,
        current_user: Annotated[User, Depends(get_current_user)]):
    event = db.scalar(select(Event).where(Event.id == event_id))
    if event is None or event.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not exist or you can't update this event")

    db.execute(update(Event).where(Event.id == event_id).values(
        title=new_event.title,
        description=new_event.description,
        # datetime=datetime.now()
    ))
    db.commit()

    return {
        "status_code": status.HTTP_200_OK,
        "message": "Event updated successfully"
    }


@router.delete('/delete_event')
async def delete_event_view(db: Annotated[Session, Depends(get_db)],
                            event_id: int,
                            current_user: Annotated[User, Depends(get_current_user)]):
    event = db.scalar(select(Event).where(Event.id == event_id))
    if not event or event.owner_id != current_user.id:
        return HTTPException(status_code=404, detail="You cannot delete this event")
    db.delete(event)
    db.commit()
    return {"status_code": status.HTTP_204_NO_CONTENT, "message": "Event deleted successfully"}
