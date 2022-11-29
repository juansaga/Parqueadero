from datetime import datetime
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, DateTime, Float
from app.utils.db import Base

# Se define la clase Factura, primordial para la implementación del proyecto 
# parqueadero
class Factura(Base):
    """Una de las clases principales para el correcto funcionamiento del
    parqueadero"""
    __tablename__ = "factura"

    id  = Column(Integer, primary_key=True, index=True)
    placa = Column(String)
    marca = Column(String)
    fk_celda = Column(Integer, ForeignKey("celdas.id"))
    hr_ingreso = Column(DateTime)
    hr_salida = Column(DateTime)
    total_factura = Column(Float)
    estado = Column(Boolean)