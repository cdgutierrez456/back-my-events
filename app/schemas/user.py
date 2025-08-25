from pydantic import BaseModel, Field, ConfigDict

class UserBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=80)
    email: str
    profile_id: int
    state_id: int

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id_user: int
    model_config = ConfigDict(from_attributes=True)