from beanie import Document
from pydantic import BaseModel


class Restaurant(Document):
    id: int
    name: str
    classification: str  # Italian, Mexican, Bar & Grill, etc.


class RestaurantRequest(BaseModel):
    name: str
    classification: str
