# Hecho por: Clara Anahí González Apolo
# Programación Orientada a Objetos - Estructuras de Datos
# Tarea Semana 9

# Clase que representa un producto dentro del sistema
class Producto:
    def __init__(self, id_producto: str, nombre: str, cantidad: int, precio: float):
        """
        Constructor de la clase Producto.
        id_producto: str -> Identificador único.
        nombre: str -> Nombre del producto.
        cantidad: int -> Cantidad disponible.
        precio: float -> Precio unitario.
        """
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Métodos getters para acceder a los atributos
    def get_id(self) -> str:
        return self.id_producto
    
    def get_nombre(self) -> str:
        return self.nombre
    
    def get_cantidad(self) -> int:
        return self.cantidad
    
    def get_precio(self) -> float:
        return self.precio

    # Setter con validación para evitar valores inválidos
    def set_cantidad(self, nueva_cantidad: int) -> None:
        if nueva_cantidad >= 0:
            self.cantidad = nueva_cantidad

    def set_precio(self, nuevo_precio: float) -> None:
        if nuevo_precio > 0:
            self.precio = nuevo_precio

    # Representación en texto del objeto
    def __str__(self) -> str:
        return f"ID: {self.id_producto}  {self.nombre}  Cant: {self.cantidad}  Precio: ${self.precio}"
