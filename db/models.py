from db.database import Base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Boolean, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

# MODELO DE DEFINICION DE LA TABLA DE LA BASE DE DATOS
#  es la estructura de la tabla

#  INFORMACIÓN NECESARIA PARA UN USUARIO


class DbUser(Base):
    #  nombre de la tabla
    __tablename__ = "users"

    # columnas de la tabla
    # primary_key es como el id y index es como el autoincrement que es un valor unico
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    hashed_password = Column(String)
    email = Column(String)

    items = relationship("DbItem", back_populates="user")
    extra_info = relationship(
        "DbInfoPersonal", uselist=False, back_populates="user")
    pedido = relationship("DbPedido", back_populates="user")

#   INFORMACIÓN  EXTTRA DEL USUARIO


class DbInfoPersonal(Base):
    __tablename__ = "info_personal"

    nombre_completo = Column(String)
    telefono = Column(Integer)
    direccion = Column(String)
    saldo = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    user = relationship("DbUser", back_populates="extra_info")


class DbItem(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    masa = Column(String)
    salsa = Column(String)
    tecnica = Column(String)
    presentacion = Column(String)
    maridaje = Column(String)

    # Define las relaciones con las tablas Ingredient y Extra
    ingredientes = relationship("Ingredient", back_populates="item")
    extras = relationship("Extra", back_populates="item")

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("DbUser", back_populates="items")


class Ingredient(Base):
    __tablename__ = "ingredients"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    item_id = Column(Integer, ForeignKey('items.id'))
    item = relationship("DbItem", back_populates="ingredientes")


class Extra(Base):
    __tablename__ = "extras"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    item_id = Column(Integer, ForeignKey('items.id'))
    item = relationship("DbItem", back_populates="extras")


class DbArticulo(Base):
    __tablename__ = "articulos"

    id_articulo = Column(Integer, primary_key=True)
    descripcion = Column(String)
    precio = Column(Integer)

    familia = relationship("Familia", back_populates="articulos")
    familia_id = Column(Integer, ForeignKey("familias.id_familia"))

    tipo = Column(String)

    pedidos = relationship("DbPedido", back_populates="articulo")


class DbPedido(Base):
    __tablename__ = "pedidos"

    id_registro = Column(Integer, primary_key=True)

    id_pedido = Column(Integer)

    id_user = Column(Integer, ForeignKey("users.id"))
    user = relationship("DbUser", back_populates="pedido")

    articulo = relationship("DbArticulo")
    id_articulo = Column(Integer, ForeignKey("articulos.id_articulo"))

    cantidad = Column(Integer)

    total = Column(Integer)

    menu = Column(Integer)


class Familia(Base):
    __tablename__ = "familias"

    id_familia = Column(Integer, primary_key=True)
    descripcion = Column(String)

    articulos = relationship("DbArticulo", back_populates="familia")
