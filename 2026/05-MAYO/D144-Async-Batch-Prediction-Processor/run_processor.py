import asyncio
import logging
from src.batch_processor import AsyncBatchPredictionProcessor

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

async def main():
    logging.info("=== Iniciando Procesador Concurrente de Predicciones por Lotes (D144) ===")

    # Simulación de un volumen masivo de características entrantes para inferencia
    massive_payload = [[float(i), float(i + 1)] for i in range(12)]
    
    logging.info(f"Total de registros a procesar: {len(massive_payload)}")

    processor = AsyncBatchPredictionProcessor(batch_size=4)
    
    logging.info("Ejecutando procesamiento asíncrono con multiprocesamiento...")
    predictions = await processor.process_batch_async(massive_payload)

    logging.info(f"Predicciones obtenidas con éxito: {predictions}")
    logging.info("=== Hito D144 Ejecutado Exitosamente ===")

if __name__ == "__main__":
    # Ejecutar loop asíncrono principal compatible con Windows/Linux/macOS
    asyncio.run(main())