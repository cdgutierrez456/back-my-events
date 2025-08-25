from pydantic import BaseModel, ConfigDict
from typing import Optional

class ProfileBase(BaseModel):
    name: str
    description: Optional[str]
    state_id: int

class ProfileCreate(ProfileBase):
    pass

class Profile(ProfileBase):
    id_profile: int
    model_config = ConfigDict(from_attributes=True)