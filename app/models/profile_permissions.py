from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base

class ProfilePermission(Base):
    __tablename__ = 'profile_permission'

    perfil_id = Column(Integer, ForeignKey('profiles.id_profile'), primary_key=True)
    permission_id = Column(Integer, ForeignKey('permissions.id_permission'), primary_key=True)

    # Relaciones
    profile = relationship("Profile", back_populates="permissions")
    permission = relationship("Permission", back_populates="profiles")