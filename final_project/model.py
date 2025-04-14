from pydantic import BaseModel


class Review(BaseModel):
    id: int
    restaurant: str
    rating: str  # Rating 1-10
    description: str


class ReviewRequest(BaseModel):
    restaurant: str
    rating: str
    description: str
