from sqlalchemy.orm.session import Session
from db.models import DbItem
from fastapi import HTTPException
from schemas import ItemDisplayModel,Item
from builder import ItemBuilder
from abc import ABC, abstractmethod
from db.models import DbItem, Ingredient, Extra
from schemas import ItemDisplayModel, ItemModel, Item, UserBaseModel, UserDisplayModel
from schemas import UserBaseModel, UserDisplayModel, ItemDisplayModel, ItemModel, Item, User


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
        if not request.ingredientes:
            request.ingredientes = []
        if not request.extras:
            request.extras = []

        # Crea un nuevo ítem en la tabla "items"
        new_pedido = DbItem(
            masa=request.masa,
            salsa=request.salsa,
            tecnica=request.tecnica,
            presentacion=request.presentacion,
            maridaje=request.maridaje,
            user_id=request.creator_id
        )

        # Agrega ingredientes relacionados
        for ingrediente_name in request.ingredientes:
            ingrediente = Ingredient(name=ingrediente_name)
            new_pedido.ingredientes.append(ingrediente)

        # Agrega extras relacionados
        for extra_name in request.extras:
            extra = Extra(name=extra_name)
            new_pedido.extras.append(extra)

        # Guarda el nuevo pedido en la base de datos
        db.add(new_pedido)
        db.commit()
        db.refresh(new_pedido)


        userr = User(id=request.creator_id, username=" ")

        new_pedido_dict = ItemDisplayModel(
            masa=new_pedido.masa,
            salsa=new_pedido.salsa,
            ingredientes=[
                ingrediente.name for ingrediente in new_pedido.ingredientes],
            extras=[extra.name for extra in new_pedido.extras],
            tecnica=new_pedido.tecnica,
            presentacion=new_pedido.presentacion,
            maridaje=new_pedido.maridaje,
            user=userr
        )
        # Devuelve el diccionario como respuesta
        return new_pedido_dict    
    

    @staticmethod
    def get_pedido_by_id(items_id: int, db: Session):
        try:
            print(f"Buscando pedido con ID: {items_id}")

            item_builder = ItemBuilder(items_id, db)
            item_builder.get_masa()
            item_builder.get_salsa()
            item_builder.get_tecnica()
            item_builder.get_presentacion()
            item_builder.get_maridaje()
            item_builder.get_ingredientes()
            item_builder.get_extras()
            item_builder.get_user()    

            print("Construyendo pizza")
            pizza = item_builder.build()

            if not pizza:
                raise HTTPException(status_code=404, detail="Item not found")

            return pizza
        
        except Exception as e:
            print(f"Error en get_pedido_by_id: {e}")
            raise
 
    @staticmethod
    def update_pedido(id: int, db: Session, request: Item):
        pedido = CrudItems.get_pedido_by_id(id, db)
    
        if pedido:
            pedido.masa = request.masa
            pedido.salsa = request.salsa
    
            # Convertir la lista de ingredientes a una cadena separada por comas
            ingredientes_str = ', '.join(request.ingredientes)
            # Crear instancias de Ingredient para cada ingrediente en la lista
            ingredientes_objetos = [Ingredient(name=nombre) for nombre in ingredientes_str.split(', ')]
            pedido.ingredientes = ingredientes_objetos
    
            # Convertir la lista de extras a una cadena separada por comas
            extras_str = ', '.join(request.extras)
            # Crear instancias de Extra para cada extra en la lista
            extras_objetos = [Extra(name=nombre) for nombre in extras_str.split(', ')]
            pedido.extras = extras_objetos
    
            pedido.tecnica = request.tecnica
            pedido.presentacion = request.presentacion
            pedido.maridaje = request.maridaje
    
            db.commit()
    
            db.refresh(pedido)
            return ItemDisplayModel(
                id=pedido.id,
                masa=pedido.masa,
                salsa=pedido.salsa,
                ingredientes=[ingrediente.name for ingrediente in pedido.ingredientes],
                extras=[extra.name for extra in pedido.extras],
                tecnica=pedido.tecnica,
                presentacion=pedido.presentacion,
                maridaje=pedido.maridaje,
                user=User(id=request.creator_id, username=" ")
            )
        raise HTTPException(status_code=404, detail="Pedido no encontrado")

    @staticmethod
    def delete_pedido(id:int,db:Session):
        # Obtener el pedido por ID
        pedido = CrudItems.get_pedido_by_id(id, db)

        if not pedido:
            # Manejar el caso en que no se encuentra el pedido
            raise HTTPException(status_code=404, detail="Pedido no encontrado")
        # Eliminar el pedido principal
        db.delete(pedido)

        # Eliminar ingredientes y extras asociados al pedido
        for ingrediente in pedido.ingredientes:
            db.delete(ingrediente)

        for extra in pedido.extras:
            db.delete(extra)

        db.commit()
        return pedido
