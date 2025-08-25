from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.database import Base

class Event(Base):
    __tablename__ = 'events'

    id_event = Column(Integer, primary_key=True, index=True)
    event_name = Column(String, nullable=False)
    initial_date = Column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    end_date = Column(DateTime, nullable=True)
    speaker_name = Column(String, nullable=False)
    state_id = Column(Integer, ForeignKey('states.id_state'))

    # Relaciones
    state = relationship("State", back_populates="events")