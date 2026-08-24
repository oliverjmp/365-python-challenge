import os
import pandas as pd

try:
    import pyarrow as pa
    import pyarrow.parquet as pq
    PYARROW_AVAILABLE = True
except ImportError:
    PYARROW_AVAILABLE = False

class ParquetPipeline:
    """Pipeline para convertir archivos CSV planos a formato columnar Parquet."""

    def __init__(self, compression: str = "SNAPPY"):
        if not PYARROW_AVAILABLE:
            raise ImportError("PyArrow no está instalado en el entorno.")
        self.compression = compression

    def convert_csv_to_parquet(self, csv_path: str, parquet_path: str) -> bool:
        """Convierte un archivo CSV en un archivo Parquet comprimido."""
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"El archivo CSV de origen no existe: {csv_path}")
        
        # Leer CSV usando Pandas
        df = pd.read_csv(csv_path)
        if df.empty:
            raise ValueError("El archivo CSV está vacío y no se puede convertir.")

        # Escribir a Parquet
        df.to_parquet(parquet_path, compression=self.compression, index=False)
        return True