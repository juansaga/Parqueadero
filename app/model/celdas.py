from datetime import datetime
from sqlalchemy import Column, String, Integer, Boolean
from app.utils.db import Base

# Se define la clase Celdas, primordial para la implementación del proyecto 
# parqueadero
class Celdas(Base):
    """Una de las clases principales para el correcto funcionamiento del
    parqueadero"""
    __tablename__ = "celdas"

    id  = Column(Integer, primary_key=True, index=True)
    tipo_celda = Column(String)
    estado = Column(Boolean)