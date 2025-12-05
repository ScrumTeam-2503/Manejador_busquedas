from fastapi import APIRouter, status, Request
from slowapi import Limiter
from slowapi.util import get_remote_address
import logic.pedido_logic as pedido_service
from models.pedido_models import PedidoOut, PedidoCollection

router = APIRouter()
ENDPOINT_NAME = "/pedidos"

limiter = Limiter(key_func=get_remote_address)

@router.get(
    "/",
    response_description="List all orders",
    response_model=PedidoCollection,
    status_code=status.HTTP_200_OK,
)
@limiter.limit("10/second")
async def get_pedidos(request: Request):
    return await pedido_service.get_pedidos()


@router.get(
    "/{id}",
    response_description="Get a single order by its ID",
    response_model=PedidoOut,
    status_code=status.HTTP_200_OK,
)
@limiter.limit("20/second")
async def get_pedido(id: str, request: Request):
    return await pedido_service.get_pedido(id)
