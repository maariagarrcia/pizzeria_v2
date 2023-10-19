from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db import models
from db.database import engine

from router import user, pedido, extra_info

app = FastAPI()
app.include_router(user.router)
app.include_router(pedido.router)
app.include_router(extra_info.router)



@app.get("/")
async def root():
    return {"message": "Hello World"}


# SE CREA EL DABATASE
models.Base.metadata.create_all(engine)
