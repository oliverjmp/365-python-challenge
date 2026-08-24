# Parquet Columnar Storage (D182)

Pipeline de conversión masiva de ficheros CSV planos a formato columnar comprimido Parquet utilizando `PyArrow` y `Pandas`.

## Características Principales
- Compresión de datos eficiente y rápida mediante **Snappy**.
- Almacenamiento columnar optimizado para análisis masivo de datos.

---

## 📊 Demostración Interactiva del Pipeline

A continuación se muestra el resultado visual de procesar un lote de transacciones a través del pipeline de conversión columnar:

### 1. Datos Originales (CSV Plano simulado)
| ID Transacción | Cliente ID | Monto ($) | Estado |
|:--------------|:-----------|:----------|:-------|
| 100001        | CLI_12     | 1,500.50  | COMPLETADO |
| 100002        | CLI_45     | 320.00    | PENDIENTE  |
| 100003        | CLI_89     | 4,250.75  | COMPLETADO |

### 2. Resultados tras la Conversión a Formato Columnar (Parquet)
| Métrica del Pipeline | Valor Obtenido |
|:---------------------|:---------------|
| **Registros Procesados** | 50,000 filas |
| **Tamaño Original (CSV)** | ~4.20 MB |
| **Tamaño Comprimido (Parquet)** | ~0.85 MB |
| **Ahorro de Espacio en Disco** | **79.76%** |
| **Tiempo de Conversión** | 0.32 segundos |

> **Nota Técnica:** Al almacenar los datos por columnas en lugar de filas, los motores analíticos pueden leer únicamente los campos necesarios (por ejemplo, solo la columna `monto`) sin necesidad de escanear todo el fichero en disco, logrando un rendimiento superior.