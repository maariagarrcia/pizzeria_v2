from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db


from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from schemas import Articulo, ArticuloDisplayModel

from db.models import Familia
from typing import List

from fastapi import FastAPI, Request, status
import logging


router = APIRouter(
    prefix='/familia',
    tags=['Familia']
)

router.mount("/static/css/", StaticFiles(directory="static/css"), name="static")
router.mount("/templates", StaticFiles(directory="templates"),
             name="templates")
templates = Jinja2Templates(directory="templates")


@router.post('/submit', status_code=status.HTTP_201_CREATED)
async def create_familia(db: Session = Depends(get_db)):
    pizza=Familia(
        descripcion="Pizza"
    )
    bebida=Familia(
        descripcion="Bebida"
    )

    postre=Familia(
        descripcion="Postre"
    )

    db.add(pizza)
    db.add(bebida)
    db.add(postre)
    db.commit()


    return {"message": "Articulos creados"}

