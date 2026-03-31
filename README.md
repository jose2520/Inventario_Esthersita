# Inventario_Esthersita
aplicación de consola creado con python para gestionar el inventario de una empresa


INVENTARIO ESTHERSITA/
├── .vscode/                # Configuración de VS Code (formateo, debugger)
│   └── settings.json
├── src/                    # Código fuente (o el nombre de tu paquete)
│   ├── __init__.py         # Convierte la carpeta en un paquete de Python
│   ├── main.py             # Punto de entrada de la aplicación
│   ├── core/               # Lógica principal y reglas de negocio
│   │   ├── __init__.py
│   │   └── logic.py
│   ├── utils/              # Funciones auxiliares (helpers)
│   │   ├── __init__.py
│   │   └── helpers.py
│   └── api/ / data/        # Conexiones externas o bases de datos
├── tests/                  # Pruebas unitarias y de integración
│   ├── __init__.py
│   └── test_main.py
├── .env                    # Variables de entorno (claves, tokens) - ¡Ignorar en Git!
├── .gitignore              # Archivos a ignorar (venv/, __pycache__/, .env)
├── requirements.txt        # Lista de librerías instaladas (pip install -r)
├── README.md               # Instrucciones del proyecto
└── venv/                   # Entorno virtual (generado automáticamente)







PROYECTO_INVENTARIO/
│
├── data/                    # Carpeta para persistencia (Task 4 y 5)
│   └── inventario.csv       # Archivo generado por guardar_csv()
│
├── src/                     # Código fuente modularizado (Task 2)
│   ├── __init__.py          # Convierte la carpeta en un paquete
│   ├── app.py               # Menú principal y bucle while (Task 1 y 6)
│   ├── servicios.py         # CRUD y Estadísticas con Lambdas (Task 2 y 3)
│   └── archivos.py          # Lógica de Guardar/Cargar CSV y Try/Except (Task 4 y 5)
│
├── docs/                    # (Opcional) Para organizar tus entregables
│   └── diagrama_flujo.png   # El diagrama de flujo de draw.io (Task 1)
│
└── README.md                # Descripción del proyecto y objetivos del módulo



PROYECTO_INVENTARIO/             <-- Carpeta principal (Abrir en VS Code)
│
├── .gitignore                   # Para ignorar archivos basura (__pycache__)
├── README.md                    # Descripción de tu proyecto (Buen hábito)
│
├── data/                        # CARPETA PARA PERSISTENCIA (S3)
│   └── inventario.csv           # Aquí se guardan tus productos (Task 4 y 5)
│
├── docs/                        # CARPETA DE ENTREGABLES
│   ├── diagrama_semana1.png     # Task 1 - Semana 1
│   └── diagrama_final.png       # Task 1 - Semana 3 (CRUD completo)
│
└── src/                         # CARPETA DE CÓDIGO FUENTE (Task 2 - S3)
    ├── __init__.py              # Archivo vacío (Hace que src sea un paquete)
    ├── app.py                   # EL MENÚ: if/elif, while, inputs (S1, S2, S3)
    ├── servicios.py             # LA LÓGICA: CRUD, Lambdas, Estadísticas (S2, S3)
    └── archivos.py              # LOS ARCHIVOS: Guardar/Cargar, Try/Except (S3)
