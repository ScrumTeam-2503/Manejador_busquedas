from fastapi import APIRouter, status, Body
import logic.producto_logic as producto_service
from models.producto_models import ProductoOut, ProductoCollection

router = APIRouter()
ENDPOINT_NAME = "/productos"


@router.get(
    "/",
    response_description="List all products",
    response_model=ProductoCollection,
    status_code=status.HTTP_200_OK,
)
async def get_productos():
    return await producto_service.get_productos()


@router.get(
    "/{codigo}",
    response_description="Get a single product by its code",
    response_model=ProductoOut,
    status_code=status.HTTP_200_OK,
)
async def get_producto(codigo: str):
    return await producto_service.get_producto(codigo)
