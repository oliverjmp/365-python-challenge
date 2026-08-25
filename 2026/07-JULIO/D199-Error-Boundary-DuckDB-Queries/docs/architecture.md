# Arquitectura del Sistema de Control de Errores (Error Boundary)

## 🎯 Objetivo
Proveer una capa robusta de aislamiento de fallos (**Error Boundary**) para la ejecución de consultas analíticas sobre DuckDB, transformando errores nativos opacos en **Excepciones Personalizadas** tipadas (`SQLSyntaxError`, `QueryExecutionError`) que faciliten el registro (logging), la auditoría y la resiliencia del pipeline.

## 🔄 Componentes del Sistema
1. **Jerarquía de Excepciones (`src/exceptions.py`):** Define excepciones base y específicas para sintaxis (`SQLSyntaxError`) y fallos de ejecución lógicos (`QueryExecutionError`).
2. **Ejecutor Seguro (`src/query_runner.py`):** Captura las excepciones de bajo nivel de DuckDB y las envuelve de manera limpia inyectando metadatos útiles (como la consulta fallida).