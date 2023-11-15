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

class Familia(BaseModel):
    id: int

    class Config():
        orm_mode = True


class Articulo(BaseModel):
    descripcion: str
    precio: int
    familia_id: int
   
class ArticuloDisplayModel(BaseModel):
    descripcion: str
    precio: int
    familia_id: Familia

    class Config():
        orm_mode = True

# ------------------------------------------
class User3(BaseModel):
    id: int
    username: str

    class Config():
        orm_mode = True


class Pedido(BaseModel):
    cantidad: int
    total: int
    id_articulo: int
    id_user: int


class PedidoDisplayModel(BaseModel):
    cantidad: int
    total: int
    id_articulo: int
    id_user: User3

    class Config():
        orm_mode = True
  