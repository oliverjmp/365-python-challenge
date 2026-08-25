import os
import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd

class SchemaEvolutionManager:
    """Gestor para la lectura, escritura y unificación automática de esquemas con PyArrow."""

    def __init__(self, dataset_dir: str = "data_lake"):
        self.dataset_dir = dataset_dir
        os.makedirs(self.dataset_dir, exist_ok=True)

    def guardar_lote_inicial(self, filename: str = "raw_lote_1.parquet") -> str:
        """Genera un lote inicial de datos reales (v1: clientes base)."""
        file_path = os.path.join(self.dataset_dir, filename)
        df_v1 = pd.DataFrame({
            "cliente_id": [1, 2, 3],
            "nombre": ["Empresa Alpha S.A.", "Comercial Beta", "Industrias Gamma"],
            "segmento": ["Corporativo", "Pyme", "Enterprise"]
        })
        table = pa.Table.from_pandas(df_v1)
        pq.write_table(table, file_path)
        return file_path

    def guardar_lote_evolucionado(self, filename: str = "raw_lote_2.parquet") -> str:
        """Genera un segundo lote con evolución de esquema (v2: añade limite_credito y pais)."""
        file_path = os.path.join(self.dataset_dir, filename)
        df_v2 = pd.DataFrame({
            "cliente_id": [4, 5],
            "nombre": ["Delta Logistics", "Omega Tech"],
            "segmento": ["Pyme", "Corporativo"],
            "limite_credito": [45000.0, 120000.0],
            "pais": ["España", "México"]
        })
        table = pa.Table.from_pandas(df_v2)
        pq.write_table(table, file_path)
        return file_path

    def leer_dataset_unificado(self) -> pa.Table:
        """Lee todos los archivos Parquet y unifica sus esquemas de forma permisiva rellenando nulos."""
        if not os.listdir(self.dataset_dir):
            raise FileNotFoundError(f"No se encontraron archivos en el directorio: {self.dataset_dir}")

        archivos = [os.path.join(self.dataset_dir, f) for f in os.listdir(self.dataset_dir) if f.endswith('.parquet')]
        
        # Leemos cada tabla individualmente
        tablas = [pq.read_table(archivo) for archivo in archivos]
        
        # Concatenamos permitiendo la promoción de esquemas y rellenando vacíos con nulls
        tabla_unificada = pa.concat_tables(tablas, promote_options="permissive")
        
        return tabla_unificada