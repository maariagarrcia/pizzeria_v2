from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db import models
from db.database import engine

from router import user, pedido, extra_info
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from pydantic import BaseModel


app = FastAPI()
app.include_router(user.router)
app.include_router(pedido.router)
app.include_router(extra_info.router)


app.mount("/static/css/", StaticFiles(directory="static/css"), name="static")
app.mount("/templates", StaticFiles(directory="templates"), name="templates")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root():
    return {"message": "Hello World"}


# SE CREA EL DABATASE
models.Base.metadata.create_all(engine)
