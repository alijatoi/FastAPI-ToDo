from pydantic import BaseModel

# Schema for creating a new to-do
class ToDoCreate(BaseModel):
    title: str
    description: str
    completed: bool = False


# Schema for updating a to-do
class ToDoUpdate(BaseModel):
    title: str
    description: str
    completed: bool = False


# Schema for reading a to-do
class ToDo(BaseModel):
    id: int
    title: str
    description: str
    completed: bool

    class Config:
        orm_mode = True
