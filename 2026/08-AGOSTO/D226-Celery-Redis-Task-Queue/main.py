from src.tasks import heavy_background_computation

def main():
    print("=== D226: Celery & Redis Task Queue (Enterprise Background Jobs) ===")
    
    # Encolamiento de tarea en modo asíncrono (requiere Redis y Celery worker activos)
    print("[i] Despachando tarea pesada a la cola de Redis...")
    try:
        task = heavy_background_computation.delay(duration=2, task_name="EnterprisePipeline-01")
        print(f"[✔] Tarea encolada con éxito. ID de Tarea: {task.id}")
        print(f"[i] Estado actual de la tarea: {task.status}")
    except Exception as e:
        print(f"[!] Nota operativa: No se pudo conectar a Redis local ({e}).")
        print("[i] Ejecutando simulación local síncrona...")
        res = heavy_background_computation.run(duration=1, task_name="FallbackTask")
        print(f"[✔] Resultado local: {res}")

if __name__ == "__main__":
    main()