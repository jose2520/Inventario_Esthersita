## 📂 Estructura del Árbol de Directorios

A continuación se detalla la organización de los archivos del proyecto:

PROYECTO_INVENTARIO/
│
├── menu.py                 # Interfaz de usuario (Menú principal y navegación)
├── funciones.py            # Lógica de negocio (CRUD, Estadísticas y Fusión)
├── archivo.py              # Gestión de persistencia (Lectura/Escritura JSON y CSV)
├── inventario.json         # Base de datos local (Generado automáticamente)
└── README.md               # Documentación del proyecto

# 📦 Sistema de Gestión de Inventario (Python)

¡Bienvenido al **Sistema de Gestión de Inventario JOS.dev**! Esta es una aplicación de consola robusta desarrollada en Python, diseñada para administrar productos, controlar existencias y generar reportes financieros detallados.

## 🚀 Características Principales

* **Gestión Completa (CRUD):** Agregar, mostrar, editar y eliminar productos por nombre.
* **Búsqueda Inteligente:** Localiza productos instantáneamente con detalles de subtotal.
* **Reportes Estadísticos:** * Cálculo de inversión total (usando funciones `lambda`).
    * Identificación automática del producto más caro y el de mayor stock.
* **Persistencia de Datos:** * Guardado automático en formato **JSON**.
    * Exportación masiva a **CSV** (compatible con Excel).
    * Importación de datos externos con lógica de **Fusión Inteligente** (suma de stock y actualización de precios).
* **Interfaz Atractiva:** Menú visual con bordes dobles y códigos de colores ANSI para una mejor experiencia de usuario.

## 🛠️ Estructura del Proyecto

El proyecto sigue una arquitectura modular para facilitar su mantenimiento:

* `menu.py`: Interfaz de usuario y flujo principal del programa.
* `funciones.py`: Lógica de negocio, cálculos estadísticos y gestión de la lista en memoria.
* `archivo.py`: Módulo especializado en la lectura y escritura de archivos (JSON/CSV).
* `inventario.json`: Archivo de base de datos local generado automáticamente.

## 📋 Requisitos

* **Python 3.8 o superior.**
* No requiere librerías externas (usa módulos estándar: `os`, `json`, `csv`, `time`, `sys`).

## 💻 Instalación y Uso

1. **Clona este repositorio o descarga los archivos:**
    ```bash
    git clone [https://github.com/jose2520/Inventario_Esthersita.git](https://github.com/jose2520/Inventario_Esthersita.git) 