from src.singleton_db import DuckDBConnectionSingleton
import threading

def worker_task(results, index):
    db1 = DuckDBConnectionSingleton()
    results.append(id(db1.connection))

def main():
    print("=== D208: Demostración de Singleton para DuckDB Connection ===")
    
    # Instancias secuenciales
    conn_a = DuckDBConnectionSingleton()
    conn_b = DuckDBConnectionSingleton()
    
    print(f"ID Conexión A: {id(conn_a.connection)}")
    print(f"ID Conexión B: {id(conn_b.connection)}")
    print(f"¿Son la misma instancia exacta?: {conn_a.connection is conn_b.connection}")
    
    # Prueba de concurrencia con múltiples hilos
    print("\nEjecutando prueba de concurrencia con hilos múltiples...")
    threads = []
    results = []
    
    for i in range(5):
        t = threading.Thread(target=worker_task, args=(results, i))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
        
    print(f"IDs de conexiones en hilos concurrentes: {results}")
    all_same = all(x == results[0] for x in results)
    print(f"¿Todas las conexiones concurrentes comparten el mismo puntero en memoria?: {all_same}")

if __name__ == "__main__":
    main()