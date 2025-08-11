# MODAXPRESS
from Clases import *

def mostrar_menu_principal():
    while True:
        try:
            inventario = Inventario()
            print("--- MODA XPRESS: Gestión de inventario ---")
            print("1. Registrar nuevo producto")
            print("2. Consultar inventario completo ")
            print("3. Leer datos de un producto especifico")
            print("4. Modificar datos de un producto")
            print("5. Eliminar un producto del inventario")
            print("6. Salir del programa")

            opcion = input("Selecciona una opción: ")

            if opcion == '1':
                #registrar un nuevo producto()
                nombre = input("Nombre del producto: ")
                while True:
                    try:
                        precio = float(input("Precio del producto: "))
                        break
                    except ValueError:
                        print("Datos ingresados no son correctos. Por favor volver a intentarlo.")
                while True:
                    try:
                        cantidad = int(input("Cantidad de productos registrados: "))
                        break
                    except ValueError:
                        print("Datos ingresados no son correctos. Por favor volver a intentarlo.")
                talla = input("Ingresar talla de producto: ")
                id = random.randint(1,999999999)
                nuevo_producto = Producto(id, nombre, precio, cantidad, talla)
                nuevo_producto.agregar_producto(id, nombre, precio, cantidad, talla)
            elif opcion == '2':
                inventario.ver_inventario()
            elif opcion == '3': #leer datos de un producto especifico()
                busqueda = input("Ingresar producto a buscar (ingresa el ID o el nombre del producto): ")
                inventario.ver_producto(busqueda)
                # falta agregar esta función, para quien la quiera hacer
            elif opcion == '4': #modificar datos de un producto()
                producto_seleccionado = input("Ingresa el producto a modificar (ingresa el ID o el nombre del producto): ")
                inventario.modificar_producto(producto_seleccionado)
            elif opcion == '5': #eliminar un producto del inventario()
                # Falta agregar esta opción, para quien la quiera hacer
                producto_seleccionado = input("Ingresa el ID del producto a eliminar: ")
                inventario.eliminar_producto(producto_seleccionado)
            elif opcion == '6':
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida. Por favor, selecciona una opción válida.")
        except KeyboardInterrupt:
            print("Programa interrumpido por el usuario. ¡Hasta luego!\n")
            break
        except Exception as e:
            print(f"Ocurrió un error. Contacte con el administrador del sistema. Error: {e}")

mostrar_menu_principal()
