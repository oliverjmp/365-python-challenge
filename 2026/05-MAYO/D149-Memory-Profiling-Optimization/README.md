# D149 - Memory Profiling & Optimization

Este hito implementa herramientas de **perfilamiento y optimización de uso de memoria RAM** en operaciones analíticas con `Pandas`, utilizando la librería nativa de Python `tracemalloc` para auditar picos de asignación de memoria.

## Características Principales
- **Auditoría de Memoria en Vivo:** Mide con precisión quirúrgica los picos de consumo de RAM (en megabytes) durante la ejecución de funciones pesadas.
- **Optimización Automática de Tipos de Datos:** Convierte enteros y flotantes a subtipos de menor capacidad (ej. de `int64` a `int8`/`int16`) y columnas de texto de alta repetición a estructuras categóricas (`category`).
- **Análisis de Huella de Memoria Profunda:** Cálculo preciso del consumo interno de objetos mediante la inspección avanzada de DataFrames (`deep=True`).

## 💡 ¿Para qué se usa y Casos de Uso Prácticos?
Optimizar la memoria RAM es vital en entornos de Big Data y microservicios con recursos limitados para evitar errores del sistema por saturación (`OutOfMemory / OOM`).

### Ejemplos de Uso:
1. **Procesamiento de Archivos CSV/Parquet Masivos:**
   * *Caso:* Reducir la huella de memoria de datasets corporativos antes de enviarlos a modelos de Machine Learning o motores de bases de datos.
2. **Optimización de Contenedores Docker (ML Microservices):**
   * *Caso:* Asegurar que los microservicios de inferencia consuman menos memoria dentro de entornos cloud restringidos.

## 📂 Estructura del Proyecto
```text
D149-Memory-Profiling-Optimization/
│
├── src/
│   ├── __init__.py
│   └── memory_profiler.py
├── tests/
│   └── test_memory.py
├── run_profiler.py
├── requirements.txt
└── README.md