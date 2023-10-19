from sqlalchemy.orm.session import Session
from db.models import DbPedido
from fastapi import HTTPException
from schemas import PedidoBaseModel, PedidoDisplayModel
from starlette import status

from abc import ABC, abstractmethod

class CrudPedidosInterfaz:
    @abstractmethod
    def create_pedido(self, data,request):
        # create a new record in the database
        pass

    @abstractmethod
    def get_all(self,data):
        # get all records from the database
        pass

    @abstractmethod
    def get_pedido_by_id(self, id, data):
        # get a record from the database
        pass

    @abstractmethod
    def update_pedido(self, id, data,request):
        # update a record in the database
        pass

    @abstractmethod
    def delete_pedido(self, id, data):
        # delete a record from the database
        pass


class CrudPedidos(CrudPedidosInterfaz):
    @staticmethod
    def create_pedido(db:Session, request:PedidoBaseModel):
        new_pedido = DbPedido(
            pizza = request.pizza,
            alergias = request.alergias,
            precio = request.precio,
            hora = request.hora,
            user_id = request.creator_id
            )
        db.add(new_pedido)
        db.commit()
        db.refresh(new_pedido)

        return new_pedido
    
    @staticmethod
    def get_all(db:Session):
        pedidos = db.query(DbPedido).all()
        return pedidos
    
    @staticmethod
    def get_pedido_by_id(id:int, db:Session):
        pedido = db.query(DbPedido).filter(DbPedido.id == id).first()
        if not pedido:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND4, detail="Pedido no encontrado")
        return pedido
    
    @staticmethod
    def update_pedido(id:int,db:Session,request:PedidoBaseModel):
        pedido = db.query(DbPedido).filter(DbPedido.id == id).first()

        if pedido:
            pedido.pizza = request.pizza
            pedido.alergias = request.alergias
            db.commit()
            db.refresh(pedido)
            return PedidoDisplayModel(
                id = pedido.id,
                pizza = pedido.pizza,
                alergias = pedido.alergias
            )
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    
    @staticmethod
    def delete_pedido(id:int,db:Session):
        pedido = db.query(DbPedido).filter(DbPedido.id == id).first()
        if not pedido:

            raise HTTPException(status_code=404, detail="Pedido no encontrado")
        db.delete(pedido)
        db.commit()
        return pedido