# Módulo D86: Process Pool Matrix Math (`multiprocessing`)

## Descripción General
Este módulo implementa **procesamiento paralelo intensivo** en Python utilizando el módulo `multiprocessing`. Su propósito es delegar operaciones numéricas pesadas (como el cálculo matricial) a múltiples núcleos del procesador de forma simultánea, maximizando el rendimiento computacional.

---

## Características Principales
* **Paralelismo Real**: División de cargas de trabajo a nivel de filas utilizando `multiprocessing.Pool` para evadir el GIL.
* **Funciones Auxiliares Modulares**: Uso de funciones de nivel superior para garantizar la serialización correcta (*pickling*) entre procesos.
* **Pruebas Automatizadas**: Verificación de integridad numérica en entornos concurrentes.

---

## Estructura del Proyecto
```text
D86-Process-Pool-Matrix-Math/
├── src/
│   ├── __init__.py
│   └── matrix_processor.py # Lógica de distribución de tareas con Process Pool
├── tests/
│   ├── __init__.py
│   └── test_matrix_processor.py # Pruebas unitarias de operaciones matriciales
├── requirements.txt # Dependencias del proyecto
└── README.md        # Documentación técnica del módulo