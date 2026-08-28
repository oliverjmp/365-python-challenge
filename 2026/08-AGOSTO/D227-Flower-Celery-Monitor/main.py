from src.monitor_tasks import monitored_computation

def main():
    print("=== D227: Celery Flower Monitor (Supervisión de Tareas) ===")
    
    print("[i] Despachando tarea rastreable al broker de Celery...")
    try:
        task = monitored_computation.delay(items_count=3, task_tag="CliPipeline")
        print(f"[✔] Tarea encolada. ID: {task.id}")
        print(f"[i] Estado inicial: {task.status}")
    except Exception as e:
        print(f"[!] Nota operativa: Redis no disponible localmente ({e}).")
        print("[i] Ejecutando simulación local síncrona de respaldo...")
        res = monitored_computation.run(items_count=3, task_tag="FallbackCLI")
        print(f"[✔] Resultado local: {res}")

if __name__ == "__main__":
    main()