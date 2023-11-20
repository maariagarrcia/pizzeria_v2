# Permite crear un backend de una aplicación web
from pydantic import BaseModel  # Para crear/validar tipos de datos complejos
from abc import ABC, abstractmethod  # Para crear clases abstractas
from typing import List

#
# Clases de datos (DTO) pydantic y enumerables
#

class Articulo(BaseModel):
    id_articulo: int
    tipo_articulo: str
    descripcion: str
    pvp: float


class LineasPedido(BaseModel):
    articulo: Articulo
    cantidad: int
    pvp: float


class Pedido(BaseModel):
    id_pedido: int
    id_user: int
    pvp: float
    lineas_pedido: list[LineasPedido]


from typing import List

from pydantic import BaseModel

class Componente(BaseModel):
    """
    Clase base para el patrón Composite
    """
    def get_pvp(self) -> float:
        """
        Método para obtener el precio total del componente
        """
        pass

    def obtener_detalles(self) -> str:
        """
        Método para obtener detalles específicos del componente
        """
        pass

class Articulo(Componente):
    id_articulo: int
    tipo_articulo: str
    descripcion: str
    pvp: float

    def get_pvp(self) -> float:
        return self.pvp

    def obtener_detalles(self) -> str:
        return f"{self.descripcion} - ${self.pvp}"

class LineasPedido(Componente):
    articulo: Articulo
    cantidad: int

    def get_pvp(self) -> float:
        return self.articulo.get_pvp() * self.cantidad

    def obtener_detalles(self) -> str:
        return f"{self.cantidad} x {self.articulo.obtener_detalles()}"

class Pedido(Componente):
    id_pedido: int
    id_user: int
    pvp: float
    lineas_pedido: List[LineasPedido]

    def get_pvp(self) -> float:
        return sum(linea.get_pvp() for linea in self.lineas_pedido)

    def obtener_detalles(self) -> str:
        detalles_lineas = "\n".join(linea.obtener_detalles() for linea in self.lineas_pedido)
        return f"Detalles del Pedido (ID: {self.id_pedido}, Usuario ID: {self.id_user}):\n{detalles_lineas}\nPrecio Total: ${self.get_pvp()}"

# Ejemplo de uso
#if __name__ == "__main__":
#    # Crear artículos
#    pizza_margarita = Articulo(id_articulo=1, tipo_articulo="p", descripcion="Margarita", pvp=10.0)
#    pizza_hawaiana = Articulo(id_articulo=2, tipo_articulo="p", descripcion="Hawaiana", pvp=12.0)#

#    refresco = Articulo(id_articulo=3, tipo_articulo="b", descripcion="Refresco", pvp=2.5)#

#    postre = Articulo(id_articulo=4, tipo_articulo="p", descripcion="Helado de vainilla", pvp=7.5)#

#    # Crear líneas de pedido
#    linea1 = LineasPedido(articulo=pizza_margarita, cantidad=2)
#    linea2 = LineasPedido(articulo=postre, cantidad=1)
#    linea3 = LineasPedido(articulo=refresco, cantidad=3)#

#    # Crear pedido compuesto
#    pedido_compuesto = Pedido(id_pedido=1, id_user=1, pvp=0.0, lineas_pedido=[linea1, linea2, linea3])#

#    pedido_simple = Pedido(id_pedido=2, id_user=2, pvp=0.0, lineas_pedido=[linea1])#

#    # Obtener el precio total del pedido
#    total_pedido = pedido_compuesto.get_pvp()
#    total_pedido2 = pedido_simple.get_pvp()#

#    # Obtener detalles del pedido
#    detalles_pedido = pedido_compuesto.obtener_detalles()
#    detalles_pedido2 = pedido_simple.obtener_detalles()#

#    print(f"El precio total del pedido es: ${total_pedido}")
#    print(detalles_pedido)#

#    print(f"\nEl precio total del pedido es: ${total_pedido2}")
#    print(detalles_pedido2)
