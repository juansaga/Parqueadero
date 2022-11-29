from datetime import datetime
from pydantic import BaseModel

from typing import Optional

# Se define la clase CreateFactura
class CreateFactura(BaseModel):
    placa :str
    marca:str
    fk_celda: int 
    hr_ingreso: datetime
    hr_salida: datetime 
    total_factura: float
    estado: bool

# Se define la clase Factura
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