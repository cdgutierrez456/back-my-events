from pydantic import BaseModel, ConfigDict

class StateBase(BaseModel):
    description: str

class StateCreate(StateBase):
    pass

class State(StateBase):
    id_state: int
    model_config = ConfigDict(from_attributes=True)