
from abc import ABC, abstractmethod
from db.models import DbArticulo



class CrudArticulos:
    @abstractmethod
    def create_articulo(db):
        # create a new record in the database
        pass

class CrudArticulos:
    @staticmethod
    def create_articulo(db):
        pizzas = [
            DbArticulo(descripcion="Pizza Margherita",
                       precio=6, familia_id=1, tipo="a"),
            DbArticulo(descripcion="Pizza Pepperoni",
                       precio=7, familia_id=1, tipo="a"),
            DbArticulo(descripcion="Pizza Vegetariana",
                       precio=9, familia_id=1, tipo="a"),
            DbArticulo(descripcion="Pizza Cuatro Quesos",
                       precio=11, familia_id=1, tipo="a"),
            DbArticulo(descripcion="Pizza BBQ", precio=12, familia_id=1, tipo="a"),
            DbArticulo(descripcion="Pizza Pollo",
                       precio=12, familia_id=1, tipo="a"),
            DbArticulo(descripcion="Pizza Hawaiana",
                       precio=12, familia_id=1, tipo="a"),
            DbArticulo(descripcion="Pizza Carbonara",
                   precio=12, familia_id=1, tipo="a")]

        # Bebidas
        bebidas = [
            DbArticulo(descripcion="Agua Mineral",
                       precio=2, familia_id=2, tipo="a"),
            DbArticulo(descripcion="Coca Cola",
                       precio=2.5, familia_id=2, tipo="a"),
            DbArticulo(descripcion="Sprite", precio=2.5, familia_id=2, tipo="a"),
            DbArticulo(descripcion="Fanta", precio=2.5, familia_id=2, tipo="a"),
        ]

        # Postres
        postres = [
            DbArticulo(descripcion="Helado de Vainilla",
                       precio=5, familia_id=3, tipo="a"),
            DbArticulo(descripcion="Tarta de Manzana",
                       precio=6, familia_id=3, tipo="a"),
            DbArticulo(descripcion="Brownie", precio=4.5, familia_id=3, tipo="a"),
            DbArticulo(descripcion="Tiramisú", precio=6, familia_id=3, tipo="a"),
        ]

        menu = DbArticulo(descripcion="Menu", precio=10, familia_id=4, tipo="m")

        personalizar = DbArticulo(
            descripcion="Personalizar Pizza", precio=10, familia_id=5, tipo="p")

        # Añadir todos los artículos a la base de datos
        db.add_all(pizzas + bebidas + postres)
        db.add(menu)
        db.add(personalizar)


