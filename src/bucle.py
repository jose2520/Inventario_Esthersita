"""
📝 Descripción de cada componente
 * main.py (La Fachada):
   * Contiene el bucle while True.
   * Se encarga de la interacción directa con el usuario (inputs y prints).
   * Importa a funciones.py y archivo.py.
   * Su objetivo: Orquestar el flujo, no procesar datos.
 * funciones.py (El Cerebro):
   * Contiene la lista inventario = [].
   * Define cómo se calcula el producto más caro, cómo se fusionan los datos y las validaciones de negocio (ej. que el precio no sea negativo).
   * No sabe que los datos vienen de un JSON o un CSV, solo recibe y entrega diccionarios.
 * archivo.py (El Almacén):
   * Contiene las funciones cargar_datos, guardar_datos, exportar_csv.
   * Usa las librerías json y csv.
   * Es el único lugar donde se abren archivos (open()).
 * README.md (La Guía):
   * Explica cómo ejecutar el programa.
   * Lista las librerías necesarias (en este caso, solo las estándar de Python).
💡 Tips para trabajar en VS Code
 * Entorno Virtual: Te recomiendo crear uno para mantener tus librerías aisladas. En la terminal de VS Code escribe:
   python -m venv venv
 * Extensiones: Asegúrate de tener instalada la extensión oficial de Python (de Microsoft) y Rainbow CSV para leer tus archivos exportados con colores directamente en el editor.
 * Debugger: Usa el "Run and Debug" (F5) de VS Code. Es mucho más eficiente que llenar el código de print() para encontrar errores en la lógica de las estadísticas o la carga de archivos.
¿Te gustaría que te ayude a redactar el contenido del archivo README.md para que tu proyecto se vea aún más profesional?"""