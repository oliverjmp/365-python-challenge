# Módulo D79: CSV Stream Processor (`Python Generators`)

## Descripción General
Este proyecto implementa un **procesador de ficheros CSV de gran tamaño (kilométricos)** utilizando **Generadores de Python** (`yield`). Su diseño permite leer y transformar flujos de datos masivos con un consumo mínimo de memoria RAM, evitando cargar archivos enteros en la memoria principal.

---

## Características Principales
* **Lectura en Streaming**: Procesamiento de archivos línea por línea mediante `csv.DictReader` y funciones generadoras.
* **Tuberías de Datos (*Pipelines*)**: Encadenamiento eficiente de múltiples generadores para filtrar y transformar información.
* **Eficiencia de Memoria**: Complejidad espacial de orden $O(1)$ constante frente al tamaño del archivo.
* **Pruebas Unitarias Exhaustivas**: Cobertura del 100% utilizando archivos CSV temporales.

---

## Estructura del Proyecto
```text
D79-CSV-Stream-Processor/
├── src/
│   ├── __init__.py
│   └── processor.py     # Lógica de generadores para lectura y filtrado de CSV
├── tests/
│   ├── __init__.py
│   └── test_processor.py # Pruebas unitarias con archivos temporales
├── requirements.txt     # Dependencias del proyecto
└── README.md            # Documentación técnica del módulo