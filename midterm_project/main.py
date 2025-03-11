import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
from review import review_router

app = FastAPI()
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


@app.get("/")
async def read_index():
    return FileResponse("./frontend/index.html")


app.include_router(review_router, tags=["Reviews"], prefix="/reviews")

app.mount("/", StaticFiles(directory="frontend"), name="static")

# uvicorn.run(app, host="localhost", port=8000)
