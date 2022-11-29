from fastapi.params import Depends
from typing import List

from app.schema.factura_schema import Factura, CreateFactura
from app.service.factura_service import Facturas_Repository

class FacturaAPI:
    """Clase para interactuar con las facturas. """
    def list(self, facturas_repository: Facturas_Repository = Depends(Facturas_Repository)) -> List[Factura]:
        return facturas_repository.list()

    def create(self, factura: CreateFactura, facturas_repository: Facturas_Repository = Depends(Facturas_Repository)) -> Factura:
        return facturas_repository.create(placa=factura.placa , marca=factura.marca, fk_celda=factura.fk_celda , hr_ingreso=factura.hr_ingreso , hr_salida= factura.hr_salida,total_factura=factura.total_factura , estado=factura.estado)

        