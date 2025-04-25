from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
from db.db_context import init_database
from routers.review import review_router
from routers.user import user_router
from routers.movie import movie_router
import os


@asynccontextmanager
async def lifespan(app: FastAPI):
    # on startup event
    print("Application starts...")
    print(os.system("pwd"))
    await init_database()
    yield
    # on shutdown event
    print("Application shuts down...")


app = FastAPI(title="Review App", version="2.0.0", lifespan=lifespan)
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


app.include_router(review_router, tags=["Reviews"], prefix="/reviews")
app.include_router(user_router, tags=["Users"], prefix="/users")
app.include_router(movie_router, tags=["Restaurants"], prefix="/restaurants")

app.mount("/", StaticFiles(directory="../frontend"), name="static")

# uvicorn.run(app, host="localhost", port=8000)
