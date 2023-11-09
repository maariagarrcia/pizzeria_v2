
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
from sqlalchemy.orm import joinedload



class ItemBuilder:
    def __init__(self, item_id: int, db: Session):
        # Realiza la consulta a la base de datos y almacena el elemento (DbItem) en self.item
        self.item = db.query(DbItem).filter(DbItem.id == item_id).first()
        self.db = db
        self.pizza = None

    def get_masa(self):
        if self.item:
            # Suponiendo que el elemento DbItem tiene un atributo "masa"
            return self.item.masa
        return None

    def get_salsa(self):
        if self.item:
            # Suponiendo que el elemento DbItem tiene un atributo "salsa"
            return self.item.salsa
        return None

    def get_tecnica(self):
        if self.item:
            # Suponiendo que el elemento DbItem tiene un atributo "tecnica"
            return self.item.tecnica
        return None

    def get_presentacion(self):
        if self.item:
            # Suponiendo que el elemento DbItem tiene un atributo "presentacion"
            return self.item.presentacion
        return None

    def get_maridaje(self):
        if self.item:
            # Suponiendo que el elemento DbItem tiene un atributo "maridaje"
            return self.item.maridaje
        return None

    def get_ingredientes(self):
       if self.item and self.item.ingredientes:
           # Recopila solo los nombres de los ingredientes
           ingredientes = [ingrediente.name for ingrediente in self.item.ingredientes]
           return ingredientes
       return None


    def get_extras(self):
        if self.item:
            # Suponiendo que el elemento DbItem tiene un atributo "extras"
            return self.item.extras
        return None

    def get_user(self):
        if self.item:
            # Suponiendo que el elemento DbItem tiene un atributo "user"
            return self.item.user
        return None


          
    def build(self):
        return self.item        
