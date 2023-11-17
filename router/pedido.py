from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db


from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from schemas import Pedido, PedidoDisplayModel

from db.models import DbPedido

from typing import List

from schemas import User2, PedidoDisplayModel, Pedido, Articulo2





router = APIRouter(
    prefix='/pedido',
    tags=['Pedido']
)

router.mount("/static/css/", StaticFiles(directory="static/css"), name="static")

router.mount("/templates", StaticFiles(directory="templates"),name="templates")
templates = Jinja2Templates(directory="templates")


@router.post('/submit', response_model=PedidoDisplayModel)
async def submit_pedido(request: Pedido, db: Session = Depends(get_db)):
    new_pedido = DbPedido(
        id_pedido=request.id_pedido,
        id_user=request.id_user,
        id_articulo=request.id_articulo,
        cantidad=request.cantidad,
        total=request.total,
        menu=request.menu)

    db.add(new_pedido)
    db.commit()
    db.refresh(new_pedido)

    user = User2(id=request.id_user, username=" ")
    articulo = Articulo2(id=request.id_articulo, descripcion=" ",tipo="", precio=0)
    
    new_pedido_dict = PedidoDisplayModel(
        id_pedido=new_pedido.id_pedido,
        id_user=user,
        id_articulo=articulo,
        cantidad=new_pedido.cantidad,
        total=new_pedido.total,
        menu=new_pedido.menu
    )
    print(f"Pedido creado con ID: {new_pedido.id_pedido}")
    return new_pedido_dict

