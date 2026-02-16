# Hecho por: Clara Anahí González Apolo
# Programación Orientada a Objetos - Estructuras de Datos
# Tarea Semana 9

from modelos.producto import Producto

# Clase que administra la colección de productos
class Inventario:
    def __init__(self) -> None:
        # Diccionario donde:
        # clave = ID (str)
        # valor = objeto Producto
        # Se usa diccionario para garantizar ID único
        self.productos: dict[str, Producto] = {}

    def agregar_producto(self, producto: Producto) -> None:
        # Verifica que el ID no esté repetido
        if producto.get_id() in self.productos:
            print("Error: ya existe ese ID")
        else:
            self.productos[producto.get_id()] = producto

    def eliminar_producto(self, id_producto: str) -> None:
        # Elimina el producto si existe
        if id_producto in self.productos:
            del self.productos[id_producto]
        else:
            print("No se encontro el producto")

    def actualizar_producto(
        self,
        id_producto: str,
        cantidad: int | None = None,
        precio: float | None = None
    ) -> None:
        # Verifica existencia del producto
        if id_producto not in self.productos:
            print("No se encontro el producto")
            return
        
        prod = self.productos[id_producto]

        # Solo actualiza los valores enviados
        if cantidad is not None:
            prod.set_cantidad(cantidad)
        
        if precio is not None:
            prod.set_precio(precio)

    def buscar_por_nombre(self, texto: str) -> None:
        # Búsqueda parcial ignorando mayúsculas/minúsculas
        texto = texto.lower()
        print("Resultados:")
        encontro = False

        for producto in self.productos.values():
            if texto in producto.get_nombre().lower():
                print(producto)
                encontro = True

        if not encontro:
            print("No hay coincidencias")

    def mostrar_todos(self) -> None:
        # Muestra todos los productos almacenados
        if not self.productos:
            print("Inventario vacio")
            return
        
        print("Inventario:")
        for producto in self.productos.values():
            print(producto)
