import time
import os
import json

# --- CONFIGURACIÓN DE INTERFAZ (COLORES) ---
VERDE, AMARILLO, AZUL, ROJO, RESET = "\033[92m", "\033[93m", "\033[94m", "\033[91m", "\033[0m"

# --- PERSISTENCIA JSON ---

def cargar_datos(nombre_archivo="inventario.json"):
    """Carga la lista de productos desde el archivo JSON principal."""
    if os.path.exists(nombre_archivo):
        try:
            with open(nombre_archivo, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []


def guardar_datos(inventario, nombre_archivo="inventario.json"):
    """Guarda el estado actual del inventario en el archivo JSON."""
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            json.dump(inventario, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"{ROJO}⚠️ Error al sincronizar: {e}{RESET}")

# --- LÓGICA DE NEGOCIO ---

def buscar_producto(inventario, nombre):
    """Retorna el diccionario o None (Lógica interna)."""
    for p in inventario:
        if p['nombre'].lower() == nombre.lower():
            return p
    return None

def interfaz_buscar_producto(inventario):
    """Interfaz para que el usuario busque un producto por nombre."""
    print(f"\n{AZUL}🔍 BUSCAR PRODUCTO{RESET}")
    nombre = input("Ingresa el nombre a buscar: ").strip()
    p = buscar_producto(inventario, nombre)
    
    if p:
        print(f"\n{VERDE}✅ ¡Producto encontrado!{RESET}")
        print(f"   📌 Nombre:   {p['nombre']}")
        print(f"   💰 Precio:   ${p['precio']:,.2f}")
        print(f"   📦 Stock:    {p['cantidad']} unidades")
        print(f"   💵 Subtotal: ${p['precio'] * p['cantidad']:,.2f}")
    else:
        print(f"\n{ROJO}❌ No se encontró '{nombre}' en el inventario.{RESET}")

def agregar_producto(inventario):
    """Captura datos y añade un producto si no existe duplicado."""
    print(f"\n{VERDE}➕ AGREGAR PRODUCTO{RESET}")
    nombre = input("Nombre: ").strip()
    if buscar_producto(inventario, nombre):
        print(f"{ROJO}⚠️ El producto ya existe.{RESET}")
        return
    try:
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
        if precio < 0 or cantidad < 0: raise ValueError
        inventario.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
        print(f"✅ {VERDE}Guardado.{RESET}")
    except ValueError:
        print(f"{ROJO}⚠️ Datos numéricos inválidos.{RESET}")

def mostrar_inventario(inventario):
    """Muestra el inventario en formato de tabla legible."""
    print(f"\n{AZUL}📋 INVENTARIO ACTUAL{RESET}")
    print(f"{AZUL}--------------------------------------------------{RESET}")
    if not inventario:
        print("   Inventario vacío.")
    else:
        print(f"  ╭───────────────────────────────────────────╮")
        print(f"  | {AMARILLO}{'NOMBRE':<18}{RESET} | {AMARILLO}{'PRECIO':>10}{RESET} | {AMARILLO}{'STOCK':>8}{RESET}|")
        print(f"  |───────────────────────────────────────────|")
        for p in inventario:
            print(f"  | {p['nombre']:<18} | ${p['precio']:>9.2f} | {p['cantidad']:>8}|")
        print(f"  ╰───────────────────────────────────────────╯")
    print(f"{AZUL}--------------------------------------------------{RESET}")

def actualizar_producto(inventario):
    """Edita precio/cantidad buscando por nombre."""
    nombre = input(f"\n{AMARILLO}✏️  Nombre a editar: {RESET}").strip()
    p = buscar_producto(inventario, nombre)
    if p:
        try:
            np = input(f"Nuevo precio [{p['precio']}]: ")
            nc = input(f"Nueva cantidad [{p['cantidad']}]: ")
            if np: p['precio'] = float(np)
            if nc: p['cantidad'] = int(nc)
            print(f"✅ {VERDE}Actualizado.{RESET}")
        except ValueError:
            print(f"{ROJO}⚠️ Error: Valor no numérico.{RESET}")
    else:
        print(f"{ROJO}⚠️ No encontrado.{RESET}")

def eliminar_producto(inventario):
    """Elimina un producto por nombre."""
    nombre = input(f"\n{ROJO}🗑️  Nombre a eliminar: {RESET}").strip()
    p = buscar_producto(inventario, nombre)
    if p:
        inventario.remove(p)
        print(f"✅ {VERDE}Eliminado.{RESET}")
    else:
        print(f"{ROJO}⚠️ No existe.{RESET}")

def calcular_estadisticas(inventario):
    """Calcula métricas detalladas usando lambdas."""
    if not inventario: return None
    subtotal = lambda p: p["precio"] * p["cantidad"]
    u_totales = sum(p['cantidad'] for p in inventario)
    v_total = sum(subtotal(p) for p in inventario)
    m_caro = max(inventario, key=lambda p: p['precio'])
    m_stock = max(inventario, key=lambda p: p['cantidad'])
    return {
        "unidades_totales": u_totales,
        "valor_total": v_total,
        "producto_mas_caro": m_caro,
        "producto_mayor_stock": m_stock
    }

def fusionar_inventarios(actual, nuevos):
    """Fusiona dos inventarios (Suma stock y actualiza precio)."""
    agregados = 0
    actualizados = 0
    for n in nuevos:
        p_existente = buscar_producto(actual, n['nombre'])
        if p_existente:
            p_existente['cantidad'] += n['cantidad']
            p_existente['precio'] = n['precio']
            actualizados += 1
        else:
            actual.append(n)
            agregados += 1
    return agregados, actualizados

def reiniciar_inventario(inventario):
    """Limpia la lista y elimina el archivo JSON."""
    if input(f"\n{ROJO}⚠️ ¿Borrar TODO? (s/n): {RESET}").lower() == 's':
        inventario.clear()
        if os.path.exists("inventario.json"): os.remove("inventario.json")
        print(f"✅ {VERDE}Sistema reiniciado.{RESET}")


