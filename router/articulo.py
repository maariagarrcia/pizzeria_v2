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

from db import  db_articulo
from db.db_articulo import CrudArticulos

from db import  db_familia
from db.db_familia import CrudFamilias


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
    CrudArticulos.create_articulo(db=db)
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
