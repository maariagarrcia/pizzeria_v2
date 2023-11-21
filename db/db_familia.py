
from abc import ABC, abstractmethod
from db.models import Familia


class CrudFamilias:
    @abstractmethod
    def create_familia(db):
        # create a new record in the database
        pass

class CrudFamilias:
    @staticmethod
    def create_familia(db):
        pizza = Familia(
            descripcion="Pizza"
        )
        bebida = Familia(
            descripcion="Bebida"
        )
    
        postre = Familia(
            descripcion="Postre"
        )
    
        menu = Familia(
            descripcion="Menu"
        )
    
        pizza_pers = Familia(
            descripcion="Pizza Personalizada"
        )
    
        db.add(pizza)
        db.add(bebida)
        db.add(postre)
        db.add(menu)
        db.add(pizza_pers)
