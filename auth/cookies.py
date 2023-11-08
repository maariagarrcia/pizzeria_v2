
from fastapi import Cookie, Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Request
import random


# -- COOKIES: Eliminar
@app.get("/cookie/delete/")
async def cookie_delete():
    response = JSONResponse(content="He eliminado la cookie ...")
    response.delete_cookie(key="dato_secreto")
    response.delete_cookie(key="dato_secreto_2")
    response.delete_cookie(key="dato_que_caduca")
    return response

# -- COOKIES: Crear o modificar

@app.get("/cookie/set/")
async def cookie_set():
    response = JSONResponse(
        content="Ahora tu ordenador tiene dos galletas más ...")
    response.set_cookie(key="dato_secreto", value="Me gusta la cocacola...")
    response.set_cookie(key="dato_secreto_2", value="con ron!")
    return response

# -- COOKIES: Recuperar

@app.get("/cookie/get/")
async def cookie_get(dato_secreto: str = Cookie(None), dato_secreto_2: str = Cookie(None)):
    return ("Tu dato secreto es: ", str(dato_secreto), str(dato_secreto_2))


@app.get("/cookie/get/expires/")
async def cookie_get_expires(dato_que_caduca: str = Cookie(None)):
    return ("Tu dato que caduca es ", dato_que_caduca)

# -- COOKIES: Fijar caducidad


@app.get("/cookie/set/expires/")
async def cookie_set_expires():
    response = JSONResponse(
        content="Ahora tu ordenador tiene una cookie que expira en 10 segundos ...")
    response.set_cookie(
        key='dato_que_caduca',
        value='como un suspiro...',
        max_age=10,     # Solo caduca.
        expires=10      # Caduca y elimina.
    )
    return response


# -- AUTENTICACION: Modo HTTP basico -> usuario y contraseña
def create_session(user_id: int):  # Creando sesión a lo cutre
    session_id = len(sessions) + random.randint(0, 1000000)
    sessions[session_id] = user_id
    return session_id

