from models.producto_models import ProductoCollection
from models.db import productos_collection
from fastapi import HTTPException


async def get_productos():
    """
    Get a list of products
    :return: A list of products
    """
    productos = await productos_collection.find().to_list(1000)
    return ProductoCollection(productos=productos)


async def get_producto(codigo: str):
    """
    Get a single product
    :param codigo: The code of the product
    :return: The product
    """
    if (producto := await productos_collection.find_one({"codigo": codigo})) is not None:
        return producto

    raise HTTPException(
        status_code=404, detail=f"Product with code {codigo} not found"
    )