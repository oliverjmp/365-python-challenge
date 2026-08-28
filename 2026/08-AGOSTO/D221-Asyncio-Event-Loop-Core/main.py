import asyncio
from src.async_core import AsyncEventLoopCore

async def main():
    print("=== D221: Arquitectura de Bucle de Eventos Asíncrono (asyncio) ===")
    core = AsyncEventLoopCore()
    
    print("[i] Ejecutando workload de alta densidad (100 tareas concurrentes)...")
    workload_summary = await core.execute_concurrent_workload(task_count=100, base_delay=0.02)
    
    print(f"[✔] Tareas procesadas: {workload_summary['total_tasks']}")
    print(f"[✔] Duración global total: {workload_summary['total_duration']} segundos")
    print(f"[✔] Muestra de primer resultado: {workload_summary['results'][0]}")

if __name__ == "__main__":
    asyncio.run(main())