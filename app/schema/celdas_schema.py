from pydantic import BaseModel

from typing import Optional

# Se define la clase CreateCelda
class CreateCelda(BaseModel):
    tipo_celda: str
    estado: bool

# Se define la clase Celdas
class Celdas(BaseModel):
    id: int
    tipo_celda: str
    estado: bool

# Se establece la configuración de tal forma que el modelo creado a partir de 
# una instancia de clase arbitraria soporte modelos que vayan a objetos ORM
    class Config:
        orm_mode = True