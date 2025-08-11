import os

archivo = "inventario.txt"

# Funciones
def limpiar_pantalla():
    if os.name == 'nt': # Windows
        os.system('cls')
    else: # Linux, macOS
        os.system('clear')

def cargar_datos(archivo: str) -> list:
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            contenido = f.read()
            return contenido.split('\n')
    except FileNotFoundError:
        print("El archivo no existe")
    except IOError:
        print("Error al abrir el archivo")
    finally:
        f.close()

def guardar_datos(archivo: str, productos: list):
    try:
        with open(archivo, 'a', encoding='utf-8') as f:
            f.write(f"\n{productos}")
    except FileNotFoundError:
        print("El archivo no existe")
    except IOError:
        print("Error al abrir el archivo")
    finally:
        f.close()

def mostrar_inventario(archivo: str) -> list:
    productos = cargar_datos(archivo)
    for i in range(len(productos)):
        print(f"{i+1} - {productos[i]}")
    return productos