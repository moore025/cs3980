from pydantic import BaseModel
from beanie import Document


class Todo(Document):
    id: int
    title: str
    description: str

    class Settings:
        name = "todos"


class TodoRequest(BaseModel):
    title: str
    description: str
