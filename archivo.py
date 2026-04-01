import csv

# Colores para mensajes de estado
VERDE, ROJO, RESET = "\033[92m", "\033[91m", "\033[0m"

def guardar_csv(inventario, ruta="inventario_exportado.csv", incluir_header=True):
    """
    Exporta la lista de diccionarios a un archivo CSV.
    
    Parámetros:
    - inventario: Lista de diccionarios con los productos.
    - ruta: Nombre o camino del archivo de destino.
    - incluir_header: Booleano para decidir si escribir la fila de títulos.
    """
    
    # REGLA: Validar que el inventario no esté vacío
    if not inventario:
        print(f"\n{ROJO}⚠️ Error: No se puede exportar un inventario vacío.{RESET}")
        return

    try:
        # Abrimos el archivo en modo escritura ('w')
        # newline='' evita líneas en blanco adicionales en algunos sistemas
        with open(ruta, mode='w', newline='', encoding='utf-8') as archivo_csv:
            # Definimos los nombres de las columnas basados en las llaves del diccionario
            campos = ["nombre", "precio", "cantidad"]
            escritor = csv.DictWriter(archivo_csv, fieldnames=campos)

            if incluir_header:
                escritor.writeheader()

            # Escribimos todas las filas del inventario
            escritor.writerows(inventario)
            
            print(f"\n{VERDE}✅ Inventario guardado exitosamente en: {ruta}{RESET}")

    except PermissionError:
        print(f"\n{ROJO}⚠️ Error de permisos: El archivo está abierto por otro programa o no tienes permisos de escritura.{RESET}")
    except OSError as e:
        print(f"\n{ROJO}⚠️ Error de sistema al intentar escribir el archivo: {e}{RESET}")
    except Exception as e:
        print(f"\n{ROJO}⚠️ Ocurrió un error inesperado: {e}{RESET}")