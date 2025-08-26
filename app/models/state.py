from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base

class State(Base):
    __tablename__ = 'states'

    id_state = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)

    # Relaciones inversas
    permissions = relationship("Permission", back_populates="state")
    profiles = relationship("Profile", back_populates="state")
    users = relationship("User", back_populates="state")
    events = relationship("Event", back_populates="state") 