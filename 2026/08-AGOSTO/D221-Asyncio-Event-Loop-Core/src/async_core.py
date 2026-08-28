import asyncio
import time

class AsyncEventLoopCore:
    """Núcleo de gestión de tareas concurrentes de alta densidad mediante asyncio."""
    
    @staticmethod
    async def simulate_io_task(task_id: int, delay: float) -> dict:
        """Simula una operación de I/O asíncrona no bloqueante."""
        start_time = time.perf_counter()
        await asyncio.sleep(delay)
        duration = time.perf_counter() - start_time
        return {
            "task_id": task_id,
            "status": "COMPLETED",
            "duration": round(duration, 4)
        }

    async def execute_concurrent_workload(self, task_count: int, base_delay: float = 0.05) -> dict:
        """Ejecuta un lote masivo de tareas concurrentes bajo el bucle de eventos."""
        if task_count <= 0:
            raise ValueError("El número de tareas concurrentes debe ser mayor a cero.")
        
        start_global = time.perf_counter()
        
        # Creación de corrutinas concurrentes de alta densidad
        tasks = [
            self.simulate_io_task(i, base_delay) 
            for i in range(task_count)
        ]
        
        results = await asyncio.gather(*tasks)
        total_duration = time.perf_counter() - start_global
        
        return {
            "total_tasks": len(results),
            "total_duration": round(total_duration, 4),
            "results": results
        }