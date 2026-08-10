# Módulo D91: Great Expectations Contracts (`Great Expectations + Python`)

## Descripción General
Este módulo implementa un **motor de contratos de datos** para la validación estricta de esquemas, tipos y restricciones en pipelines ETL. Su propósito es actuar como una barrera de calidad automatizada que intercepta anomalías estructurales antes de la persistencia.

---

## Características Principales
* **Definición de Esquemas**: Reglas declarativas por columna (tipos de datos y nulabilidad).
* **Validación por Lotes**: Auditoría completa de registros devolviendo un desglose detallado de errores por índice de fila.
* **Pruebas Automatizadas**: Verificación de integridad para conjuntos de datos válidos e inválidos.

---

## Estructura del Proyecto
```text
D91-Great-Expectations-Contracts/
├── src/
│   ├── __init__.py
│   └── data_contract.py # Motor de validación de contratos de datos
├── tests/
│   ├── __init__.py
│   └── test_data_contract.py # Pruebas unitarias de cumplimiento de esquemas
├── requirements.txt # Dependencias del proyecto
└── README.md        # Documentación técnica del módulo