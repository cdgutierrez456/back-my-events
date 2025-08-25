from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class ProfilePermission(Base):
    __tablename__ = 'profile_permission'

    perfil_id = Column(Integer, ForeignKey('profiles.id_profile'), primary_key=True)
    permission_id = Column(Integer, ForeignKey('permissions.id_permission'), primary_key=True)

    # Relaciones
    profile = relationship("Profile", back_populates="permissions")
    permission = relationship("Permission", back_populates="profiles")