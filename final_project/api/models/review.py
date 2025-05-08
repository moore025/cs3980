from fastapi import File, UploadFile
from pydantic import BaseModel
from beanie import Document


class Review(Document):
    restaurant: str
    rating: str
    description: str
    created_by: str
    image: str | None = None

    class Settings:
        name = "reviews"


class ReviewRequest(BaseModel):
    restaurant: str
    rating: str
    description: str
