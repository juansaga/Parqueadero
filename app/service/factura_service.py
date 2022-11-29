from datetime import datetime
from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.utils.db import get_db
from app.model.factura import Factura

class Facturas_Repository:
    
    # Se define la función para inicializar la clase
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db
    def list(self) -> list[Factura]:
        return self.db.query(Factura).all()

    def create(self, placa :str, marca:str, fk_celda: int ,hr_ingreso: datetime, hr_salida: datetime , total_factura: float, estado: bool) -> Factura:
        """Función para crear la base de datos de las facturas"""
        
        db_factura = Factura (placa=placa, marca=marca, fk_celda= fk_celda, hr_ingreso=hr_ingreso , hr_salida= hr_salida,total_factura=total_factura ,estado=estado)
        self.db.add(db_factura)
        self.db.commit()
        self.db.refresh(db_factura)
        return db_factura