from fastapi import APIRouter, Path, HTTPException, status

from models.todo import Todo, TodoRequest

todo_router = APIRouter()

max_id: int = (
    0  # NOT IDEAL because if you stop session and reload, then you open the door for duplicate ID's. Try doing a query of the database instead to get id numbers.
)


@todo_router.post("", status_code=status.HTTP_201_CREATED)
async def add_todo(todo: TodoRequest) -> Todo:
    global max_id
    max_id += 1  # auto increment ID

    newTodo = Todo(id=max_id, title=todo.title, description=todo.description)
    await Todo.insert_one(newTodo)
    return newTodo


@todo_router.get("")
async def get_todos() -> list[Todo]:
    return await Todo.find_all().to_list()


@todo_router.get("/{id}")
async def get_todo_by_id(id: int = Path(..., title="default")) -> Todo:
    todo = await Todo.get(id)
    if todo:
        return todo
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"The todo with ID={id} is not found.",
    )


@todo_router.put("/{id}")
async def update_todo(todo: TodoRequest, id: int) -> dict:
    existing_todo = await Todo.get(id)
    if existing_todo:
        existing_todo.title = todo.title
        existing_todo.description = todo.description
        await existing_todo.save()
        return {"message": "Todo updated successfully"}

    return {"message": f"The todo with ID={id} is not found."}


@todo_router.delete("/{id}")
async def delete_todo(id: int) -> dict:
    todo = await Todo.get(id)
    await todo.delete()
    return {"message": f"The todo with ID={id} has been deleted."}
