import funciones
import archivo
import os
import time
import sys

# --- CONFIGURACIÓN INICIAL ---
inventario = funciones.cargar_datos()
VERDE, AMARILLO, AZUL, ROJO, RESET = "\033[92m", "\033[93m", "\033[94m", "\033[91m", "\033[0m"

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# --- BUCLE PRINCIPAL ---
while True:
    limpiar_pantalla()
    
    print(f"{AZUL}╔═══════════════════════════════════════════╗{RESET}")
    print(f"{AZUL}║{RESET}   📦 SISTEMA DE GESTIÓN DE INVENTARIO     {AZUL}║{RESET}")
    print(f"{AZUL}╠═══════════════════════════════════════════╣{RESET}")
    print(f"{AZUL}║{RESET} {VERDE}▸[1]{RESET} Agregar nuevo producto ✨            {AZUL}║{RESET}")
    print(f"{AZUL}║{RESET} {VERDE}▸[2]{RESET} Mostrar inventario completo 📋       {AZUL}║{RESET}")
    print(f"{AZUL}║{RESET} {AZUL}▸[3]{RESET} Buscar producto (por nombre) 🔍      {AZUL}║{RESET}")
    print(f"{AZUL}║{RESET} {AMARILLO}▸[4]{RESET} Editar producto (por nombre) ✏️       {AZUL}║{RESET}")
    print(f"{AZUL}║{RESET} {ROJO}▸[5]{RESET} Eliminar producto (por nombre) 🗑️     {AZUL}║{RESET}")
    print(f"{AZUL}║{RESET} {AZUL}▸[6]{RESET} Ver reporte de estadísticas 📊       {AZUL}║{RESET}")
    print(f"{AZUL}║{RESET} {AZUL}▸[7]{RESET} Exportar inventario a CSV 📄         {AZUL}║{RESET}")
    print(f"{AZUL}║{RESET} {AZUL}▸[8]{RESET} Importar datos desde CSV 📥          {AZUL}║{RESET}")
    print(f"{AZUL}║{RESET} {ROJO}▸[9]{RESET} Reiniciar todo el inventario 🔥      {AZUL}║{RESET}")
    print(f"{AZUL}║{RESET} {ROJO}▸[10]{RESET} Salir del sistema ❌                {AZUL}║{RESET}")
    print(f"{AZUL}╚═══════════════════════════════════════════╝{RESET}")

    opcion = input(f"\n{AMARILLO}👉 Selecciona una opción (1-10): {RESET}").strip()

    if opcion == "1":
        funciones.agregar_producto(inventario)
        funciones.guardar_datos(inventario)
        time.sleep(1.2)

    elif opcion == "2":
        funciones.mostrar_inventario(inventario)
        input(f"\n{AZUL}Presiona Enter para volver al menú...{RESET}")

    elif opcion == "3":
        funciones.interfaz_buscar_producto(inventario)
        input(f"\n{AZUL}Presiona Enter para volver...{RESET}")

    elif opcion == "4":
        funciones.actualizar_producto(inventario)
        funciones.guardar_datos(inventario)
        time.sleep(1.5)

    elif opcion == "5":
        funciones.eliminar_producto(inventario)
        funciones.guardar_datos(inventario)
        time.sleep(1.5)

    elif opcion == "6":
        stats = funciones.calcular_estadisticas(inventario)
        if stats:
            print(f"\n{AMARILLO}📊 REPORTE ESTADÍSTICO DETALLADO{RESET}")
            print(f"---------------------------------------")
            print(f"📦 Unidades totales: {stats['unidades_totales']}")
            print(f"💰 Valor total:      ${stats['valor_total']:,.2f}")
            print(f"💎 Más caro:         {stats['producto_mas_caro']['nombre']} (${stats['producto_mas_caro']['precio']})")
            print(f"📈 Mayor stock:      {stats['producto_mayor_stock']['nombre']} ({stats['producto_mayor_stock']['cantidad']} unds)")
            print(f"---------------------------------------")
        else:
            print(f"\n{ROJO}⚠️ Sin datos suficientes.{RESET}")
        input(f"\n{AZUL}Presiona Enter para continuar...{RESET}")

    elif opcion == "7":
        archivo.guardar_csv(inventario)
        time.sleep(2)

    elif opcion == "8":
        ruta = input(f"\n📂 Nombre del archivo (ej: datos.csv): ").strip()
        prods_nuevos, total_errores = archivo.cargar_csv(ruta)
        if prods_nuevos is not None:
            choice = input(f"¿Sobrescribir {ROJO}(S){RESET} o Fusionar {VERDE}(N){RESET}?: ").strip().upper()
            if choice == 'S':
                inventario[:] = prods_nuevos
            else:
                funciones.fusionar_inventarios(inventario, prods_nuevos)
            funciones.guardar_datos(inventario)
            print(f"\n{VERDE}✅ Carga completada.{RESET}")
        input(f"\n{AZUL}Presiona Enter para volver...{RESET}")

    elif opcion == "9":
        funciones.reiniciar_inventario(inventario)
        time.sleep(1.5)

    elif opcion == "10":
        funciones.guardar_datos(inventario)
        print(f"\n{ROJO}👋 Saliendo...{RESET}")
        time.sleep(1)
        break

    else:
        print(f"\n{ROJO}⚠️ Error: Opción inválida.{RESET}")
        time.sleep(1.2)

sys.exit()