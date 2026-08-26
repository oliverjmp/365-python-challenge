import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import tempfile
import os
from src.parquet_inspector import ParquetMetadataInspector

def main():
    print("=== D214: Ejecución CLI de Inspección de Ficheros Parquet ===")
    
    # Crear un archivo temporal de prueba
    df = pd.DataFrame({
        "sku": ["SKU-01", "SKU-02"],
        "precio": [99.99, 149.50],
        "stock": [12, 45]
    })
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=".parquet") as tmp:
        file_path = tmp.name
        
    pq.write_table(pa.Table.from_pandas(df), file_path)
    
    # Instanciamos el inspector y cerramos el bloque de lectura de forma segura
    inspector = ParquetMetadataInspector(file_path)
    
    print("\n--- Esquema del Fichero ---")
    for col in inspector.get_schema_info():
        print(f"Columna: {col['column_name']} | Tipo: {col['data_type']} | Nullable: {col['nullable']}")
        
    print("\n--- Metadatos Generales ---")
    meta = inspector.get_file_metadata()
    for k, v in meta.items():
        print(f"{k}: {v}")
        
    print("\n--- Estadísticas de Row Groups ---")
    for rg in inspector.get_row_group_statistics():
        print(f"Grupo {rg['row_group_index']} | Filas: {rg['num_rows']} | Tamaño (bytes): {rg['total_byte_size']}")
        
    # Liberar la referencia explícitamente para cerrar el archivo en Windows
    del inspector
    
    if os.path.exists(file_path):
        os.unlink(file_path)
        
    print("\n[✔] Inspección CLI finalizada exitosamente.")

if __name__ == "__main__":
    main()