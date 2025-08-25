from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Permission(Base):
    __tablename__ = 'permissions'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    route = Column(String, nullable=False)
    state_id = Column(Integer, ForeignKey('states.id_state'))

    # Relaciones
    state = relationship("State", back_populates="permissions")
    profiles = relationship("ProfilePermission", back_populates="permission")