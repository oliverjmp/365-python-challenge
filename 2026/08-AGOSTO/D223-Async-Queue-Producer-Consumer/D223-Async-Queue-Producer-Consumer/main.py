import asyncio
from src.queue_core import AsyncQueueManager

async def main():
    print("=== D223: Patrón Productor-Consumidor Asíncrono (asyncio.Queue) ===")
    manager = AsyncQueueManager(maxsize=10)
    
    items = [f"Payload_ID_{i}" for i in range(1, 11)]
    print(f"[i] Iniciando pipeline con {len(items)} elementos y 3 consumidores concurrentes...")
    
    summary = await manager.run_pipeline(items, num_consumers=3)
    
    print(f"[✔] Total elementos producidos: {summary['total_produced']}")
    print(f"[✔] Total elementos consumidos: {summary['total_consumed']}")
    print(f"[✔] Muestra del primer resultado procesado: {summary['results'][0]}")

if __name__ == "__main__":
    asyncio.run(main())