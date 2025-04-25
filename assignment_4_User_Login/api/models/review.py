from pydantic import BaseModel
from beanie import Document


class Review(Document):
    id: int
    restaurant: str
    rating: str
    description: str

    class Settings:
        name = "reviews"


class ReviewRequest(BaseModel):
    restaurant: str
    rating: str
    description: str
