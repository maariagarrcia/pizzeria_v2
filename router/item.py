from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from sqlalchemy.orm import Session
from db.database import get_db

from schemas import ItemDisplayModel, Item
from auth.oauth2 import oauth2_scheme, get_current_user


from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from pydantic import BaseModel
from typing import Optional

from db import db_user
from schemas import UserBaseModel, UserDisplayModel, ItemDisplayModel, ItemModel, Item, User

from db.models import  DbItem, Ingredient, Extra
from builder import ItemBuilder  # Asegúrate de importar ItemBuilder desde el módulo adecuado


router = APIRouter(
    prefix='/item',
    tags=['Items']
)

router.mount("/static/css/", StaticFiles(directory="static/css"), name="static")
router.mount("/templates", StaticFiles(directory="templates"), name="templates")
templates = Jinja2Templates(directory="templates")




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
        maridaje=request.maridaje,
        user_id = request.creator_id
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
        "maridaje": new_pedido.maridaje,
        "user": {
            "id": new_pedido.user.id,
            "username": new_pedido.user.username
        }
    }

    # Devuelve el diccionario como respuesta
    return new_pedido_dict



@router.get('/{items_id}')
async def get_pedido(items_id: int, db: Session = Depends(get_db),current_user:UserBaseModel =Depends(get_current_user)):
    # Crear un ItemBuilder y configurarlo con el id y la sesión de la base de datos
    item_builder = ItemBuilder(items_id, db)
    
    # Recuperar los detalles de la pizza desde la base de datos
    item_builder.get_masa()
    item_builder.get_salsa()
    item_builder.get_tecnica()
    item_builder.get_presentacion()
    item_builder.get_maridaje()
    item_builder.get_ingredientes()
    item_builder.get_extras()
    item_builder.get_user()
   
    # Construir el objeto de pizza con los detalles recuperados
    pizza = item_builder.build()

    if not pizza:
        raise HTTPException(status_code=404, detail="Item not found")

    # Devolver la pizza como respuesta
    return pizza

    