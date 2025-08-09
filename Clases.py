from funciones import *
from datetime import *
from random import *

class Producto():
    def __init__(self, nombre, precio, stock, talla, id=randint(1,999999999)):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.talla = talla
        self.fecha_modificacion = datetime.now().strftime("%d/%m/%Y")
    
    """
    def __str__(self):
        return f"Producto: {self.nombre}\nPrecio: {self.precio}\nTalla: {self.talla}\nStock: {self.stock}\nUltima modificación: {self.fecha_modificacion}"
    """
    
    def agregar_producto(self, id, nombre, precio, stock, talla):
        try:
            with open(archivo, 'a', encoding='utf-8') as f:
                f.write(f"\n{id},{nombre},{precio},{stock},{talla},{self.fecha_modificacion}")
        except FileNotFoundError:
            print("El archivo de recetas no existe. Crea una receta primero.")
        except IOError:
            print("Error al leer el archivo de recetas.")
        finally:
            f.close()
    
    def modificar_producto(self):
        while True:
            try:
                print("--- MODIFICAR PRODUCTO ---")
                print("1. Modificar nombre")
                print("2. Modificar precio")
                print("3. Modificar stock")
                print("4. Modificar talla")
                opcion = int(input("Selecciona una opción: "))
                if opcion == 1:
                    nuevo_nombre = input("Ingrese el nuevo nombre del producto: ")
                    self.nombre = nuevo_nombre
                    print("Nombre modificado correctamente.")
                elif opcion == 2:
                    while True:
                        try:
                            nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
                            self.precio = nuevo_precio
                            print("Precio modificado correctamente.")
                            break
                        except ValueError:
                            print("Datos ingresados no son correctos. Por favor volver a intentarlo.")
                elif opcion == 3:
                    while True:
                        nuevo_stock = int(input("Ingrese el nuevo stock del producto: "))
                        if nuevo_stock < 0:
                            print("El stock no puede ser negativo.")
                            continue
                        elif nuevo_stock == self.stock:
                            print("El stock no ha cambiado.")
                            r_u_sure = input("¿Estás seguro que el stock es ese? (s/n): ")[:1].lower()
                            if r_u_sure == 's':
                                break
                            else:
                                continue
                        else:
                            self.stock = nuevo_stock
                            print("Stock modificado correctamente.")
                            break
                elif opcion == 4:
                    nueva_talla = input("Ingrese la nueva talla del producto: ")
                    self.talla = nueva_talla
                    print("Talla modificada correctamente.")
                else:
                    print("Opción inválida. Por favor, selecciona una opción válida.")
            except ValueError:
                print("Opción inválida. Por favor, selecciona una opción válida.")
            finally:
                while True:
                    nuevo_try = input("¿Quieres volver a modificar algo? (s/n): ")[:1].lower()
                    if nuevo_try not in ['s','n']:
                        print("Opción inválida. Por favor, selecciona una opción válida.")
                    elif nuevo_try.lower() == 's':
                        break

class Inventario(Producto):
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            pass
    except FileNotFoundError:
        with open(archivo, 'w', encoding='utf-8') as f:
            pass
    finally:
        f.close()
    
    def __init__(self):
        self.productos = []
    
    def ver_inventario(self):
        try:
            with open(archivo, 'r', encoding='utf-8') as f:
                productos = f.readlines()
                if not productos:
                    print("No hay productos en el inventario.")
                    return
                print("\n--- INVENTARIO ---")
                for i, productos in enumerate(productos):
                    print(f"{i+1}. {productos.strip()}")
                print("-------------------------\n")
        except FileNotFoundError:
            print("El archivo de recetas no existe. Crea una receta primero.")
        except IOError:
            print("Error al leer el archivo de recetas.")
        finally:
            f.close()