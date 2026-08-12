# D104 - Data Cleaning Pipeline Pro

Este proyecto implementa un **pipeline masivo de limpieza y tratamiento de valores nulos aplicando operaciones vectorizadas** en Pandas.

## Características Principales
- **Vectorización con Pandas:** Procesamiento eficiente y optimizado de DataFrames sin bucles costosos.
- **Tratamiento Inteligente de Nulos:** Imputación de medianas para variables numéricas y valores por defecto controlados (`Unknown`, `Unnamed Product`, `0`) para variables cualitativas y faltantes.
- **Pruebas Unitarias Rigurosas:** Cobertura de código validada al 100% mediante `pytest` y `tmp_path`.

## Requisitos del Entorno
- Python 3.11 o superior.
- Librerías especificadas en `requirements.txt`:
  ```text
  pandas==2.2.1
  pytest==8.1.1
  pytest-cov==4.1.0