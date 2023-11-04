
# Primer paso es crear el  patron builder para crear una pizza dps ya  haremos  
# modificaciones 

# Tipo de masa: Variedades premium desde masas delgadas hasta masas fermentadas por 48 horas, con opciones de ingredientes especiales.
# Salsa base: Desde salsas clásicas hasta salsas de autor, incluyendo opciones veganas y de edición limitada.
# Ingredientes principales: Una gama que abarca desde ingredientes locales hasta importados de especialidad, todos categorizados por su origen, tipo y rareza.
# Técnicas de cocción: Diversidad que abarca desde hornos tradicionales hasta técnicas modernas de cocina molecular.
# Presentación: Opciones que van desde estilos clásicos hasta presentaciones que son verdaderas obras de arte.
# Maridajes recomendados: Una base de datos con cientos de opciones de vinos, cervezas y cocteles, con recomendaciones basadas en las elecciones de los ingredientes de la pizza.
# Extras y finalizaciones: Desde bordes especiales hasta acabados con ingredientes gourmet como trufas y caviar.

class Pizza:
    def __init__(self):
        self.masa_type = None
        self.sauce = None
        self.ingredients = []
        self.techniques = []
        self.presentation = None
        self.pairing = None  # maridaje
        self.extras = []

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_masa_type(self, masa_type):
        self.pizza.masa_type = masa_type
        return self

    def set_sauce(self, sauce):
        self.pizza.sauce = sauce
        return self

    def add_ingredient(self, ingredient):
        self.pizza.ingredients.append(ingredient)
        return self

    def set_technique(self, technique):
        self.pizza.techniques.append(technique)
        return self

    def set_presentation(self, presentation):
        self.pizza.presentation = presentation
        return self

    def set_pairing(self, pairing):  # maridaje
        self.pizza.pairing = pairing
        return self

    def add_extra(self, extra):
        self.pizza.extras.append(extra)
        return self

    def get_result(self) -> Pizza:
        return self.pizza


