import logging
from beanie import init_beanie
from models.my_config import get_settings
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorGridFSBucket

from models.restaurant import Restaurant
from models.user import User
from models.review import Review

logger = logging.getLogger(__name__)


async def init_database():
    my_config = get_settings()
    print(my_config)
    client = AsyncIOMotorClient(my_config.connection_string)
    logger.info("Database client created")
    db = client["review_app"]
    fs = AsyncIOMotorGridFSBucket(db)
    await init_beanie(database=db, document_models=[Review, User, Restaurant])
