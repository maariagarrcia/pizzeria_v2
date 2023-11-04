
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from sqlalchemy.orm import Session
from db.database import get_db

from schemas import PedidoBaseModel, PedidoDisplayModel,ItemDisplayModel, Item

from db import db_pedidos

from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from pydantic import BaseModel


router = APIRouter(
    prefix='/pedido',
    tags=['Pedidos']
)

router.mount("/static/css/", StaticFiles(directory="static/css"), name="static")
router.mount("/templates", StaticFiles(directory="templates"), name="templates")
templates = Jinja2Templates(directory="templates")

# ----------------- Ejemplo de uso de Pydantic -----------------


@router.post("/post")
async def create_item(item: Item):
    item_dict = item.model_dump()
    return item_dict


#-----------------------------------------------------------------

@router.get('/crear')
async def mostrar_pedido(request: Request):
    return templates.TemplateResponse("pizza_personalizada.html", {"request": request})

@router.post('/submit', response_model=PedidoDisplayModel)
async def create_pedido(request: PedidoBaseModel, db: Session = Depends(get_db)):
    new_pedido= db_pedidos.CrudPedidos.create_pedido(db, request)
    return new_pedido

@router.get('/', response_model=List[PedidoDisplayModel])
async def get_all_pedidos(db: Session = Depends(get_db)):
    return db_pedidos.CrudPedidos.get_all(db)

@router.get('/{id}')
async def get_pedido_by_id(id: int, db: Session = Depends(get_db)):
    return db_pedidos.CrudPedidos.get_pedido_by_id(id, db)

@router.put('/{id}', response_model=PedidoDisplayModel)
async def update_pedido(id: int, request: PedidoBaseModel, db: Session = Depends(get_db)):
    return db_pedidos.CrudPedidos.update_pedido(id,db,request)

@router.delete('/{id}/delete')
async def delete_pedido(id: int, db: Session = Depends(get_db)):
    return db_pedidos.CrudPedidos.delete_pedido(id, db)

