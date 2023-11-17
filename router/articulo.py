from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db


from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from schemas import Articulo, ArticuloDisplayModel

from db.models import DbArticulo
from typing import List
from fastapi.responses import HTMLResponse

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
        DbArticulo(descripcion="Pizza Margherita",
                   precio=6, familia_id=1, tipo="a"),
        DbArticulo(descripcion="Pizza Pepperoni",
                   precio=7, familia_id=1, tipo="a"),
        DbArticulo(descripcion="Pizza Vegetariana",
                   precio=9, familia_id=1, tipo="a"),
        DbArticulo(descripcion="Pizza Cuatro Quesos",
                   precio=11, familia_id=1, tipo="a"),
        DbArticulo(descripcion="Pizza BBQ", precio=12, familia_id=1, tipo="a"),
        DbArticulo(descripcion="Pizza Pollo",
                   precio=12, familia_id=1, tipo="a"),
        DbArticulo(descripcion="Pizza Hawaiana",
                   precio=12, familia_id=1, tipo="a"),
        DbArticulo(descripcion="Pizza Carbonara",
                   precio=12, familia_id=1, tipo="a"),
    ]

    # Bebidas
    bebidas = [
        DbArticulo(descripcion="Agua Mineral",
                   precio=2, familia_id=2, tipo="a"),
        DbArticulo(descripcion="Coca Cola",
                   precio=2.5, familia_id=2, tipo="a"),
        DbArticulo(descripcion="Sprite", precio=2.5, familia_id=2, tipo="a"),
        DbArticulo(descripcion="Fanta", precio=2.5, familia_id=2, tipo="a"),
    ]

    # Postres
    postres = [
        DbArticulo(descripcion="Helado de Vainilla",
                   precio=5, familia_id=3, tipo="a"),
        DbArticulo(descripcion="Tarta de Manzana",
                   precio=6, familia_id=3, tipo="a"),
        DbArticulo(descripcion="Brownie", precio=4.5, familia_id=3, tipo="a"),
        DbArticulo(descripcion="Tiramisú", precio=6, familia_id=3, tipo="a"),
    ]

    menu = DbArticulo(descripcion="Menu", precio=10, familia_id=4, tipo="m")

    personalizar = DbArticulo(
        descripcion="Personalizar Pizza", precio=10, familia_id=5, tipo="p")

    # Añadir todos los artículos a la base de datos
    db.add_all(pizzas + bebidas + postres)
    db.add(menu)
    db.add(personalizar)

    # Realizar commit en la base de datos
    db.commit()

    return {"message": "Articulos creados"}


@router.get('/all', response_model=List[ArticuloDisplayModel], response_class=HTMLResponse)
async def get_articulos(request: Request, db: Session = Depends(get_db)):
    articulos = db.query(DbArticulo).all()
    return templates.TemplateResponse("articulos.html", {"request": request, "articulos": articulos})


@router.get('/menu', response_model=List[ArticuloDisplayModel], response_class=HTMLResponse)
async def get_menu(request: Request, db: Session = Depends(get_db)):
    articulos = db.query(DbArticulo).all()
    return templates.TemplateResponse("menu_pizza.html", {"request": request, "articulos": articulos})
