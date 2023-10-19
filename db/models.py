from db.database import Base
from sqlalchemy import  Column
from sqlalchemy.sql.sqltypes import Boolean, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


# MODELO DE DEFINICION DE LA TABLA DE LA BASE DE DATOS
# es la estructura de la tabla 

# INFORMACIÓN NECESARIA PARA UN USUARIO
class DbUser(Base):
    # nombre de la tabla
    __tablename__ = "users"

    # columnas de la tabla
    # primary_key es como el id y index es como el autoincrement que es un valor unico
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    hashed_password = Column(String)
    email = Column(String)
    items = relationship("DbPedido", back_populates="user")
    extra_info = relationship("DbInfoPersonal", uselist=False, back_populates="user")

#  INFORMACIÓN  EXTTRA DEL USUARIO
class DbInfoPersonal(Base):
    __tablename__ = "info_personal"

    nombre_completo = Column(String)
    telefono = Column(Integer)
    direccion = Column(String)
    saldo = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    user = relationship("DbUser", back_populates="extra_info")


# INFORMACIÓN DE LOS PEDIDOS
class DbPedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)
    pizza = Column(String)
    alergias = Column(String)
    precio= Column(Integer)
    hora = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("DbUser", back_populates="items")
