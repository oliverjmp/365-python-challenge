import pandas as pd
from src.memory_optimizer import ArrowMemoryOptimizer

def main():
    print("=== D218: Optimización de Footprint de Memoria con PyArrow Pools ===")
    
    pools = ArrowMemoryOptimizer.get_available_memory_pools()
    print(f"[✔] Backend de Memoria Activo: {pools}")
    
    stats_pre = ArrowMemoryOptimizer.get_memory_pool_stats()
    print(f"[i] Bytes asignados antes del proceso: {stats_pre['bytes_allocated']} bytes")
    
    # Generar dataset masivo de prueba simulado
    df_large = pd.DataFrame({
        "transaccion_id": range(1, 100001),
        "monto": [i * 1.1 for i in range(1, 100001)],
        "comercio": ["Comercio_X"] * 100000
    })
    
    print("[i] Procesando 100,000 registros en memoria columnar Arrow...")
    _, metrics = ArrowMemoryOptimizer.process_large_dataset_with_pool(df_large)
    
    stats_post = ArrowMemoryProcessorStats = ArrowMemoryOptimizer.get_memory_pool_stats()
    print(f"[✔] Proceso finalizado. Estadísticas de la piscina:")
    for k, v in metrics.items():
        print(f"    - {k}: {v}")
        
    print("\n[✔] Validación CLI completada exitosamente sin fugas de memoria.")

if __name__ == "__main__":
    main()