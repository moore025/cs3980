from beanie import Document
from pydantic import BaseModel


class User(Document):
    username: str
    email: str
    role: str
    password: str  # hash and salted password in the database

    class Settings:
        name = "users"  # by default, if not having this settings, then the collection name is "Product"


class UserRequest(BaseModel):
    """
    **model for user sign up**
    """

    username: str
    email: str
    password: str  # plain text from user input


class UserDto(BaseModel):
    """
    **model for user sign up**
    """

    id: str
    username: str
    email: str
