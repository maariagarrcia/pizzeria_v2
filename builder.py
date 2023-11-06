
# Primer paso es crear el  patron builder para crear una pizza dps ya  haremos  
# modificaciones 

# Tipo de masa: Variedades premium desde masas delgadas hasta masas fermentadas por 48 horas, con opciones de ingredientes especiales.
# Salsa base: Desde salsas clásicas hasta salsas de autor, incluyendo opciones veganas y de edición limitada.
# Ingredientes principales: Una gama que abarca desde ingredientes locales hasta importados de especialidad, todos categorizados por su origen, tipo y rareza.
# Técnicas de cocción: Diversidad que abarca desde hornos tradicionales hasta técnicas modernas de cocina molecular.
# Presentación: Opciones que van desde estilos clásicos hasta presentaciones que son verdaderas obras de arte.
# Maridajes recomendados: Una base de datos con cientos de opciones de vinos, cervezas y cocteles, con recomendaciones basadas en las elecciones de los ingredientes de la pizza.
# Extras y finalizaciones: Desde bordes especiales hasta acabados con ingredientes gourmet como trufas y caviar.


from typing import List, Optional
from pydantic import BaseModel

from sqlalchemy.orm import Session
from db.models import DbItem, Ingredient, Extra, DbUser

class ItemBuilder:
    def __init__(self, id: int, db: Session):
        self.item = db.query(DbItem).filter(DbItem.id == id).first()
        self.db = db

    def get_property(self, property_name):
        if self.item:
            property_value = getattr(self.item, property_name)
            if property_value:
                return property_value.name
        return None

    def build(self):
        return self.item

    def get_masa(self):
        if self.item:
            self.item.masa = self.get_property("masa")
        return self.item.masa
    
    def get_salsa(self):
        if self.item:
            self.item.salsa = self.get_property("salsa")
        return self.item.salsa
    
    def get_tecnica(self):
        if self.item:
            self.item.tecnica = self.get_property("tecnica")
        return self.item.tecnica
    
    def get_presentacion(self):
        if self.item:
            self.item.presentacion = self.get_property("presentacion")
        return self.item.presentacion
    
    def get_maridaje(self):
        if self.item:
            self.item.maridaje = self.get_property("maridaje")
        return self.item.maridaje
    
    def get_ingredientes(self):
        if self.item:
            ingredientes = self.item.ingredientes
            self.item.ingredientes = [ingrediente.name if ingrediente else None for ingrediente in ingredientes]
        return self.item.ingredientes
    
    def get_extras(self):
        if self.item:
            extras = self.item.extras
            self.item.extras = [extra.name if extra else None for extra in extras]
        return self.item.extras


    def get_user(self):
        if self.item:
            self.item.user = self.db.query(DbUser).filter(DbUser.id == self.item.user_id).first()
        return self.item.user
