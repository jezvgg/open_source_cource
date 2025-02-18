import json

from fastapi import APIRouter, HTTPException, UploadFile

from app.routers import users
from core.enums import ConvertType
from core.deconverter import Deconverter
from core.converter import Converter


router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)


items: dict[str, str] = {}
deconverter = Deconverter()
converter = Converter()


@router.post('/add/{username}', status_code=200)
async def add_item(username: str, file: UploadFile) -> str:
    if username not in users:
        return HTTPException(status_code=404, detail='User not found!')
    items[username] = deconverter.deconvert(ConvertType.CSV, file)
    return 'ok'


@router.get('/get/{username}')
async def get_item(username: str) -> dict:
    if username not in users:
        return HTTPException(status_code=404, detail='User not found!')
    return json.loads(converter.convert(ConvertType.JSON, items[username]))