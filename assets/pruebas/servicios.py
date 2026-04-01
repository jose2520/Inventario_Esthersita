import time
import os
import json

# --- CONFIGURACIÓN DE INTERFAZ (COLORES) ---
VERDE, AMARILLO, AZUL, ROJO, RESET = "\033[92m", "\033[93m", "\033[94m", "\033[91m", "\033[0m"

# --- MÓDULO DE PERSISTENCIA ---

def cargar_datos(nombre_archivo="inventario.json"):
    """
    Lee el archivo JSON al iniciar el programa y devuelve la lista de datos.
    Si el archivo no existe, retorna una lista vacía.
    """
    try:
        if os.path.exists(nombre_archivo):
            with open(nombre_archivo, "r", encoding="utf-8") as f:
                return json.load(f)
        return []
    except Exception as e:
        print(f"{ROJO}⚠️ Error al cargar datos: {e}{RESET}")
        return []

def guardar_datos(inventario, nombre_archivo="inventario.json"):
    """
    Guarda la lista de diccionarios actual en un archivo físico .json.
    """
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            json.dump(inventario, f, indent=4, ensure_ascii=False)
        print(f"\n{VERDE}💾 Datos sincronizados correctamente.{RESET}")
    except Exception as e:
        print(f"\n{ROJO}⚠️ Error al guardar: {e}{RESET}")

# --- MÓDULO DE SERVICIOS (LÓGICA DE NEGOCIO) ---

def buscar_producto(inventario, nombre):
    """
    Busca un producto por su nombre (sin importar mayúsculas/minúsculas).
    
    Parámetros:
    - inventario: Lista de diccionarios.
    - nombre: String con el nombre a buscar.
    
    Retorna: El diccionario del producto o None si no se encuentra.
    """
    for producto in inventario:
        if producto['nombre'].lower() == nombre.lower():
            return producto
    return None

def agregar_producto(inventario):
    """
    Captura datos desde teclado, valida que el producto no exista y lo añade.
    """
    print(f"\n{VERDE}➕ AGREGAR NUEVO PRODUCTO{RESET}")
    nombre = input("Nombre del producto: ").strip()
    
    if not nombre:
        print(f"{ROJO}⚠️ El nombre no puede estar vacío.{RESET}")
        return

    if buscar_producto(inventario, nombre):
        print(f"{ROJO}⚠️ Error: Ya existe un producto con ese nombre.{RESET}")
        return

    try:
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
        
        if precio < 0 or cantidad < 0:
            print(f"{ROJO}⚠️ No se permiten valores negativos.{RESET}")
            return

        nuevo_prod = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
        inventario.append(nuevo_prod)
        print(f"✅ {VERDE}Producto '{nombre}' registrado.{RESET}")
    except ValueError:
        print(f"{ROJO}⚠️ Error: Debes ingresar números válidos.{RESET}")

def mostrar_inventario(inventario):
    """
    Recorre la lista y muestra los productos con formato de tabla.
    """
    print(f"\n{AZUL}📋 ESTADO DEL INVENTARIO{RESET}")
    print(f"{AZUL}--------------------------------------------------{RESET}")
    if not inventario:
        print("   El inventario está actualmente vacío.")
    else:
        # Encabezados
        print(f"   {'NOMBRE':<18} | {'PRECIO':>10} | {'STOCK':>8}")
        print(f"   {'-'*44}")
        for p in inventario:
            print(f"   {p['nombre']:<18} | ${p['precio']:>9.2f} | {p['cantidad']:>8}")
    print(f"{AZUL}--------------------------------------------------{RESET}")

def actualizar_producto(inventario):
    """
    Busca un producto por nombre y permite modificar precio o cantidad.
    """
    nombre_buscado = input(f"\n{AMARILLO}✏️  Nombre del producto a editar: {RESET}").strip()
    prod = buscar_producto(inventario, nombre_buscado)

    if prod:
        print(f"Modificando: {AZUL}{prod['nombre']}{RESET} (Presiona Enter para mantener actual)")
        try:
            n_precio = input(f"Nuevo precio [{prod['precio']}]: ").strip()
            n_cant = input(f"Nueva cantidad [{prod['cantidad']}]: ").strip()

            if n_precio: prod['precio'] = float(n_precio)
            if n_cant: prod['cantidad'] = int(n_cant)
            print(f"✅ {VERDE}Actualización exitosa.{RESET}")
        except ValueError:
            print(f"{ROJO}⚠️ Error: Formato numérico incorrecto.{RESET}")
    else:
        print(f"{ROJO}⚠️ El producto '{nombre_buscado}' no existe.{RESET}")

def eliminar_producto(inventario):
    """
    Busca por nombre y elimina el elemento de la lista si existe.
    """
    nombre_buscado = input(f"\n{ROJO}🗑️  Nombre del producto a eliminar: {RESET}").strip()
    prod = buscar_producto(inventario, nombre_buscado)

    if prod:
        inventario.remove(prod)
        print(f"✅ {VERDE}Producto '{nombre_buscado}' eliminado correctamente.{RESET}")
    else:
        print(f"{ROJO}⚠️ No se encontró ningún producto con ese nombre.{RESET}")

def calcular_estadisticas(inventario):
    """
    Calcula métricas financieras y de stock.
    
    Retorna: Un diccionario con total_items, valor_total y stock_total.
    """
    stats = {
        "total_items": len(inventario),
        "valor_total": sum(p['precio'] * p['cantidad'] for p in inventario),
        "stock_total": sum(p['cantidad'] for p in inventario)
    }
    return stats

def reiniciar_inventario(inventario, nombre_archivo="inventario.json"):
    """
    Limpia la memoria y elimina el archivo de persistencia física.
    """
    confirmar = input(f"\n{ROJO}⚠️  ¿Seguro que quieres borrar TODO? (s/n): {RESET}").lower()
    if confirmar == 's':
        inventario.clear()
        if os.path.exists(nombre_archivo):
            os.remove(nombre_archivo)
        print(f"✅ {VERDE}Inventario borrado por completo.{RESET}")
    else:
        print(f"ℹ️  Operación cancelada.")