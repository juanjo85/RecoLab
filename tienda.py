# Clase Tienda
class Tienda:
    # Construir tienda
    def __init__ (self,nombre_tienda,direccion_tienda,categoria,imagen_portada_tienda,contacto,ID_tienda):
        self.nombre_tienda = nombre_tienda
        self.direccion_tienda = direccion_tienda
        self.categoria = categoria
        self.imagen_portada_tienda = imagen_portada_tienda
        self.contacto = contacto
        self.ID_tienda = ID_tienda
        print("Se ha creado la tienda",self.nombre_tienda)
        
    # Editar datos de la tienda
    def editar_nombre (self,nuevo_nombre):
        self.nombre_tienda = nuevo_nombre
        print("Se ha modificado el nombre de la tienda ha",nuevo_nombre)

    def editar_direccion_tienda (self,nueva_direccion_tienda):
        self.direccion_tienda = nueva_direccion_tienda
        print("Se ha modificado la direcion de tienda ha",nueva_direccion_tienda)
    
    def editar_categoria (self,nueva_categoria):
        self.categoria = nueva_categoria
        print("Se ha modificado la categoria por",nueva_categoria)

    def editar_imagen_portada_tienda (self,nueva_imagen_portada_tienda):
        self.imagen_portada_tienda = nueva_imagen_portada_tienda
        print("Se ha modificado la imagen de portada")

    def ID (self,nuevo_ID_tienda):
        self.ID_tienda = nuevo_ID_tienda
        print("Se ha modificado el ID de la tienda ha",nuevo_ID_tienda)

    # Borrar Tienda
    def __del__(self):
        print("Se ha borrando la Tienda",self.ID_tienda)
    
    # Mostrar datos de la tienda
    def __str__(self):
        print("La tienda {} ubicada en {} de la categoria {} la puedes contactar atraves de {}".format(self.nombre_tienda,self.direccion_tienda,self.categoria,self.contacto)) 
class Catalogo_Tiendas:
    # Crear catalogo de tiendas
    def __init__(self,catalogo = []):
        self.catalogo = catalogo

    # Agregar al catalogo de tiendas
    def agregar (self,t):
        t = self.catalogo.append(t)

    # Mostrar catalogo de tiendas
    def mostrar (self,catalogo):
            print(catalogo)

    # Clase Productos

class Producto:
    def __init__ (self,nombre_producto,descripcion_producto,imagen_producto,precio_producto,ID_producto,):
        self.ID_producto = ID_producto
        self.nombre_producto = nombre_producto
        self.descripcion_producto = descripcion_producto
        self.imagen_producto = imagen_producto
        self.precio_producto = precio_producto
        self.ID_producto = ID_producto
        print("Se ha creado el producto",self.nombre_producto)
    
    # Editar Productos
    def editar_nombre_producto (self,nuevo_nombre_producto):
        self.nombre_producto = nuevo_nombre_producto
        print("Se ha modificado el nombrel producto ha",nuevo_nombre_producto)

    def editar_descripcion_producto (self,nueva_descripcion_producto):
        self.descripcion_producto = nueva_descripcion_producto
        print("Se ha modificado la descripcion del producto ha",nueva_descripcion_producto)
    
    def editar_imagen_producto (self,nueva_imagen_producto):
        self.imagen_producto = nueva_imagen_producto
        print("Se ha modificado la imagen del producto")

    def editar_precio_producto (self,nueva_precio_producto):
        self.precio_producto = nueva_precio_producto
        print("Se ha modificado el precio del producto a $ ",nueva_precio_producto)

    def editar_ID_producto (self,nuevo_ID_producto):
        self.ID_producto = nuevo_ID_producto
        print("Se ha modificado el ID del producto ha",nuevo_ID_producto)

    # Borrar Producto
    def __del__(self):
        print("Se ha borrado el producto",self.ID_producto)
    
    # Mostrar datos el producto
    def __str__(self):
        print("EL producto {} con la descripcion {} tiene el precio {}".format(self.nombre_producto,self.descripcion_producto,self.precio_producto)) 

class Catalogo_Productos:

    # Crear catalogo de productos
    def __init__(self,catalogo_productos = []):
        self.catalogo_productos = catalogo_productos
