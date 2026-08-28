import pandas as pd
from src.data_validator import DataQualityEngine

def main():
    print("=== D217: Pipeline de Calidad de Datos con DuckDB Constraints ===")
    
    df = pd.DataFrame({
        "transaction_id": [501, 502, 503, 504],
        "customer_id": [10, 11, 12, 13],
        "amount": [2500.00, 150.75, 999.99, 12000.00],
        "status": ["COMPLETED", "COMPLETED", "PENDING", "COMPLETED"],
        "event_date": ["2026-08-20", "2026-08-21", "2026-08-22", "2026-08-23"]
    })
    
    engine = DataQualityEngine()
    engine.create_validated_table(df, "production_transactions")
    
    print("\n[✔] Tabla creada exitosamente aplicando constraints nativos de DuckDB.")
    
    metrics = engine.run_data_assertions("production_transactions")
    print("\n--- Reporte de Métricas y Aserciones de Calidad ---")
    for k, v in metrics.items():
        print(f" - {k}: {v}")
        
    engine.close()
    print("\n[✔] Validación CLI completada sin incidencias.")

if __name__ == "__main__":
    main()