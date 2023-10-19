from abc import ABC, abstractmethod
from sqlalchemy.orm.session import Session
from fastapi import HTTPException
from schemas import InfoBaseModel
from db.models import DbInfoPersonal

# crud de  info personal

class CrudInfoInterfaz:
    @abstractmethod
    def create_info(self, data,request):
        # create a new record in the database
        pass


    @abstractmethod
    def update_info(self, id, data,request):
        # update a record in the database
        pass

    @abstractmethod
    def delete_info(self, id):
        # delete a record in the database
        pass

    


class CrudInfo(CrudInfoInterfaz):
    @staticmethod
    def create_info(db:Session, request:InfoBaseModel):
        new_info = DbInfoPersonal(
            nombre_completo = request.nombre_completo,
            telefono = request.telefono,
            direccion = request.direccion,
            saldo = request.saldo,
            user_id = request.creator_id
            )
        db.add(new_info)
        db.commit()
        db.refresh(new_info)

        return new_info
    
    @staticmethod
    def update_info(id:int, request:InfoBaseModel, db:Session):
        info = db.query(DbInfoPersonal).filter(DbInfoPersonal.user_id == id).first()
        if not info:
            raise HTTPException(status_code=404, detail="Info not found")
        info.nombre_completo = request.nombre_completo
        info.telefono = request.telefono
        info.direccion = request.direccion
        info.saldo = request.saldo
        db.commit()
        db.refresh(info)
        return info
    
    @staticmethod
    def delete_info(id:int, db:Session):
        info = db.query(DbInfoPersonal).filter(DbInfoPersonal.user_id == id).first()
        if not info:
            raise HTTPException(status_code=404, detail="Info not found")
        db.delete(info)
        db.commit()
        return info