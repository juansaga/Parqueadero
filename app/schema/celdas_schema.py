from pydantic import BaseModel

from typing import Optional

class CreateCelda(BaseModel):
    tipo_celda: str
    estado: bool

class Celdas(BaseModel):
    id: int
    tipo_celda: str
    estado: bool

    class Config:
        orm_mode = True