import pyarrow as pa
import pandas as pd

class ArrowMemoryManagementSubsystem:
    """Subsistema 1: Control de piscinas de memoria y asignación de búferes."""
    def get_active_pool_stats(self) -> dict:
        pool = pa.default_memory_pool()
        return {
            "backend": pool.backend_name,
            "bytes_allocated": pool.bytes_allocated()
        }

class ColumnarIngestionSubsystem:
    """Subsistema 2: Ingesta y conversión eficiente a tablas Arrow in-memory."""
    def ingest_to_arrow(self, df: pd.DataFrame) -> pa.Table:
        if df.empty:
            raise ValueError("El DataFrame de entrada está vacío.")
        return pa.Table.from_pandas(df)

class AnalyticalProcessingSubsystem:
    """Subsistema 3: Ejecución de operaciones analíticas sobre el núcleo columnar."""
    def compute_metrics(self, table: pa.Table) -> dict:
        df = table.to_pandas()
        return {
            "total_rows": len(df),
            "columns": list(df.columns),
            "memory_footprint_bytes": table.nbytes
        }