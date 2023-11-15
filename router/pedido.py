from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db


from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from schemas import Pedido, PedidoDisplayModel

from db.models import DbPedido

from typing import List




router = APIRouter(
    prefix='/pedidos',
    tags=['Pedidos']
)

router.mount("/static/css/", StaticFiles(directory="static/css"), name="static")

router.mount("/templates", StaticFiles(directory="templates"),name="templates")
templates = Jinja2Templates(directory="templates")


