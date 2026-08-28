from src.cpu_core import MultiprocessingCPUBoundManager

def main():
    print("=== D224: Procesamiento Paralelo con Multiprocessing (CPU-Bound) ===")
    manager = MultiprocessingCPUBoundManager()
    
    numbers = [500, 1000, 1500, 2000]
    print(f"[i] Procesando {len(numbers)} operaciones factoriales pesadas en paralelo...")
    
    summary = manager.compute_batch(numbers)
    
    print(f"[✔] Total cálculos completados: {summary['total_computations']}")
    for r in summary["results"]:
        print(f"    - Factorial de {r['number']}: Resultado con {r['result_digits']} dígitos.")

if __name__ == "__main__":
    main()