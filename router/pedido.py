
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from sqlalchemy.orm import Session
from db.database import get_db

from schemas import PedidoBaseModel, PedidoDisplayModel

from db import db_pedidos

router = APIRouter(
    prefix='/pedido',
    tags=['Pedidos']
)

@router.post('/', response_model=PedidoDisplayModel)
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
