from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db import models
from db.database import engine

from router import user, extra_info, item,articulo,pedido,familia
from auth import authentication

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from pydantic import BaseModel

from pathlib import Path
import uvicorn

from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse

from fastapi import status
from fastapi.responses import HTMLResponse

from db.database import SessionLocal, engine
from db import models
from db.models import DbArticulo
from db.db_articulo import CrudArticulos
from db.db_familia import CrudFamilias

app = FastAPI()
app.include_router(familia.router)
app.include_router(pedido.router)
app.include_router(articulo.router)
app.include_router(authentication.router)                                               
app.include_router(item.router)
app.include_router(user.router)
app.include_router(extra_info.router)


# -- SERVIR ARCHIVOS HTML ESTATICOS


app.mount("/static/images/", StaticFiles(directory="static/images"), name="static")
app.mount("/static/images/pizzas/", StaticFiles(directory="static/images/pizzas"), name="static")
app.mount("/static/css/", StaticFiles(directory="static/css"), name="static")

app.mount("/templates", StaticFiles(directory="templates"), name="templates")
app.mount("/templates/pizza_personalizada", StaticFiles(directory="templates/pizza_personalizada"), name="templates")
app.mount("/templates/pedidos", StaticFiles(directory="templates/pedidos"), name="templates")

templates = Jinja2Templates(directory="templates")


# -- REDIRECCIONES: index.html pasa a ser archivo por defecto de la ruta
@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})

startup_event_executed = False


def startup_event():
    """Evento de inicio de la aplicación
    """

    global startup_event_executed

    # Crea una sesión de la base de datos
    db = SessionLocal()

    # Ejecuta la lógica de creación inicial de artículos
    CrudArticulos.create_articulo(db)
    CrudFamilias.create_familia(db)

    # Confirma los cambios en la base de datos
    db.commit()

    # Cierra la sesión de la base de datos
    db.close()

    # Marca el evento de inicio como ejecutado
    startup_event_executed = True


    

# SE CREA EL DABATASE

models.Base.metadata.create_all(engine)

if __name__ == "__main__":
    print("-> Inicio integrado de servicIo web")
    uvicorn.run(app, host="127.0.0.1", port=8000)
else:
    print("=> Iniciado desde el servidor web")
    print("   Módulo python iniciado:", __name__)

