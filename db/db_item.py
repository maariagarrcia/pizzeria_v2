from sqlalchemy.orm.session import Session
from db.models import DbItem
from fastapi import HTTPException
from schemas import ItemDisplayModel,Item
from starlette import status

from abc import ABC, abstractmethod

class CrudItemsInterfaz:
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

class CrudItems(CrudItemsInterfaz):
    @staticmethod
    def create_pedido(db:Session, request:Item):
        new_pedido = DbItem(
            masa = request.masa,
            salsa = request.salsa,
            ingredientes = request.ingredientes,
            extras = request.extras,
            tecnica = request.tecnica,
            presentacion = request.presentacion,
            maridaje = request.maridaje,
            user_id = request.creator_id
            )
        
        db.add(new_pedido)
        db.commit()
        db.refresh(new_pedido)

        return new_pedido
    
    @staticmethod
    def get_all(db:Session):
        pedidos = db.query(DbItem).all()
        return pedidos
    
    @staticmethod
    def get_pedido_by_id(id:int, db:Session):
        pedido = db.query(DbItem).filter(DbItem.id == id).first()
        if not pedido:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND4, detail="Pedido no encontrado")
        return pedido
    
    @staticmethod
    def update_pedido(id:int,db:Session,request:Item):
        pedido = db.query(DbItem).filter(DbItem.id == id).first()

        if pedido:
            pedido.pizza = request.pizza
            pedido.alergias = request.alergias
            db.commit()
            db.refresh(pedido)
            return ItemDisplayModel(
                id = pedido.id,
                masa = pedido.masa,
                salsa = pedido.salsa,
                ingredientes = pedido.ingredientes,
                extras = pedido.extras,
                tecnica = pedido.tecnica,
                presentacion = pedido.presentacion,
                maridaje = pedido.maridaje,
            )
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    
    @staticmethod
    def delete_pedido(id:int,db:Session):
        pedido = db.query(DbItem).filter(DbItem.id == id).first()
        if not pedido:

            raise HTTPException(status_code=404, detail="Pedido no encontrado")
        db.delete(pedido)
        db.commit()
        return pedido