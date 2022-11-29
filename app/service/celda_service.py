from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.utils.db import get_db
from app.model.celdas import Celdas

class Celdas_Repository:
    
    # Se define la función para inicializar la clase
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db
    def list(self) -> list[Celdas]:
        return self.db.query(Celdas).all()

    def create(self, tipo_celda: str, estado: bool) -> Celdas:
        """Función para crear la base de datos de las celdas"""
        
        db_celdas = Celdas (tipo_celda=tipo_celda, estado=estado)
        self.db.add(db_celdas)
        self.db.commit()
        self.db.refresh(db_celdas)
        return db_celdas