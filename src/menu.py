import time
import sys

# 1. Definimos la lista global
inventario = []

# Definición de colores para la terminal
VERDE = "\033[92m"
AMARILLO = "\033[93m"
AZUL = "\033[94m"
ROJO = "\033[91m"
RESET = "\033[0m"

def escribir_suave(texto, velocidad=0.03):
    """Efecto de escritura letra por letra usando sys."""
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(velocidad)
    print()

while True:
    # --- DISEÑO DEL MENÚ CON EFECTO TIME ---
    lineas_menu = [
        f"\n{AZUL}+-----------------------------------+{RESET}",
        f"{AZUL}|{RESET} {AZUL}📦 MENÚ DE GESTIÓN DEL INVENTARIO{RESET} {AZUL}|{RESET}",
        f"{AZUL}|-----------------------------------|{RESET}",
        f"{AZUL}|{RESET}  {VERDE}[1.]{RESET} Agregar producto ✨         {AZUL}|{RESET}",
        f"{AZUL}|{RESET}  {VERDE}[2.]{RESET} Mostrar inventario 📋       {AZUL}|{RESET}",
        f"{AZUL}|{RESET}  {VERDE}[3.]{RESET} Calcular estadísticas 📊    {AZUL}|{RESET}",
        f"{AZUL}|{RESET}  {ROJO}[4.] Salir{RESET} ❌                    {AZUL}|{RESET}",
        f"{AZUL}+___________________________________+{RESET}"
    ]

    for linea in lineas_menu:
        print(linea)
        time.sleep(0.06) # Pausa visual entre líneas

    # Uso de sys para el prompt de selección
    sys.stdout.write(f"\n{AMARILLO}👉 Selecciona una opción (1-4): {RESET}")
    sys.stdout.flush()
    opcion = sys.stdin.readline().strip()

    if opcion == "1":
        print(f"\n{VERDE}➕ Acción: Agregando productos...{RESET}")
        while True:
            nombre = input("\nNombre: ")
            try:
                precio = float(input("Precio: "))
                cantidad = int(input("Cantidad: "))
                producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
                inventario.append(producto)
                print(f"✅ {VERDE}Guardado:{RESET} {nombre}")
            except ValueError:
                print(f"{ROJO}⚠️ Error: Ingresa números válidos.{RESET}")
            nombre = input(f"\n{VERDE}[1]Continuar [2]Salir\n: {RESET}")
            if nombre.lower() == '2': break
            elif nombre.lower() == '1': continue
    # La Opcion 2 de Mostrar Inventario
    elif opcion == "2":
        escribir_suave(f"\n{AZUL}📋 INVENTARIO ACTUAL...{RESET}")
        if not inventario:
            print("   El inventario está vacío.")
        else:
            for i, p in enumerate(inventario, 1):
                print(f"   {i}. Producto {p['nombre']} | Precio: ${p['precio']} | Stock: {p['cantidad']}")
        time.sleep(1)
    # La Opcion 3 de Calcular estadisticas
    elif opcion == "3":
        escribir_suave(f"\n{AMARILLO}📈 CALCULANDO REPORTE ESTADÍSTICO...{RESET}")
        time.sleep(0.5)
        if not inventario:
            print("   No hay datos para calcular.")
        else:
            total_items = len(inventario)
            valor_total_stock = sum(p['precio'] * p['cantidad'] for p in inventario)
            cantidad_total = sum(p['cantidad'] for p in inventario)
            
            print(f"   • Productos distintos: {total_items}")
            print(f"   • Valor total del inventario: ${valor_total_stock:,.2f}")
            print(f"   • Cantidad Total de Producto: {cantidad_total}")
        time.sleep(1)
    # La Opcion 4 de Salir 
    elif opcion == "4":
        escribir_suave(f"\n{ROJO}👋 Cerrando sesión. ¡Que tengas un gran día!{RESET}")
        time.sleep(0.8)
        sys.exit() # Salida limpia usando la librería sys
        
    else:
        print(f"\n{ROJO}⚠️  ERROR: '{opcion}' no es válido. Intenta de nuevo.{RESET}")
        time.sleep(1)
