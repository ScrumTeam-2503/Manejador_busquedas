import os
import motor.motor_asyncio
from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated

client = motor.motor_asyncio.AsyncIOMotorClient(
    f"mongodb://provesi_user:scrumteam@{os.getenv('PROVESI_DB_HOST', '100.26.61.156 ')}:27017/provesi_mongodb?authSource=provesi_mongodb"
)
db = client.get_database("provesi_mongodb")
pedidos_collection = db.get_collection("pedidos")
productos_collection = db.get_collection("productos")


async def set_provesi_db():
    await pedidos_collection.create_index("id", unique=True)
    await productos_collection.create_index("codigo", unique=True)


# Represents an ObjectId field in the database.
PyObjectId = Annotated[str, BeforeValidator(str)]