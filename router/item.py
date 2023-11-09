from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from sqlalchemy.orm import Session
from db.database import get_db

from schemas import ItemDisplayModel, Item
from auth.oauth2 import get_current_user


from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from pydantic import BaseModel
from typing import Optional

from db import db_user
from schemas import UserBaseModel, UserDisplayModel, ItemDisplayModel, ItemModel, Item, User

from db.models import DbItem, Ingredient, Extra


# Asegúrate de importar ItemBuilder desde el módulo adecuado
from builder import ItemBuilder


from auth.oauth2 import get_current_user
from db.db_item import CrudItems

from db import db_item

router = APIRouter(
    prefix='/item',
    tags=['Items']
)

router.mount("/static/css/", StaticFiles(directory="static/css"), name="static")
router.mount("/templates", StaticFiles(directory="templates"),
             name="templates")
templates = Jinja2Templates(directory="templates")



@router.post('/submit', response_model=ItemDisplayModel)
async def create_pedido(request: Item, db: Session = Depends(get_db)):
    pedido_new=CrudItems.create_pedido(db, request)
    return pedido_new


@router.get('/{items_id}')
async def get_pedido(items_id: int, db: Session = Depends(get_db)):
    pedido = CrudItems.get_pedido_by_id(items_id, db)
    # Devuelve el resultado desde la ruta
    return pedido
        

@router.put('/put_by_id/', response_model=ItemDisplayModel)
async def update_pedido(item_id: int, request: Item, db: Session = Depends(get_db), current_user: UserBaseModel = Depends(get_current_user)):
    pedido = CrudItems.update_pedido(item_id, db, request)
    return pedido

@router.delete('/delete_by_id/')
async def delete_pedido(item_id: int, db: Session = Depends(get_db), current_user: UserBaseModel = Depends(get_current_user)):
    pedido = CrudItems.delete_pedido(item_id, db)
    return pedido



