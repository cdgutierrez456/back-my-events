from pydantic import BaseModel, ConfigDict

class PermissionBase(BaseModel):
    name: str
    route: str
    state_id: int

class PermissionCreate(PermissionBase):
    pass

class Permission(PermissionBase):
    id_permission: int
    model_config = ConfigDict(from_attributes=True)