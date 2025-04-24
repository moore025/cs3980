from beanie import init_beanie
from models.my_config import get_settings
from motor.motor_asyncio import AsyncIOMotorClient

from models.restaurant import Restaurant
from models.user import User
from models.review import Review


async def init_database():
    my_config = get_settings()
    print(my_config)
    client = AsyncIOMotorClient(my_config.connection_string)
    db = client["review_app"]
    await init_beanie(database=db, document_models=[Review, User, Restaurant])
