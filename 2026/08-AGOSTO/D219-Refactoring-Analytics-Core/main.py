import pandas as pd
from src.facade import AnalyticsCoreFacade

def main():
    print("=== D219: Refactorización de Core Analítico bajo Patrón Fachada ===")
    facade = AnalyticsCoreFacade()
    
    df_sample = pd.DataFrame({
        "id": range(1, 5001),
        "metrica": [i * 1.5 for i in range(1, 5001)]
    })
    
    result = facade.execute_pipeline(df_sample)
    print("[✔] Pipeline ejecutado con éxito a través de la Fachada.")
    print(f"[i] Métricas obtenidas: {result['analytical_metrics']}")
    print(f"[i] Estado de memoria Arrow: {result['final_memory']}")

if __name__ == "__main__":
    main()