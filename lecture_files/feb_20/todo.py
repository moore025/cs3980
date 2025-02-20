from fastapi import APIRouter
from pydantic import BaseModel


class Todo(BaseModel):
    id: int
    item: str


todo_router = APIRouter()

todo_list = []


@todo_router.get("")
async def get_todos() -> dict:
    return {"todos": todo_list}


@todo_router.post("")
async def add_todos(todo: Todo) -> dict:
    todo_list.append(todo)
    return {"msg": "new todo added"}
