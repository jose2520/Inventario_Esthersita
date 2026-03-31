# 1. Definimos la lista vacía al principio
inventario = []

VERDE = "\033[92m"
AMARILLO = "\033[93m"
AZUL = "\033[94m"
ROJO = "\033[91m"
RESET = "\033[0m"

while True:
    print(f"\n{AZUL}+-----------------------------------+{RESET}")
    print(f"{AZUL}|{RESET} {AZUL}📦 MENÚ DE GESTIÓN DEL INVENTARIO{RESET} {AZUL}|{RESET}")
    # ... (resto de tus prints del menú)
    
    opcion = input(f"\n{AMARILLO}👉 Selecciona una opción (1-4): {RESET}")

    if opcion == "1":
        print(f"\n{VERDE}➕ Acción: Agregando productos...{RESET}")
        while True:
            nombre = input(f"{VERDE}Nombre del producto (o 'fin' para volver): {RESET}")
            if nombre.lower() == 'fin':
                break
            
            try:
                precio = float(input(f"{VERDE}Precio: {RESET}"))
                cantidad = int(input(f"{VERDE}Cantidad: {RESET}"))
                
                # Creamos el diccionario y lo añadimos a la lista
                producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
                inventario.append(producto)
                print(f"✅ '{nombre}' añadido con éxito.\n")
            except ValueError:
                print(f"{ROJO}⚠️ Error: Precio y cantidad deben ser números.{RESET}")

    elif opcion == "2":
        print(f"\n{AZUL}📋 INVENTARIO ACTUAL:{RESET}")
        for p in inventario:
            print(f"• {p['nombre']}: ${p['precio']} (Stock: {p['cantidad']})")
        if not inventario:
            print("El inventario está vacío.")
    
    # ... (resto de tus elif)
