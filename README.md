# pizzeria_v2

Este proyecto utiliza el microframework FastAPI para construir una aplicación que permite a los usuarios personalizar y realizar pedidos de pizzas. El sistema está dividido en frontend y backend, con una base de datos (SQLAlchemy) que almacena la información de los pedidos y los usuarios. Además, se emplea el patrón de diseño Builder para crear objetos relacionados con los pedidos de manera modular y flexible.
A diferencia de frameworks más integrados como Django, la gestión de usuarios y pedidos no viene predefinida.


1. Estructura del Proyecto:
------------------------------

- App y Routers: La aplicación sigue una estructura típica de FastAPI, con la definición de rutas y operaciones en routers. Los routers, en este caso, gestionan tanto los ítems como los usuarios. Se utiliza el enfoque de programación asíncrona para manejar las solicitudes de manera eficiente.

- Templates: Se utilizan archivos HTML como templates para renderizar las páginas web. Los templates están vinculados a las rutas definidas en los routers. 

- Builder: Se ha implementado un patrón de diseño Builder para crear objeto, utilizándolo para crear objetos relacionados con pedidos. Cuando un cliente busca su pedido, se genera un builder con el pedido creado. Más detallado abajo.

- Auth: Al crear un nuevo pedido, se asigna un ID de usuario y se genera un objeto User. La información relevante, como el ID del pedido, se almacena en cookies del navegador.
  Se utiliza JavaScript para obtener y manipular cookies. La autenticación y la gestión de sesiones se llevan a cabo manualmente. Al cerrar sesión, se eliminan las cookies relacionadas con el usuario.



2. Código del Servidor:
------------------------------

- FastAPI Models: Se definen modelos utilizando las clases de Pydantic proporcionadas por FastAPI para validar y documentar las solicitudes y respuestas.
CRUD Operations: Las operaciones CRUD (Crear, Leer, Actualizar, Eliminar) se implementan en las clases CrudItemsInterfaz y CrudItems, la interfaz y su implementación concreta respectivamente, lo que facilita la expansión y mantenimiento del código. Y se hace lo mismo para el usuario.

- Creación de Pedidos: La función create_pedido en CrudItems crea un nuevo pedido en la base de datos, gestionando las relaciones con ingredientes y extras. Se utiliza un objeto JSONResponse para enviar la respuesta al cliente.

3. Patrón de Diseño Builder:
------------------------------

- Objetivo del Builder: El patrón Builder se utiliza para construir objetos complejos paso a paso. En este contexto, se utiliza para construir objetos relacionados con pedidos.

- Uso: Aunque inicialmente parezca que la mejor ubicación para aplicar el Builder es durante la creación de un pedido, es importante considerar que al crear un pedido se están generando datos, no objetos. La implementación más eficaz del Builder en este contexto se da al recuperar un pedido, donde se traducen los datos almacenados en la base de datos en un objeto estructurado.

- Implementación: El código del Builder se encuentra en la sección que maneja los pedidos en el backend. La clase ItemBuilder se encarga de construir objetos DbItem (pedidos de pizza) paso a paso.
  El proceso se realiza de la siguiente manera: al recuperar un pedido de la base de datos, utilizamos el patrón Builder. Creamos una instancia de la clase ItemBuilder y configuramos sus propiedades utilizando la información específica almacenada en la base de datos. Cada método del Builder se encarga de asignar un aspecto particular del pedido, como la masa, la salsa, los ingredientes, entre otros. Una vez que todas las propiedades relevantes han sido configuradas, invocamos el método build para obtener el objeto DbItem completamente estructurado.
