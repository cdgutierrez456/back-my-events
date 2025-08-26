from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base

class User(Base):
    __tablename__ = 'users'

    id_user = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    password = Column(String, nullable=False)
    profile_id = Column(Integer, ForeignKey('profiles.id_profile'))
    state_id = Column(Integer, ForeignKey('states.id_state'))

    # Relaciones
    profiles = relationship("Profile", back_populates="users")
    state = relationship("State", back_populates="users")