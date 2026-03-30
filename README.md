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
