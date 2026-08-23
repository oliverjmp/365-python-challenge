# D167 - CSV Streaming con Python Generators

Procesador de visualización y análisis para datasets masivos en formato CSV que superan la capacidad de la memoria RAM, implementando flujos de datos por bloques (*chunking*) mediante generadores nativos de Python.

## Características Principales
- **Optimización de Memoria RAM:** Lectura diferida y por lotes utilizando generadores (`yield`) para evitar desbordamientos de memoria con ficheros gigantescos.
- **Procesamiento en Streaming:** Cálculo de agregaciones y métricas en tiempo real sobre flujos continuos de datos.
- **Pruebas Automatizadas:** Validación estricta del comportamiento de los generadores y la correcta lectura por bloques.

## 📂 Estructura del Proyecto
```text
D167-CSV-Streaming-Large-Datasets/
├── src/
│   ├── __init__.py
│   └── streamer.py
├── tests/
│   ├── __init__.py
│   └── test_streamer.py
├── app_stream.py
├── requirements.txt
└── README.md