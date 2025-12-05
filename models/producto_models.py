from pydantic import BaseModel, Field, ConfigDict
from typing import List
from models.db import PyObjectId

class Producto(BaseModel):
    codigo: str = Field(...)
    nombre: str = Field(...)
    descripcion: str = Field(...)
    precio: int = Field(...)
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "codigo": "87FDS98F7S",
                "nombre": "Producto01",
                "descripcion": "Este es el producto 01 de Provesi",
                "precio": 999999
            }
        },
    )


class ProductoOut(Producto):
    id: PyObjectId = Field(alias="id", default=None, serialization_alias="id")
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "codigo": "87FDS98F7S",
                "nombre": "Producto01",
                "descripcion": "Este es el producto 01 de Provesi",
                "precio": 999999
            }
        }
    )

class ProductoCollection(BaseModel):
    productos: List[ProductoOut] = Field(...)