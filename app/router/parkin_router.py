from fastapi import APIRouter
from starlette import status

from app.endpoints.celdas_endpoint import CeldaAPI
from app.schema.celdas_schema import Celdas

router = APIRouter()
celdas_api = CeldaAPI()


router.add_api_route(path="/", endpoint=celdas_api.list, response_model=list[Celdas], status_code=status.HTTP_200_OK, methods= ["GET"])
router.add_api_route(path="/", endpoint=celdas_api.create, response_model=Celdas, status_code = status.HTTP_201_CREATED, methods=["POST"])