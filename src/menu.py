# Definición de colores simples (Códigos ANSI)
VERDE = "\033[92m"
AMARILLO = "\033[93m"
AZUL = "\033[94m"
ROJO = "\033[91m"
RESET = "\033[0m"

while True:
    print(f"\n{AZUL}+-----------------------------------+{RESET}")
    print(f"{AZUL}|{RESET} {AZUL}📦 MENÚ DE GESTIÓN DEL INVENTARIO{RESET} {AZUL}|{RESET}")
    print(f"{AZUL}|-----------------------------------|{RESET}")
    print(f"{AZUL}|{RESET}  {VERDE}[1.]{RESET} Agregar producto ✨         {AZUL}|{RESET}")
    print(f"{AZUL}|{RESET}  {VERDE}[2.]{RESET} Mostrar inventario 📋       {AZUL}|{RESET}")
    print(f"{AZUL}|{RESET}  {VERDE}[3.]{RESET} Calcular estadísticas 📊    {AZUL}|{RESET}")
    print(f"{AZUL}|{RESET}  {ROJO}[4.] Salir{RESET} ❌                    {AZUL}|{RESET}")
    print(f"{AZUL}+___________________________________+{RESET}")
    
    opcion = input(f"\n{AMARILLO}👉 Selecciona una opción (1-4): {RESET}")

    if opcion == "1":
        print(f"\n{VERDE}➕ Acción: Agregando un nuevo producto...{RESET}")
    elif opcion == "2":
        print(f"\n{AZUL}📦 Acción: Consultando la base de datos...{RESET}")
    elif opcion == "3":
        print(f"\n{AMARILLO}📈 Acción: Generando reporte estadístico...{RESET}")
    elif opcion == "4":
        print(f"\n{ROJO}👋 Cerrando sesión. ¡Que tengas un gran día!{RESET}")
        break
    else:
        print(f"\n{ROJO}⚠️  ERROR: '{opcion}' no es válido. Intenta de nuevo.{RESET}")