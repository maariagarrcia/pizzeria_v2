from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db


from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from schemas import Articulo, ArticuloDisplayModel

from db.models import DbArticulo
from typing import List

from fastapi import FastAPI, Request, status
import logging


router = APIRouter(
    prefix='/articulo',
    tags=['Articulo']
)

router.mount("/static/css/", StaticFiles(directory="static/css"), name="static")
router.mount("/templates", StaticFiles(directory="templates"),
             name="templates")
templates = Jinja2Templates(directory="templates")


@router.post('/submit', status_code=status.HTTP_201_CREATED)
async def create_articulos(request: Articulo, db: Session = Depends(get_db)):
    # Pizzas
    pizzas = [
        DbArticulo(descripcion="Pizza Margherita", precio=6, familia_id=1),
        DbArticulo(descripcion="Pizza Pepperoni", precio=7, familia_id=1),
        DbArticulo(descripcion="Pizza Vegetariana", precio=9, familia_id=1),
        DbArticulo(descripcion="Pizza Cuatro Quesos", precio=11, familia_id=1),
        DbArticulo(descripcion="Pizza BBQ", precio=12, familia_id=1),
        DbArticulo(descripcion="Pizza Mexicana", precio=12, familia_id=1),
    ]

    # Bebidas
    bebidas = [
        DbArticulo(descripcion="Agua Mineral", precio=2, familia_id=2),
        DbArticulo(descripcion="Coca Cola", precio=2.5, familia_id=2),
        DbArticulo(descripcion="Sprite", precio=2.5, familia_id=2),
    ]

    # Postres
    postres = [
        DbArticulo(descripcion="Helado de Vainilla", precio=5, familia_id=3),
        DbArticulo(descripcion="Tarta de Manzana", precio=6, familia_id=3),
        DbArticulo(descripcion="Brownie", precio=4.5, familia_id=3),
    ]

    # Añadir todos los artículos a la base de datos
    db.add_all(pizzas + bebidas + postres)

    # Realizar commit en la base de datos
    db.commit()

    return {"message": "Articulos creados"}
