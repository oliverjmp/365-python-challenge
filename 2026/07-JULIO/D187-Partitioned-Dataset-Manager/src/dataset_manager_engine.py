import os
import time
import pyarrow as pa
import pyarrow.dataset as ds
import pandas as pd

class PartitionedDatasetManagerEngine:
    """
    Gestor de datasets particionados en disco utilizando PyArrow Datasets,
    optimizado para filtrado por fecha y región geográfica (Partition Pruning).
    """

    def __init__(self, base_path: str = "data_lake/partitioned_store"):
        self.base_path = base_path

    def escribir_dataset_particionado(self, num_filas: int = 100000) -> dict:
        """
        Genera un DataFrame y lo escribe en disco particionado por región y fecha.
        """
        print(f"[Partition Manager] Generando dataset masivo de {num_filas:,} registros...")
        
        regiones = ["AMERICA", "EUROPE", "ASIA"]
        fechas = ["2026-07-01", "2026-07-02", "2026-07-03"]
        
        data = {
            "transaccion_id": range(1, num_filas + 1),
            "region": [regiones[i % len(regiones)] for i in range(num_filas)],
            "fecha": [fechas[i % len(fechas)] for i in range(num_filas)],
            "monto": [round(float((i % 3000) + 10.50), 2) for i in range(num_filas)]
        }
        
        df = pd.DataFrame(data)
        tabla = pa.Table.from_pandas(df)

        inicio = time.time()
        # Escritura particionada utilizando PyArrow Dataset API
        ds.write_dataset(
            tabla,
            base_dir=self.base_path,
            format="parquet",
            partitioning=["region", "fecha"],
            existing_data_behavior="overwrite_or_ignore"
        )
        duracion = time.time() - inicio

        print(f" > Dataset particionado escrito con éxito en: {self.base_path} ({duracion * 1000:.2f} ms)")
        return {
            "filas_escritas": num_filas,
            "tiempo_escritura_ms": round(duracion * 1000, 2)
        }

    def leer_dataset_filtrado(self, region_filtro: str, fecha_filtro: str) -> dict:
        """
        Lee el dataset aplicando Partition Pruning (descarta directorios que no cumplen el filtro).
        """
        if not os.path.exists(self.base_path):
            raise FileNotFoundError(f"El directorio particionado no existe: {self.base_path}")

        # Cargar el dataset particionado desde disco
        dataset = ds.dataset(self.base_path, format="parquet", partitioning=["region", "fecha"])

        # Definir filtro de expresiones para lectura selectiva (Predicate Pushdown / Pruning)
        filtro = (ds.field("region") == region_filtro) & (ds.field("fecha") == fecha_filtro)

        inicio = time.time()
        # Leer únicamente las particiones coincidentes hacia una tabla Arrow y luego a Pandas
        tabla_filtrada = dataset.to_table(filter=filtro)
        df_resultado = tabla_filtrada.to_pandas()
        latencia = (time.time() - inicio) * 1000

        return {
            "latencia_ms": round(latencia, 2),
            "filas_recuperadas": len(df_resultado),
            "dataframe_resultados": df_resultado
        }