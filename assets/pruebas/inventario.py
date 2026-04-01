import sys
import time

# Colores
VERDE = "\033[32m"
AZUL = "\033[94m"
ROJO = "\033[91m"
AMARILLO = "\033[93m"
CYAN = "\033[36m"
RESET = "\033[0m"


# --- ENTRADA DINÁMICA ---

# 1. Animación del Título Principal
titulo = " REGISTRO DE PRODUCTO "
borde_t = f"+{'-' * len(titulo)}+"
print(f"{VERDE}{borde_t}")
for char in f"|{titulo}|":
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.02)
print(f"\n{borde_t}{RESET}")

# 2. Inputs Para Solicitar datos al Usuario..
nombre = input(f"{CYAN} | Nombre del producto | -> {RESET}")  
precio = float(input(f"{CYAN} | Precio unitario ($) | -> {RESET}"))
cantidad = int(input(f"{CYAN} | Stock disponible    | -> {RESET}"))

# Cálculo
costo_total = precio * cantidad

# --- MOSTRAR RESULTADO ---
# Creamos la línea de datos
datos = f" Producto: {nombre} | Precio: ${precio:.2f} | Stock: {cantidad} | Total: ${costo_total:.2f} "
borde_f = "-" * len(datos)

print(f"\n{VERDE}{borde_f}")
for char in f"|{datos}|":
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.02)
print(f"\n{borde_f}{RESET}\n")



