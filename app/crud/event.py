from sqlalchemy.ext.asyncio import AsyncSession
from models import Event
from schemas import EventCreate
from datetime import timezone

async def create_event(db: AsyncSession, event: EventCreate) -> Event:
    db_event = Event(
        event_name=event.event_name,
        initial_date=event.initial_date.astimezone(timezone.utc),
        end_date=event.end_date.astimezone(timezone.utc),
        speaker_name=event.speaker_name,
        state_id=event.state_id
    )
    db.add(db_event)
    await db.commit()
    await db.refresh(db_event)
    return db_event
