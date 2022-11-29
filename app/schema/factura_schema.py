from datetime import datetime
from pydantic import BaseModel

from typing import Optional

# Se define la clase CreateFactura
class CreateFactura(BaseModel):
    """La clase CreateFactura posee como atributos la placa del vehículo 
    (string),la marca (string), una clave foranea (int), la hora de ingreso del 
    vehículo (datetime), la hora de salida del vehículo (datetime), el total de 
    dinero que se debe pagar (float) y el estado de la factura (boolean)"""
    placa :str
    marca:str
    fk_celda: int 
    hr_ingreso: datetime
    hr_salida: datetime 
    total_factura: float
    estado: bool

# Se define la clase Factura
class Factura(BaseModel):
    """La clase Factura posee como atributos una clave primaria (int), 
    la placa del vehículo (string),la marca (string), una clave foranea (int), 
    la hora de ingreso del vehículo (datetime), la hora de salida del vehículo 
    (datetime), el total de dinero que se debe pagar (float) y el estado de 
    la factura (boolean)"""
    id: int
    placa :str
    marca:str
    fk_celda: int 
    hr_ingreso: datetime
    hr_salida: datetime 
    total_factura: float
    estado: bool

# Se establece la configuración de tal forma que el modelo creado a partir de 
# una instancia de clase arbitraria soporte modelos que vayan a objetos ORM
    class Config:
        orm_mode = True