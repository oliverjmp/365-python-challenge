import os
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from typing import Generator

class CSVParquetBatchConverter:
    """Motor de conversión por lotes de CSV a Parquet usando generadores de Python."""
    
    def __init__(self, raw_dir: str = "data_lake/raw", processed_dir: str = "data_lake/processed"):
        self.raw_dir = raw_dir
        self.processed_dir = processed_dir
        os.makedirs(self.raw_dir, exist_ok=True)
        os.makedirs(self.processed_dir, exist_ok=True)
        self._generar_csv_prueba_si_no_existe()

    def _generar_csv_prueba_si_no_existe(self):
        """Crea un fichero CSV de prueba masivo si no existe en la capa raw."""
        csv_path = os.path.join(self.raw_dir, "dataset_gigante.csv")
        if not os.path.exists(csv_path):
            df_dummy = pd.DataFrame({
                "id": range(1, 10001),
                "categoria": ["A", "B", "C", "D"] * 2500,
                "valor": [i * 1.5 for i in range(1, 10001)],
                "timestamp": pd.date_range(start="2026-01-01", periods=10000, freq="min")
            })
            df_dummy.to_csv(csv_path, index=False)

    def leer_csv_por_lotes(self, csv_filename: str, chunksize: int = 2000) -> Generator[pd.DataFrame, None, None]:
        """Generador que lee un fichero CSV por fragmentos (chunks) para ahorrar memoria RAM."""
        csv_path = os.path.join(self.raw_dir, csv_filename)
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"El fichero CSV no existe en la ruta: {csv_path}")
            
        for chunk in pd.read_csv(csv_path, chunksize=chunksize):
            yield chunk

    def convertir_a_parquet(self, csv_filename: str, parquet_filename: str, chunksize: int = 2000) -> int:
        """Convierte un CSV por lotes a Parquet usando el generador y PyArrow."""
        parquet_path = os.path.join(self.processed_dir, parquet_filename)
        writer = None
        total_filas = 0
        
        try:
            for chunk in self.leer_csv_por_lotes(csv_filename, chunksize=chunksize):
                table = pa.Table.from_pandas(chunk)
                if writer is None:
                    writer = pq.ParquetWriter(parquet_path, table.schema)
                writer.write_table(table)
                total_filas += len(chunk)
        finally:
            if writer is not None:
                writer.close()
                
        return total_filas