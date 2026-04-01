import funciones
import time
import sys
import os

# --- SECCIÓN 1: CONFIGURACIÓN Y VARIABLES GLOBALES ---
# Cargamos el inventario desde el archivo JSON al iniciar
inventario = funciones.cargar_datos()

# Códigos ANSI para personalizar la estética de la consola
VERDE, AMARILLO, AZUL, ROJO, RESET = "\033[92m", "\033[93m", "\033[94m", "\033[91m", "\033[0m"

# --- SECCIÓN 2: FUNCIONES DE INTERFAZ ---
def escribir_suave(texto, velocidad=0.03):
    """Crea una animación de escritura mecánica para mensajes especiales."""
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(velocidad)
    print()

def limpiar_pantalla():
    """Limpia la terminal para mantener una interfaz limpia."""
    os.system('cls' if os.name == 'nt' else 'clear')

# --- SECCIÓN 3: BUCLE PRINCIPAL Y MENÚ ---
while True:
    limpiar_pantalla()
    
    lineas_menu = [
        f"\n{AZUL}+-----------------------------------+{RESET}",
        f"{AZUL}|{RESET} {AZUL}📦 SISTEMA DE GESTIÓN (v2.0){RESET}    {AZUL}|{RESET}",
        f"{AZUL}|-----------------------------------|{RESET}",
        f"{AZUL}|{RESET}  {VERDE}[1.]{RESET} Agregar producto ✨         {AZUL}|{RESET}",
        f"{AZUL}|{RESET}  {VERDE}[2.]{RESET} Mostrar inventario 📋       {AZUL}|{RESET}",
        f"{AZUL}|{RESET}  {AMARILLO}[3.]{RESET} Editar por nombre ✏️         {AZUL}|{RESET}",
        f"{AZUL}|{RESET}  {ROJO}[4.]{RESET} Eliminar por nombre 🗑️       {AZUL}|{RESET}",
        f"{AZUL}|{RESET}  {VERDE}[5.]{RESET} Ver reporte estadístico 📊  {AZUL}|{RESET}",
        f"{AZUL}|{RESET}  {ROJO}[6.]{RESET} Reiniciar Inventario 🔥     {AZUL}|{RESET}",
        f"{AZUL}|{RESET}  {ROJO}[7.] Salir del sistema ❌        {AZUL}|{RESET}",
        f"{AZUL}+___________________________________+{RESET}"
    ]

    for linea in lineas_menu:
        print(linea)

    sys.stdout.write(f"\n{AMARILLO}👉 Opción seleccionada: {RESET}")
    sys.stdout.flush()
    opcion = sys.stdin.readline().strip()

    # --- SECCIÓN 4: LÓGICA DE OPCIONES ---
    if opcion == "1":
        funciones.agregar_producto(inventario)
        funciones.guardar_datos(inventario)
        time.sleep(1.2)

    elif opcion == "2":
        funciones.mostrar_inventario(inventario)
        input(f"\n{AZUL}Presiona Enter para volver al menú...{RESET}")

    elif opcion == "3":
        funciones.actualizar_producto(inventario)
        funciones.guardar_datos(inventario)
        time.sleep(1.5)

    elif opcion == "4":
        funciones.eliminar_producto(inventario)
        funciones.guardar_datos(inventario)
        time.sleep(1.5)

    elif opcion == "5":
        # Ahora recibimos los datos (diccionario) que retorna la función
        stats = funciones.calcular_estadisticas(inventario)
        print(f"\n{AMARILLO}📊 REPORTE DE MÉTRICAS{RESET}")
        print(f"   • Productos distintos: {stats['total_items']}")
        print(f"   • Unidades en total:   {stats['stock_total']}")
        print(f"   • Inversión total:     ${stats['valor_total']:,.2f}")
        input(f"\n{AZUL}Presiona Enter para continuar...{RESET}")

    elif opcion == "6":
        funciones.reiniciar_inventario(inventario)
        time.sleep(1.5)

    elif opcion == "7":
        funciones.guardar_datos(inventario)
        escribir_suave(f"\n{ROJO}👋 Guardando cambios y saliendo...{RESET}")
        time.sleep(0.8)
        break
        
    else:
        print(f"\n{ROJO}⚠️  ERROR: '{opcion}' no es una opción válida.{RESET}")
        time.sleep(1.2)

# Cierre definitivo del programa
sys.exit()