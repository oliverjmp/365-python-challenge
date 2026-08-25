# Arquitectura de Evolución Automática de Esquemas con PyArrow

## 🎯 Objetivo
Gestionar de forma transparente la llegada incremental de archivos Parquet tabulares donde los esquemas evolucionan con el tiempo (adición de nuevas columnas de negocio, cambios de tipos compatibles) sin romper los pipelines analíticos posteriores en DuckDB o Pandas.

## 🔄 Funcionamiento del Motor (`SchemaEvolutionManager`)
1. **Escaneo Dinámico**: Utiliza `pyarrow.dataset.dataset()` apuntando al directorio de origen para inspeccionar todos los fragmentos Parquet de manera unificada.
2. **Unificación de Esquema (Schema Evolution)**: Al escanear, PyArrow reconcilia las diferencias estructurales entre particiones/archivos. Las columnas ausentes en lotes antiguos se rellenan automáticamente con valores nulos (`null`).
3. **Consolidación**: Exporta un único `pa.Table` listo para ingesta analítica.