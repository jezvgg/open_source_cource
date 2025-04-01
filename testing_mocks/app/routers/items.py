import json

from fastapi import APIRouter, HTTPException, UploadFile

from app.routers import users_list
from core.enums import ConvertType
from core.converter import Converter


router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)


items: dict[str, bytes] = {}


@router.post('/add/{username}', status_code=200)
async def add_item(username: str, file: UploadFile):
    '''
    Сервис добавления CSV файла к пользователю.
    
    :param username: Никнейм пользователя
    :param file: Файл, который нужно прикерпить
    '''
    if username not in users_list:
        raise HTTPException(status_code=404, detail='User not found!')
    
    items[username] = Converter.deconvert(ConvertType.CSV, file.file.read())
    return 'ok'


@router.get('/get/{username}')
async def get_item(username: str):
    '''
    Сервис реализующй логику получения файла пользователя.

    :param username: Никнейм пользователя
    '''
    if username not in users_list:
        raise HTTPException(status_code=404, detail='User not found!')

    item = Converter.convert(ConvertType.JSON, items[username]).decode('utf-8')

    return json.loads(item)