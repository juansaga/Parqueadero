from fastapi.params import Depends
from typing import List

from app.schema.celdas_schema import Celdas, CreateCelda
from app.service.celda_service import Celdas_Repository

class CeldaAPI:
    """Clase para interactuar con las celdas. """
    def list(self, celda_repository: Celdas_Repository = Depends(Celdas_Repository)) -> List[Celdas]:
        return celda_repository.list()

    def create(self, celda: CreateCelda, celda_repository: Celdas_Repository = Depends(Celdas_Repository)) -> Celdas:
        return celda_repository.create(tipo_celda=celda.tipo_celda, estado=celda.estado)