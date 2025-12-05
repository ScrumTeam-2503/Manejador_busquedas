from fastapi import APIRouter, status, Body
import logic.pedido_logic as pedido_service
from models.pedido_models import PedidoOut, PedidoCollection

router = APIRouter()
ENDPOINT_NAME = "/pedidos"


@router.get(
    "/",
    response_description="List all orders",
    response_model=PedidoCollection,
    status_code=status.HTTP_200_OK,
)
async def get_pedidos():
    return await pedido_service.get_pedidos()


@router.get(
    "/{id}",
    response_description="Get a single order by its ID",
    response_model=PedidoOut,
    status_code=status.HTTP_200_OK,
)
async def get_pedido(id: str):
    return await pedido_service.get_pedido(id)
