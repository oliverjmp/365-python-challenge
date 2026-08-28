import numpy as np
from src.shared_mem_core import SharedMemoryManagerEngine

def main():
    print("=== D225: Shared Memory Manager (Procesamiento Cero-Copia) ===")
    engine = SharedMemoryManagerEngine()
    
    matrix = np.array([[1, 2], [3, 4]], dtype=np.int32)
    print(f"[i] Matriz original en proceso padre:\n{matrix}")
    
    summary = engine.execute_shared_computation(matrix)
    
    print(f"[✔] Estado de ejecución hijo: {summary['computation_result']['status']}")
    print(f"[✔] Suma total procesada en el hijo: {summary['computation_result']['sum']}")
    print(f"[✔] Matriz modificada leída desde memoria compartida:\n{np.array(summary['modified_data'])}")

if __name__ == "__main__":
    main()