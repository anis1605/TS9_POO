# Hecho por: Clara Anahí González Apolo
# Programación Orientada a Objetos - Estructuras de Datos
# Tarea Semana 9

from servicios.inventario import Inventario
from modelos.producto import Producto

# Muestra las opciones disponibles al usuario
def mostrar_menu() -> None:
    print("1 Agregar producto")
    print("2 Eliminar producto")
    print("3 Actualizar producto")
    print("4 Buscar por nombre")
    print("5 Mostrar inventario")
    print("6 Salir")

def main() -> None:
    # Se crea una instancia del inventario
    inventario = Inventario()
    
    while True:
        mostrar_menu()
        opcion = input("Opcion: ")
        
        if opcion == "6":
            break
            
        elif opcion == "1":
            id_prod: str = input("ID: ")
            nombre: str = input("Nombre: ")
            cantidad: int = int(input("Cantidad: "))
            precio: float = float(input("Precio: "))

            # Se crea el objeto Producto
            producto = Producto(id_prod, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
                
        elif opcion == "2":
            id_prod: str = input("ID a eliminar: ")
            inventario.eliminar_producto(id_prod)
            
        elif opcion == "3":
            id_prod: str = input("ID a actualizar: ")
            cant_str: str = input("Nueva cantidad (enter para no cambiar): ")
            prec_str: str = input("Nuevo precio (enter para no cambiar): ")
            
            # Permite actualizar solo si el usuario ingresa valor
            cantidad = int(cant_str) if cant_str else None
            precio = float(prec_str) if prec_str else None
            
            inventario.actualizar_producto(id_prod, cantidad, precio)
            
        elif opcion == "4":
            texto: str = input("Buscar: ")
            inventario.buscar_por_nombre(texto)
            
        elif opcion == "5":
            inventario.mostrar_todos()
            
        else:
            print("Opcion invalida")

if __name__ == "__main__":
    main()
