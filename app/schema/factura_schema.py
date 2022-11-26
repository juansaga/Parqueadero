from datetime import datetime
from pydantic import BaseModel

from typing import Optional

class CreateFactura(BaseModel):
    placa :str
    marca:str
    fk_celda: int 
    hr_ingreso: datetime
    hr_salida: datetime 
    total_factura: float
    estado: bool

class Factura(BaseModel):
    id: int
    placa :str
    marca:str
    fk_celda: int 
    hr_ingreso: datetime
    hr_salida: datetime 
    total_factura: float
    estado: bool

    class Config:
        orm_mode = True