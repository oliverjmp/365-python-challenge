import pandas as pd
from src.duck_sync import DuckDBMotherDuckManager

def main():
    print("=== D212: Ejecución CLI de Sincronización Híbrida DuckDB & MotherDuck ===")
    
    manager = DuckDBMotherDuckManager(":memory:")
    
    df_inventario = pd.DataFrame({
        "sku": ["SKU-001", "SKU-002"],
        "stock": [50, 150]
    })
    
    manager.create_local_table("inventario_local", df_inventario)
    print("[✔] Tabla analítica 'inventario_local' creada exitosamente en DuckDB.")
    
    rows = manager.simulate_cloud_sync("inventario_local", "md.inventario_nube")
    print(f"[✔] Sincronización híbrida simulada: {rows} registros enviados a MotherDuck Cloud.")
    
    df_result = manager.query_hybrid_data("SELECT * FROM inventario_local")
    print("[✔] Datos consultados desde el motor analítico:")
    print(df_result.to_string(index=False))
    
    manager.close()

if __name__ == "__main__":
    main()