import asyncio

class AsyncQueueManager:
    """Núcleo de procesamiento desacoplado mediante el patrón Productor-Consumidor con asyncio.Queue."""

    def __init__(self, maxsize: int = 10):
        self.queue: asyncio.Queue = asyncio.Queue(maxsize=maxsize)

    async def producer(self, items: list, delay: float = 0.01) -> int:
        """Produce elementos y los deposita de manera asíncrona en la cola."""
        if not items:
            raise ValueError("La lista de elementos a producir no puede estar vacía.")
        
        for item in items:
            await self.queue.put(item)
            await asyncio.sleep(delay)
        return len(items)

    async def consumer(self, consumer_id: int, results_container: list, stop_event: asyncio.Event) -> None:
        """Consume elementos de la cola de forma concurrente hasta recibir señal de término."""
        while not (stop_event.is_set() and self.queue.empty()):
            try:
                item = await asyncio.wait_for(self.queue.get(), timeout=0.1)
                # Simulación de procesamiento del ítem
                await asyncio.sleep(0.02)
                results_container.append({
                    "consumer_id": consumer_id,
                    "processed_item": item,
                    "status": "PROCESSED"
                })
                self.queue.task_done()
            except asyncio.TimeoutError:
                continue

    async def run_pipeline(self, items: list, num_consumers: int = 2) -> dict:
        """Orquesta el flujo completo del patrón Productor-Consumidor."""
        if not items:
            raise ValueError("La lista de elementos a producir no puede estar vacía.")
        if num_consumers <= 0:
            raise ValueError("El número de consumidores debe ser mayor a cero.")

        results: list = []
        stop_event = asyncio.Event()

        # Lanzar tarea productora
        producer_task = asyncio.create_task(self.producer(items))

        # Lanzar tareas consumidoras concurrentes
        consumer_tasks = [
            asyncio.create_task(self.consumer(i, results, stop_event))
            for i in range(num_consumers)
        ]

        # Esperar a que el productor termine de inyectar todo
        await producer_task
        
        # Indicar que la producción finalizó y esperar a que la cola se vacíe
        stop_event.set()
        await self.queue.join()

        # Cancelar o asegurar que los consumidores terminen
        for task in consumer_tasks:
            task.cancel()
        
        await asyncio.gather(*consumer_tasks, return_exceptions=True)

        return {
            "total_produced": len(items),
            "total_consumed": len(results),
            "consumers_count": num_consumers,
            "results": results
        }