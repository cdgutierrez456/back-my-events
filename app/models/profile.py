from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base

class Profile(Base):
    __tablename__ = 'profiles'

    id_profile = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    state_id = Column(Integer, ForeignKey('states.id_state'))

    # Relaciones
    state = relationship("State", back_populates="profiles")
    users = relationship("User", back_populates="profile")
    permissions = relationship("ProfilePermission", back_populates="profile")