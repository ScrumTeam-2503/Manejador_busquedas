from fastapi import APIRouter, status, Request
from slowapi import Limiter
from slowapi.util import get_remote_address
import logic.producto_logic as producto_service
from models.producto_models import ProductoOut, ProductoCollection
from config import limiter

router = APIRouter()
ENDPOINT_NAME = "/productos"

@router.get(
    "/",
    response_description="List all products",
    response_model=ProductoCollection,
    status_code=status.HTTP_200_OK,
)
@limiter.limit("10/second")
async def get_productos(request: Request):
    return await producto_service.get_productos()


@router.get(
    "/{codigo}",
    response_description="Get a single product by its code",
    response_model=ProductoOut,
    status_code=status.HTTP_200_OK,
)
@limiter.limit("20/second")
async def get_producto(codigo: str, request: Request):
    return await producto_service.get_producto(codigo)
