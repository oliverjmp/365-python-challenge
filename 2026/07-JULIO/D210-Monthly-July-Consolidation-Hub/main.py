import duckdb
from src.consolidation_hub import JulyConsolidationHub

def main():
    print("=== D210: Ejecución CLI de Consolidación Mensual (Julio) ===")
    conn = duckdb.connect(database=":memory:")
    hub = JulyConsolidationHub(conn)
    
    kpis = hub.calcular_kpis_globales()
    print("[✔] KPIs Globales Calculados:")
    for k, v in kpis.items():
        print(f" -> {k}: {v}")
        
    print("\n[✔] Reporte de Hitos:")
    df = hub.generar_reporte_consolidado_julio()
    print(df.to_string(index=False))

    conn.close()

if __name__ == "__main__":
    main()