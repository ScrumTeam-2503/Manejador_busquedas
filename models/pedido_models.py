from enum import Enum
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict
from typing import List
from models.db import PyObjectId

class MetodoPago(str, Enum):
    Efectivo = "efectivo"
    TarjetaDebito = "tarjeta debito"
    TarjetaCredito = "tarjeta credito"
    Transferencia = "transferencia"

class Pedido(BaseModel):
    estado: str = Field(...)
    metodo_pago: MetodoPago = Field(...)
    fecha_creacion: datetime = Field(...)
    fecha_actualizacion: datetime = Field(...)
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "estado": "Pendiente",
                "metodo_pago": MetodoPago.Efectivo,
                "fecha_creacion": "2025-11-12T00:00:00",
                "fecha_actualizacion": "2025-11-12T00:00:00"
            }
        }
    )


class PedidoOut(Pedido):
    id: PyObjectId = Field(alias="id", default=None, serialization_alias="id")
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "estado": "Pendiente",
                "metodo_pago": MetodoPago.Efectivo,
                "fecha_creacion": "2025-11-12T00:00:00",
                "fecha_actualizacion": "2025-11-12T00:00:00"
            }
        }
    )

class PedidoCollection(BaseModel):
    pedidos: List[PedidoOut] = Field(...)