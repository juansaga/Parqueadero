from pydantic import BaseModel

from typing import Optional

# Se define la clase CreateCelda
class CreateCelda(BaseModel):
    """La clase CreateCelda posee como atributos el tipo de celda (string),
    el estado de la celda (boolean)"""
    tipo_celda: str
    estado: bool

# Se define la clase Celdas
class Celdas(BaseModel):
    """La clase Celdas tiene como atributos una clave primaria (integer), el
    tipo de celda (string) y el estado de la celda (boolean)"""
    id: int
    tipo_celda: str
    estado: bool

# Se establece la configuración de tal forma que el modelo creado a partir de 
# una instancia de clase arbitraria soporte modelos que vayan a objetos ORM
    class Config:
        orm_mode = True