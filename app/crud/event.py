from fastapi import HTTPException
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.event import Event
from app.schemas.event import EventCreate

async def create_event(db: AsyncSession, event: EventCreate) -> Event:
    db_event = Event(
        event_name=event.event_name,
        initial_date=event.initial_date.replace(tzinfo=None),
        end_date=event.end_date.replace(tzinfo=None),        
        speaker_name=event.speaker_name,
        state_id=event.state_id or 1
    )
    db.add(db_event)
    await db.commit()
    await db.refresh(db_event)
    return db_event

async def list_events(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(Event).offset(skip).limit(limit))
    return result.scalars().all()

async def delete_event(db: AsyncSession, event_id: int):
    result = await db.execute(select(Event).where(Event.id_event == event_id))
    event = result.scalar_one_or_none()

    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    await db.delete(event)
    await db.commit()