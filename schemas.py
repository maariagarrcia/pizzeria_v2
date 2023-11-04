from pydantic import BaseModel, constr
from typing import List, Union, ClassVar
import datetime
import random


class PedidoModel(BaseModel):
    masa:str
    salsa:str
    ingredientes: List[str] = []
    extras: List[str] = []
    tecnica: str 
    presentacion: str 
    maridaje: str    
    precio: int = random.randint(1, 100)
    hora: ClassVar[datetime.datetime] = datetime.datetime.now()

    class Config():
        orm_mode = True


class UserBaseModel(BaseModel):
    username: str
    email: str
    hashed_password: str


class UserDisplayModel(BaseModel):
    username: str
    email: str
    items: List[PedidoModel] = []

    class Config():
        orm_mode = True

#  ------------------------------------------------------------


class User(BaseModel):
    id: int
    username: str

    class Config():
        orm_mode = True


class PedidoBaseModel(BaseModel):
    masa:str
    salsa:str
    ingredientes: List[str] = []
    extras: List[str] = []
    tecnica: str 
    presentacion: str 
    maridaje: str
    precio: int = random.randint(1, 100)
    hora: ClassVar[datetime.datetime] = datetime.datetime.now()
    creator_id: int


class PedidoDisplayModel(BaseModel):
    masa:str
    salsa:str
    ingredientes: List[str] = []
    extras: List[str] = []
    tecnica: str 
    presentacion: str 
    maridaje: str
    precio: int
    hora: ClassVar[datetime.datetime]
    user: User

    class Config():
        orm_mode = True


# ------------------------------------------------------------
class User2(BaseModel):
    id: int
    username: str

    class Config():
        orm_mode = True


class InfoBaseModel(BaseModel):
    nombre_completo: str
    telefono: int
    direccion: str
    saldo: int
    creator_id: int


class InfoDisplayModel(BaseModel):
    nombre_completo: str
    telefono: int
    direccion: str
    saldo: int
    user: User2

    class Config():
        orm_mode = True

