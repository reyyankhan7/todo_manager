from pydantic import BaseModel
from datetime import date

class TodoBase(BaseModel):
    title: str
    deadline: date
    status: str = "pending"

class TodoCreate(TodoBase):
    pass

class TodoResponse(TodoBase):
    id: int
    class Config:
        orm_mode = True
