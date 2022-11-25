from datetime import datetime
from sqlalchemy import Column, String, Integer, Boolean
from app.utils.db import Base

class Celdas(Base):
    __tablename__ = "celdas"

    id  = Column(Integer, primary_key=True, index=True)
    tipo_celda = Column(String)
    estado = Column(Boolean)