import pyarrow as pa
import pandas as pd

class ArrowMemoryOptimizer:
    """Clase gestora para configurar, auditar y optimizar piscinas de memoria en PyArrow."""

    @staticmethod
    def get_available_memory_pools() -> list:
        """Retorna los nombres de los asignadores de memoria disponibles en el entorno."""
        return [pa.default_memory_pool().backend_name]

    @staticmethod
    def get_memory_pool_stats() -> dict:
        """Obtiene las estadísticas detalladas de uso de la piscina de memoria activa."""
        pool = pa.default_memory_pool()
        return {
            "backend_name": pool.backend_name,
            "bytes_allocated": pool.bytes_allocated(),
            "max_memory": pool.max_memory()
        }

    @staticmethod
    def process_large_dataset_with_pool(df: pd.DataFrame) -> tuple:
        """Simula una carga masiva utilizando el memory pool optimizado de Arrow."""
        pool = pa.default_memory_pool()
        initial_bytes = pool.bytes_allocated()
        
        table = pa.Table.from_pandas(df)
        
        allocated_during = pool.bytes_allocated()
        df_result = table.to_pandas()
        final_bytes = pool.bytes_allocated()
        
        metrics = {
            "initial_bytes": initial_bytes,
            "allocated_during": allocated_during,
            "final_bytes": final_bytes,
            "rows_processed": len(df_result)
        }
        return df_result, metrics