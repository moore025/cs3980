from contextlib import asynccontextmanager
import logging
from logging_setup import setup_logging
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
from db.db_context import init_database
from routers.review import review_router
from routers.user import user_router
import os

setup_logging()
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # on startup event
    logger.info("Application starts...")
    print(os.system("pwd"))
    await init_database()
    yield
    # on shutdown event
    logger.info("Application shuts down...")


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

app.mount("/", StaticFiles(directory="../frontend"), name="static")

# uvicorn.run(app, host="localhost", port=8000)
