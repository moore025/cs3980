from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from models.my_config import MyConfig
from models.product import Product
import asyncio

from models.student import Student


async def init_db():
    my_config = MyConfig()
    client = AsyncIOMotorClient(my_config.connection_string)
    db = client["test_db2"]
    await init_beanie(database=db, document_models=[Product, Student])
    data = await Product.insert_one(Product(name="pen", description="abc"))
    print(data)
    data = await Student.insert_one(Student(univ_id="0099999", name="John Doe"))
    print(data)


asyncio.run(init_db())
