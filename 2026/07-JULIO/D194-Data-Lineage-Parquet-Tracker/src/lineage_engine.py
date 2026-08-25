import os
import json
import pandas as pd
import pyarrow.parquet as pq
from datetime import datetime
from typing import Dict, Any

class DataLineageTracker:
    """Motor de rastreo de metadatos y linaje para ficheros Parquet."""
    
    def __init__(self, data_lake_dir: str = "data_lake", metadata_path: str = "data_lake/lineage_metadata.json"):
        self.data_lake_dir = data_lake_dir
        self.metadata_path = metadata_path
        os.makedirs(self.data_lake_dir, exist_ok=True)
        self._inicializar_entorno()

    def _inicializar_entorno(self):
        """Genera ficheros Parquet con datos reales y su linaje si no existen o están vacíos."""
        raw_path = os.path.join(self.data_lake_dir, "raw_data.parquet")
        processed_path = os.path.join(self.data_lake_dir, "processed_data.parquet")
        
        # Generar o rellenar raw_data.parquet si no existe o está vacío
        if not os.path.exists(raw_path) or os.path.getsize(raw_path) == 0:
            df_raw = pd.DataFrame({
                "id": [1, 2, 3, 4, 5],
                "usuario": ["Ana", "Carlos", "Beatriz", "David", "Elena"],
                "monto": [150.0, 300.5, 450.0, 100.0, 600.0],
                "fecha": ["2026-07-01", "2026-07-01", "2026-07-02", "2026-07-02", "2026-07-03"]
            })
            df_raw.to_parquet(raw_path, index=False)
            
        # Generar o rellenar processed_data.parquet si no existe o está vacío
        if not os.path.exists(processed_path) or os.path.getsize(processed_path) == 0:
            df_processed = pd.DataFrame({
                "usuario": ["Ana", "Carlos", "Beatriz", "David", "Elena"],
                "monto_total": [150.0, 300.5, 450.0, 100.0, 600.0],
                "segmento": ["VIP", "Standard", "VIP", "Standard", "Enterprise"]
            })
            df_processed.to_parquet(processed_path, index=False)
            
        # Generar metadatos de linaje si no existen
        if not os.path.exists(self.metadata_path):
            lineage_inicial = {
                "nodes": [
                    {"file": "raw_data.parquet", "layer": "RAW", "rows": 5, "columns": 4},
                    {"file": "processed_data.parquet", "layer": "PROCESSED", "rows": 5, "columns": 3}
                ],
                "edges": [
                    {"from": "raw_data.parquet", "to": "processed_data.parquet", "transformation": "Limpieza, Agregación y Segmentación por Tipo de Cliente"}
                ],
                "last_updated": str(datetime.now())
            }
            with open(self.metadata_path, "w", encoding="utf-8") as f:
                json.dump(lineage_inicial, f, indent=4)

    def obtener_linaje(self) -> Dict[str, Any]:
        """Carga el registro de metadatos y linaje desde el Data Lake."""
        if not os.path.exists(self.metadata_path):
            raise FileNotFoundError(f"El fichero de metadatos de linaje no existe en: {self.metadata_path}")
            
        with open(self.metadata_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def registrar_transformacion(self, origen: str, destino: str, transformacion: str) -> bool:
        """Registra una nueva relación de linaje entre ficheros Parquet."""
        metadata = self.obtener_linaje()
        
        orig_path = os.path.join(self.data_lake_dir, origen)
        dest_path = os.path.join(self.data_lake_dir, destino)
        
        if os.path.exists(orig_path) and os.path.exists(dest_path):
            meta_orig = pq.read_metadata(orig_path)
            meta_dest = pq.read_metadata(dest_path)
            
            nodos = {n["file"]: n for n in metadata["nodes"]}
            nodos[origen] = {"file": origen, "layer": "UPSTREAM", "rows": meta_orig.num_rows, "columns": meta_orig.num_columns}
            nodos[destino] = {"file": destino, "layer": "DOWNSTREAM", "rows": meta_dest.num_rows, "columns": meta_dest.num_columns}
            metadata["nodes"] = list(nodos.values())
            
            nuevo_edge = {"from": origen, "to": destino, "transformation": transformacion}
            if nuevo_edge not in metadata["edges"]:
                metadata["edges"].append(nuevo_edge)
                
            metadata["last_updated"] = str(datetime.now())
            
            with open(self.metadata_path, "w", encoding="utf-8") as f:
                json.dump(metadata, f, indent=4)
            return True
        return False