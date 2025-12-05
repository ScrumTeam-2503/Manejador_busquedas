from fastapi import APIRouter

from views import producto_view, pedido_view

API_PREFIX = "/api"
router = APIRouter()

router.include_router(producto_view.router, prefix=producto_view.ENDPOINT_NAME)
router.include_router(pedido_view.router, prefix=pedido_view.ENDPOINT_NAME)