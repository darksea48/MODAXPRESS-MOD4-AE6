# MODAXPRESS
from Clases import *

def mostrar_menu_principal():
    while True:
        try:
            inventario = Inventario()
            print("\n --- MODA XPRESS: Gestión de inventario ---")
            print("1. Registrar nuevo producto")
            print("2. Consultar inventario completo ")
            print("3. Leer datos de un producto especifico")
            print("4. Modificar datos de un producto")
            print("5. Eliminar un producto del inventario")
            print("6. Salir del programa")

            opcion = input("Selecciona una opción: ")

            if opcion == '1':
                #registrar un nuevo producto()
                nombre = input ("Nombre del producto:")
                precio = input ("Precio del producto en pesos clp ") 
                cantidad = input ("Cantidad de productos registrados") 
                talla = input ("Ingresar talla de producto") 
                nuevo_producto = Producto(nombre, precio, cantidad, talla)
                nuevo_producto.agregar_producto(nombre, precio, cantidad, talla)
            elif opcion == '2':
                inventario.ver_inventario()
            
            elif opcion == '3':
                leer datos de un producto especifico()
                busqueda = input ("Ingresar producto a buscar")
                print = ("El producto es: ")

            elif opcion == '4':
                modificar datos de un producto() 
                inventario.modificar_producto()
            elif opcion == '5':
                eliminar un producto del inventario()    
            elif opcion == '6':
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida. Por favor, selecciona una opción válida.")
        except KeyboardInterrupt:
            print("\n")
            print("Programa interrumpido por el usuario. ¡Hasta luego!\n")
        except Exception as e:
            print(f"Ocurrió un error: {e}")

mostrar_menu_principal()
