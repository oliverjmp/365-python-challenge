# D105 - Outlier Detection Engine

Este proyecto implementa un **motor estadístico automatizado para la detección y tratamiento de valores atípicos (Outliers)** utilizando **NumPy** y **SciPy**.

## Características Principales
- **Análisis Estadístico Avanzado:** Implementación de métodos de Z-score (SciPy) y Rango Intercuartílico - IQR (NumPy).
- **Tratamiento Automatizado:** Limpieza e imputación de valores anómalos basada en la mediana de la distribución robusta.
- **Pruebas Unitarias Rigurosas:** Cobertura de código validada al 100% mediante `pytest` y `tmp_path`.

## Requisitos del Entorno
- Python 3.11 o superior.
- Librerías especificadas en `requirements.txt`:
  ```text
  numpy==1.26.4
  scipy==1.12.0
  pandas==2.2.1
  pytest==8.1.1
  pytest-cov==4.1.0