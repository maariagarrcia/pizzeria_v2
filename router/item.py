from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from sqlalchemy.orm import Session
from db.database import get_db

from schemas import PedidoBaseModel, PedidoDisplayModel,ItemDisplayModel, Item


from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from pydantic import BaseModel
from typing import Optional

from db.models import  DbItem, Ingredient, Extra


router = APIRouter(
    prefix='/item',
    tags=['Items']
)

router.mount("/static/css/", StaticFiles(directory="static/css"), name="static")
router.mount("/templates", StaticFiles(directory="templates"), name="templates")
templates = Jinja2Templates(directory="templates")


@router.post("/post")
async def create_item(item: Item):
    item_dict = item.model_dump()
    return item_dict

@router.get('/crear')
async def mostrar_pedido(request: Request):
    return templates.TemplateResponse("pizza_personalizada.html", {"request": request})

@router.post('/submit', response_model=ItemDisplayModel)
async def create_pedido(request: Item, db: Session = Depends(get_db)):
    # Asegúrate de que request.ingredientes y request.extras sean listas vacías en lugar de listas vacías
    if not request.ingredientes:
        request.ingredientes = []
    if not request.extras:
        request.extras = []

    # Crea un nuevo ítem en la tabla "items"
    new_pedido = DbItem(
        masa=request.masa,
        salsa=request.salsa,
        tecnica=request.tecnica,
        presentacion=request.presentacion,
        maridaje=request.maridaje
    )

    # Agrega ingredientes relacionados
    for ingrediente_name in request.ingredientes:
        ingrediente = Ingredient(name=ingrediente_name)
        new_pedido.ingredientes.append(ingrediente)

    # Agrega extras relacionados
    for extra_name in request.extras:
        extra = Extra(name=extra_name)
        new_pedido.extras.append(extra)

    # Guarda el nuevo pedido en la base de datos
    db.add(new_pedido)
    db.commit()
    db.refresh(new_pedido)

    # Crea un diccionario con los datos del nuevo pedido
    new_pedido_dict = {
        "masa": new_pedido.masa,
        "salsa": new_pedido.salsa,
        "ingredientes": [ingrediente.name for ingrediente in new_pedido.ingredientes],
        "extras": [extra.name for extra in new_pedido.extras],
        "tecnica": new_pedido.tecnica,
        "presentacion": new_pedido.presentacion,
        "maridaje": new_pedido.maridaje
    }

    # Devuelve el diccionario como respuesta
    return new_pedido_dict
