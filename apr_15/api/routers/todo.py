from fastapi import APIRouter, Path, HTTPException, status

from models.todo import Todo, TodoRequest

todo_router = APIRouter()

todo_list = []
max_id: int = 0


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
    todo = Todo.get(id)
    if todo:
        return todo
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"The todo with ID={id} is not found.",
    )


@todo_router.put("/{id}")
async def update_todo(todo: TodoRequest, id: int) -> dict:
    for x in todo_list:
        if x.id == id:
            x.title = todo.title
            x.description = todo.description
            return {"message": "Todo updated successfully"}

    return {"message": f"The todo with ID={id} is not found."}


@todo_router.delete("/{id}")
async def delete_todo(id: int) -> dict:
    for i in range(len(todo_list)):
        todo = todo_list[i]
        if todo.id == id:
            todo_list.pop(i)
            return {"message": f"The todo with ID={id} has been deleted."}

    return {"message": f"The todo with ID={id} is not found."}
