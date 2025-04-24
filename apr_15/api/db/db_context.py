import logging
from beanie import init_beanie
from models.my_config import get_settings
from motor.motor_asyncio import AsyncIOMotorClient

from models.todo import Todo
from models.user import User
from models.movie import Movie

logger = logging.getLogger(__name__)


async def init_database():
    my_config = get_settings()
    print(my_config)
    client = AsyncIOMotorClient(my_config.connection_string)
    logger.info("Database client created")
    db = client["todo_app"]
    await init_beanie(database=db, document_models=[User, Todo, Movie])
