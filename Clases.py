from funciones import *
from datetime import *
import random

class Producto():
    def __init__(self, id, nombre, precio, stock, talla):
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
                if os.stat(archivo).st_size > 0:
                    f.write('\n')
                f.write(f"{id},{nombre},{precio},{stock},{talla},{self.fecha_modificacion}")
            print("Producto agregado correctamente.")
            print()
        except IOError:
            print("Error al escribir en el archivo de productos.")
    
    def ver_producto(self, dato):
        try:
            lineas = cargar_datos(archivo)
            encontrado = False
            for linea in lineas:
                partes = linea.strip().split(',')
                if partes[0] == str(dato) or partes[1].lower() == str(dato).lower():
                    print("".center(50, '-'))
                    print(f"ID: {partes[0]} - Nombre: {partes[1]} - Talla: {partes[4]}")
                    print(f"Precio: {partes[2]} - Stock: {partes[3]}")
                    print(f"Ultima modificación: {partes[5]}")
                    print("".center(50, '-'))
                    encontrado = True
                    return partes
            if not encontrado:
                print("Producto no encontrado.")
        except IOError:
            print("Error al leer el archivo de productos.")

    def modificar_producto(self, dato_busqueda):
        try:
            lineas = cargar_datos(archivo)
            if not lineas:
                print("El inventario está vacío. No hay productos que modificar.")
                return
        except IOError:
            print("Error al leer el archivo de productos.")
            return
        producto_encontrado = None
        indice_producto = -1
        for i, linea in enumerate(lineas):
            partes = linea.split(',')
            if partes[0] == str(dato_busqueda) or partes[1].lower() == str(dato_busqueda).lower():
                producto_encontrado = partes
                indice_producto = i
                break
        if producto_encontrado is None:
            print(f"Producto con ID o nombre '{dato_busqueda}' no encontrado.")
            return
        print(f"Producto encontrado: {producto_encontrado[1]}")
        while True:
            print("\n--- ¿Qué deseas modificar? ---")
            print("1. Nombre")
            print("2. Precio")
            print("3. Stock")
            print("4. Talla")
            print("5. Guardar cambios y salir")
            print("6. Cancelar y salir sin guardar")

            opcion = input("Selecciona una opción: ")

            if opcion == '1':
                nuevo_nombre = input(f"Nombre actual: {producto_encontrado[1]}. Ingrese el nuevo nombre: ")
                producto_encontrado[1] = nuevo_nombre
                print("Nombre actualizado.")
            elif opcion == '2':
                nuevo_precio = input(f"Precio actual: {producto_encontrado[2]}. Ingrese el nuevo precio: ")
                producto_encontrado[2] = nuevo_precio
                print("Precio actualizado.")
            elif opcion == '3':
                nuevo_stock = input(f"Stock actual: {producto_encontrado[3]}. Ingrese el nuevo stock: ")
                producto_encontrado[3] = nuevo_stock
                print("Stock actualizado.")
            elif opcion == '4':
                nueva_talla = input(f"Talla actual: {producto_encontrado[4]}. Ingrese la nueva talla: ")
                producto_encontrado[4] = nueva_talla
                print("Talla actualizada.")
            elif opcion == '5':
                # Actualizar fecha de modificación
                producto_encontrado[5] = datetime.now().strftime("%d/%m/%Y")
                linea_modificada = ",".join(producto_encontrado)
                lineas[indice_producto] = linea_modificada
                
                # 4. Guardar todos los datos de vuelta en el archivo
                try:
                    with open(archivo, 'w', encoding='utf-8') as f:
                        f.write('\n'.join(lineas))
                        if lineas:
                            f.write('\n')
                    print("Producto modificado y guardado correctamente.")
                except IOError:
                    print("Error: No se pudieron guardar los cambios en el archivo.")
                break 
            elif opcion == '6':
                print("Modificación cancelada.")
                break
            else:
                print("Opción inválida.")
    
    def eliminar_producto(self, id):
        lineas_actualizadas = []
        producto_encontrado = False
        try:
            lineas = cargar_datos(archivo)
            if not lineas:
                print("El inventario está vacío.")
                return

            for linea in lineas:
                # Comparamos el ID al inicio de la línea para evitar coincidencias parciales (ej: ID 1 vs 10)
                if linea.strip().startswith(str(id) + ','):
                    producto_encontrado = True
                    continue # Saltamos esta línea para no agregarla a la nueva lista
                lineas_actualizadas.append(linea)

            if not producto_encontrado:
                print(f"Producto con ID {id} no encontrado.")
                return

            with open(archivo, 'w', encoding='utf-8') as f:
                f.write('\n'.join(lineas_actualizadas))
                # Aseguramos que el archivo termine con un salto de línea si no está vacío
                if lineas_actualizadas:
                    f.write('\n')
            print("Producto eliminado correctamente.")

        except FileNotFoundError:
            print("El archivo de productos no existe. Crea un producto primero.")
        except IOError:
            print("Error al leer el archivo de productos.")


class Inventario(Producto):
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            pass
    except FileNotFoundError:
        with open(archivo, 'w', encoding='utf-8') as f:
            pass
    finally:
        pass
    
    def __init__(self):
        self.productos = []
    
    def ver_inventario(self):
        try:
            lineas_productos = cargar_datos(archivo)
            if not lineas_productos:
                print("No existen productos en el inventario.")
                return

            print("".center(50, '='))    
            print("INVENTARIO".center(50, ' '))
            print("".center(50, '='))
            for linea in lineas_productos:
                partes = linea.split(',')
                print("".center(50, '-'))
                print(f"ID: {partes[0]} - Nombre: {partes[1]} - Talla: {partes[4]}")
                print(f"Precio: {partes[2]} - Stock: {partes[3]}")
                print(f"Ultima modificación: {partes[5]}")
            print("".center(50, '-'))
            print()
            input("Presione enter para continuar...")
            print()
        except Exception as e:
            print("Ocurrió un error inesperado al ver el inventario:", e)