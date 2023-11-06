from pydantic import BaseModel, constr
from typing import List, Union, ClassVar
import datetime
import random

class User(BaseModel):
    id: int
    username: str

    class Config():
        orm_mode = True


class Item(BaseModel):
    masa:str
    salsa:str
    ingredientes: List[str] = []
    extras: List[str] = []
    tecnica: str 
    presentacion: str 
    maridaje: str
    creator_id: int

class ItemDisplayModel(BaseModel):
    masa:str
    salsa:str
    ingredientes: List[str] = []
    extras: List[str] = []
    tecnica: str 
    presentacion: str 
    maridaje: str
    user:User

#-------------------------
class ItemModel(BaseModel):
    masa:str
    salsa:str
    ingredientes: List[str] = []
    extras: List[str] = []
    tecnica: str 
    presentacion: str 
    maridaje: str    

    class Config():
        orm_mode = True


class UserBaseModel(BaseModel):
    username: str
    email: str
    hashed_password: str


class UserDisplayModel(BaseModel):
    username: str
    email: str
    items: List[ItemModel] = []

    class Config():
        orm_mode = True

#  ------------------------------------------------------------

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


# ------------------------------------------