class Tienda:
    # Construir tienda
    def __init__ (self,nombre_tienda,direccion_tienda,categoria,imagen_portada_tienda,contacto):
        self.nombre_tienda = nombre_tienda
        self.direccion_tienda = direccion_tienda
        self.categoria = categoria
        self.imagen_portada_tienda = imagen_portada_tienda
        self.contacto = contacto
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

    # Borrar Tienda
    def __del__(self):
        print("Se ha borrando la Tienda",self.nombre_tienda)
    
    # Mostrar datos de la tienda
    def __str__(self):
        print("La tienda {} ubicada en {} de la categoria {} la puedes contactar atraves de {}".format(self.nombre_tienda,self.direccion_tienda,self.categoria,self.contacto)) 
class Catalogo_Tiendas:
    # Crear catalogo de tiendas
    def __init__(self,catalogo = []):
        self.catalogo = catalogo

    # Agregar al catalogo de tiendas
    def agregar (self,t):
        self.catalogo.append(t)

    # Mostrar catalogo de tiendas
    def mostrar (self):
        for t in self.catalogo:
            print(t)