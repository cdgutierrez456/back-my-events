from pydantic import BaseModel, ConfigDict
from datetime import datetime

class EventBase(BaseModel):
    event_name: str
    initial_date: datetime
    end_date: datetime
    speaker_name: str
    state_id: int

class EventCreate(EventBase):
    pass

class EventOut(EventBase):
    id_event: int
    model_config = ConfigDict(from_attributes=True)