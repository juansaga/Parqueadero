from fastapi import APIRouter
from starlette import status

from app.endpoints.celdas_endpoint import CeldaAPI
from app.schema.celdas_schema import Celdas

from app.endpoints.factura_endpoint import FacturaAPI
from app.schema.factura_schema import Factura


router = APIRouter()
celdas_api = CeldaAPI()
facturas_api  = FacturaAPI()


router.add_api_route(path="/celda", endpoint=celdas_api.list, response_model=list[Celdas], status_code=status.HTTP_200_OK, methods= ["GET"])
router.add_api_route(path="/celda", endpoint=celdas_api.create, response_model=Celdas, status_code = status.HTTP_201_CREATED, methods=["POST"])


router.add_api_route(path="/factura", endpoint=facturas_api.list, response_model=list[Factura], status_code=status.HTTP_200_OK, methods= ["GET"])
router.add_api_route(path="/factura", endpoint=facturas_api.create, response_model=Factura, status_code = status.HTTP_201_CREATED, methods=["POST"])