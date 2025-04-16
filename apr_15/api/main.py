from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
from db.db_context import init_database
from routers.todo import todo_router
from routers.user import user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # on startup event
    print("Application starts...")
    await init_database()
    yield
    # on shutdown event
    print("Application shuts down...")


app = FastAPI(title="Todo App", version="2.0.0", lifespan=lifespan)
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


@app.get("/")
async def read_index():
    return FileResponse("../frontend/index.html")


app.include_router(todo_router, tags=["Todos"], prefix="/todos")
app.include_router(user_router, tags=["Users"], prefix="/users")

app.mount("/", StaticFiles(directory="../frontend"), name="static")

# uvicorn.run(app, host="localhost", port=8000)
