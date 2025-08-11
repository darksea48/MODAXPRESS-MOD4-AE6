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
            lineas = [line.strip() for line in f if line.strip()]
            return lineas
    except FileNotFoundError:
        print("El archivo de productos no existe.")
        return []
    except IOError:
        print("Error al abrir el archivo")
        return []

def guardar_datos(archivo: str, productos: list):
    try:
        with open(archivo, 'a', encoding='utf-8') as f:
            f.write(f"\n{productos}")
    except IOError:
        print("Error al abrir el archivo")