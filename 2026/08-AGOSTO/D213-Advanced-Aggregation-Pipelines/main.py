import pandas as pd
from src.aggregation_manager import AdvancedAggregationManager

def main():
    print("=== D213: Ejecución CLI de Agregaciones Avanzadas (CUBE / ROLLUP) ===")
    
    manager = AdvancedAggregationManager(":memory:")
    
    df_transacciones = pd.DataFrame({
        "pais": ["MX", "MX", "ES", "ES"],
        "producto": ["App", "Web", "App", "Web"],
        "ingresos": [1000, 1500, 2000, 2500]
    })
    
    manager.load_dataset("transacciones", df_transacciones)
    print("[✔] Dataset cargado exitosamente en DuckDB.")
    
    print("\n--- Ejecutando ROLLUP (Jerarquía por País y Producto) ---")
    df_rollup = manager.execute_rollup("transacciones", "pais", "producto", "ingresos")
    print(df_rollup.to_string(index=False))
    
    print("\n--- Ejecutando CUBE (Multidimensional Cruzado) ---")
    df_cube = manager.execute_cube("transacciones", "pais", "producto", "ingresos")
    print(df_cube.to_string(index=False))
    
    manager.close()

if __name__ == "__main__":
    main()