import tracemalloc
import pandas as pd
import numpy as np
from typing import Dict, Any, Tuple, Callable

class MemoryProfilerEngine:
    """Clase para perfilar y optimizar el consumo de memoria RAM en operaciones con Pandas."""

    @staticmethod
    def measure_memory_usage(func: Callable, *args: Any, **kwargs: Any) -> Tuple[Any, float]:
        """Mide la memoria máxima consumida (en MB) al ejecutar una función."""
        tracemalloc.start()
        try:
            result = func(*args, **kwargs)
            current, peak = tracemalloc.get_traced_memory()
        finally:
            tracemalloc.stop()
        
        peak_mb = peak / (1024 * 1024)
        return result, peak_mb

    def generate_heavy_dataframe(self, num_rows: int = 100_000) -> pd.DataFrame:
        """Genera un DataFrame analítico pesado con tipos de datos estándar (no optimizados)."""
        if num_rows <= 0:
            raise ValueError("El número de filas debe ser mayor a cero.")
        
        np.random.seed(42)
        data = {
            "id": np.arange(num_rows, dtype=np.int64),
            "categoria": np.random.choice(["A", "B", "C", "D"], size=num_rows),
            "valor_numerico": np.random.randn(num_rows) * 100,
            "activo": np.random.choice([True, False], size=num_rows)
        }
        return pd.DataFrame(data)

    def optimize_dataframe_memory(self, df: pd.DataFrame) -> pd.DataFrame:
        """Optimiza el uso de memoria de un DataFrame convirtiendo tipos de datos a subtipos eficientes."""
        if df.empty:
            raise ValueError("El DataFrame de entrada está vacío.")
        
        optimized_df = df.copy()
        
        for col in optimized_df.columns:
            col_type = optimized_df[col].dtype
            
            if col_type != object and not pd.api.types.is_datetime64_any_dtype(col_type):
                c_min = optimized_df[col].min()
                c_max = optimized_df[col].max()
                
                # Optimizar enteros
                if str(col_type).startswith("int"):
                    if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                        optimized_df[col] = optimized_df[col].astype(np.int8)
                    elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                        optimized_df[col] = optimized_df[col].astype(np.int16)
                    elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                        optimized_df[col] = optimized_df[col].astype(np.int32)
                
                # Optimizar flotantes
                elif str(col_type).startswith("float"):
                    if c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                        optimized_df[col] = optimized_df[col].astype(np.float32)
            
            # Optimizar objetos (strings) a categoría si tienen baja cardinalidad
            elif col_type == object:
                num_unique = optimized_df[col].nunique()
                num_total = len(optimized_df[col])
                if num_unique / num_total < 0.5:
                    optimized_df[col] = optimized_df[col].astype("category")
                    
        return optimized_df

    def get_memory_stats(self, df: pd.DataFrame) -> Dict[str, float]:
        """Calcula el uso total de memoria del DataFrame en MB y KB."""
        if df.empty:
            raise ValueError("El DataFrame está vacío.")
        
        memory_bytes = df.memory_usage(deep=True).sum()
        return {
            "bytes": float(memory_bytes),
            "kb": float(memory_bytes / 1024),
            "mb": float(memory_bytes / (1024 * 1024))
        }