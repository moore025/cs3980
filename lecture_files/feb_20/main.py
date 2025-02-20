from enum import Enum
from fastapi import FastAPI
from todo import todo_router


app = FastAPI()

app.include_router(todo_router, tags=["todos"], prefix="/todos")


@app.get("/")
async def welcome() -> dict:
    """My document summary"""
    return {"msg": "hello world"}


@app.get("/items")
async def get_items() -> dict:
    return {"item1": "book1"}


@app.get("/items/foo")  # works
async def get_item() -> dict:
    return {"foo": "bar"}


@app.get("/items/{item_id}")
async def get_item(item_id: int) -> dict:
    if item_id == 1:
        return {"item1": "book1"}
    else:
        return {}


@app.get("/items/{id}")  # This api will use query parameter
async def get_item_by_item_id(item_id: int) -> dict:
    if item_id == 1:
        return {"item1": "book1"}
    else:
        return {}


@app.get("/items/r")  # this path doesn't work
async def get_item() -> dict:
    return {"foo": "bar"}


class PersonType(str, Enum):
    student = "Student"
    employee = "Employee"
    patient = "Patient"


@app.get("/persons/{peron_type}")
async def get_persons_with_type_of(peron_type: PersonType) -> dict:
    if peron_type is PersonType.student:
        return {"item1": "book1"}
    if peron_type is PersonType.employee:
        return {"employee1": "name name1", "employee2": "name name2"}
    if peron_type.value == "Patient":
        return {"patient1": "p1 t1"}
    else:
        return {}
