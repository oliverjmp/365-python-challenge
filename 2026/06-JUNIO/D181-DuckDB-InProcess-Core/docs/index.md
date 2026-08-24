# DuckDB In-Process Core (D181)

Inicialización de base de datos analítica *in-process* y ejecución de consultas SQL de alta velocidad utilizando DuckDB y Python.

## Características
- Consultas SQL ultrarrápidas embebidas en Python.
- Análisis de datos sin necesidad de servidores externos.

---

## 📊 Demostración Interactiva del Motor Analítico

A continuación se muestra el resultado de una consulta SQL ejecutada en tiempo real sobre una tabla de prueba en memoria utilizando DuckDB:

| ID | Categoría | Valor Registrado |
|:---|:----------|:-----------------|
| 1  | A         | 10.5             |
| 2  | B         | 20.0             |
| 3  | A         | 15.2             |

### Resultado de la Agrupación (SUM por Categoría)
| Categoría | Suma Total de Valores |
|:----------|:----------------------|
| **A**     | 25.7                  |
| **B**     | 20.0                  |