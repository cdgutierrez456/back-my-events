from pydantic import BaseModel, ConfigDict

class ProfilePermissionBase(BaseModel):
    perfil_id: int
    permission_id: int

class ProfilePermissionCreate(ProfilePermissionBase):
    pass

class ProfilePermission(ProfilePermissionBase):
    model_config = ConfigDict(from_attributes=True)