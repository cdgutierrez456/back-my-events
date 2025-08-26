from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.event import EventCreate, EventOut
from app.crud import event as crud_event
from app.database import get_db

router = APIRouter()

@router.post("/create/", response_model=EventOut)
async def create_event(event: EventCreate, db: AsyncSession = Depends(get_db)):
    return await crud_event.create_event(db, event)

@router.get("/", response_model=list[EventOut])
async def list_events(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    return await crud_event.list_users(db, skip, limit)