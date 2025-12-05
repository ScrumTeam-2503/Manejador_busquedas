from models.pedido_models import PedidoCollection
from models.db import pedidos_collection
from fastapi import HTTPException


async def get_pedidos():
    """
    Get a list of orders
    :return: A list of orders
    """
    pedidos = await pedidos_collection.find().to_list(1000)
    return PedidoCollection(pedidos=pedidos)


async def get_pedido(id: str):
    """
    Get a single order
    :param codigo: The id of the order
    :return: The order
    """
    if (pedido := await pedidos_collection.find_one({"id": id})) is not None:
        return pedido

    raise HTTPException(
        status_code=404, detail=f"Order with ID {id} not found"
    )