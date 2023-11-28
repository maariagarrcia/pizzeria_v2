from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db


from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from schemas import Pedido, PedidoDisplayModel

from db.models import DbPedido

from typing import List

from schemas import User2, PedidoDisplayModel, Pedido, Articulo2

from composite import PedidoC, LineasPedido, Articulo

from fastapi import HTTPException

from fastapi.responses import HTMLResponse
from fastapi import Request


router = APIRouter(
    prefix='/pedido',
    tags=['Pedido']
)

router.mount("/static/images/",
             StaticFiles(directory="static/images"), name="static")
router.mount("/static/images/pizzas/",
             StaticFiles(directory="static/images/pizzas"), name="static")
router.mount("/static/css/", StaticFiles(directory="static/css"), name="static")
router
router.mount("/templates", StaticFiles(directory="templates"),
             name="templates")
router.mount("/templates/pizza_personalizada",
             StaticFiles(directory="templates/pizza_personalizada"), name="templates")
router.mount("/templates/pedidos",
             StaticFiles(directory="templates/pedidos"), name="templates")

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
    articulo = Articulo2(id=request.id_articulo,
                         descripcion=" ", tipo="", precio=0)

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


@router.get('/get_id/{pedido_id}')
async def get_pedido(request: Request, pedido_id: int, db: Session = Depends(get_db)):
    # Obtener el pedido y sus líneas de pedido de la base de datos
    db_pedido = db.query(DbPedido).filter(
        DbPedido.id_pedido == pedido_id).first()

    # Verificar si el pedido existe
    if not db_pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")

    # Si el pedido es una hoja (tipo 0), simplemente crea una línea de pedido
    if db_pedido.menu == 0:
        articulo = Articulo(
            id_articulo=db_pedido.articulo.id_articulo,
            tipo_articulo=db_pedido.articulo.tipo,
            descripcion=db_pedido.articulo.descripcion,
            pvp=db_pedido.articulo.precio
        )

        linea_pedido = LineasPedido(
            articulo=articulo, cantidad=db_pedido.cantidad
        )
        
        detalles_pedido = linea_pedido.obtener_detalles()
    else:
        # Si el pedido es una composición (tipo diferente de 0), crea un pedido compuesto
        pedido_compuesto = PedidoC(id_pedido=db_pedido.id_pedido,
                                   id_user=db_pedido.id_user, pvp=db_pedido.total, lineas_pedido=[])

        # Obtén todas las líneas de pedido asociadas al pedido
        db_lineas_pedido = db.query(DbPedido).filter(
            DbPedido.id_pedido == pedido_id).all()

        for db_linea_pedido in db_lineas_pedido:
            articulo = Articulo(
                id_articulo=db_linea_pedido.articulo.id_articulo,
                tipo_articulo=db_linea_pedido.articulo.tipo,
                descripcion=db_linea_pedido.articulo.descripcion,
                pvp=db_linea_pedido.articulo.precio
            )
            linea_pedido = LineasPedido(
                articulo=articulo, cantidad=db_linea_pedido.cantidad
            )
            pedido_compuesto.lineas_pedido.append(linea_pedido)

        # Obtener los detalles del pedido compuesto utilizando el patrón Composite
        detalles_pedido = pedido_compuesto.obtener_detalles()

    # Devuelve los detalles del pedido para mostrarlos en la página web
        return templates.TemplateResponse("pedidos/ver_pedido.html", {"request": request, "detalles_pedido": detalles_pedido,"pedido_compuesto":pedido_compuesto,"linea_pedido":linea_pedido,"articulo":articulo})
