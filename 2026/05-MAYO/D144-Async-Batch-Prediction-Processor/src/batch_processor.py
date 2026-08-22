import asyncio
from concurrent.futures import ProcessPoolExecutor
from typing import List, Dict, Any
import numpy as np

def cpu_heavy_predict(batch_features: List[List[float]]) -> List[float]:
    """Función independiente orientada a CPU para realizar predicciones por lotes (simulada)."""
    # Simulamos un cálculo matricial pesado de Machine Learning
    arr = np.array(batch_features)
    # Ejemplo: suma ponderada de las características multiplicada por un factor simulado
    predictions = np.sum(arr * 1.5, axis=1).tolist()
    return predictions

class AsyncBatchPredictionProcessor:
    """Procesador concurrente que combina asyncio y multiprocessing para lotes masivos."""

    def __init__(self, max_workers: int = None, batch_size: int = 5):
        self.max_workers = max_workers
        self.batch_size = batch_size

        if batch_size <= 0:
            raise ValueError("El tamaño del lote (batch_size) debe ser mayor a cero.")

    def _chunk_data(self, data: List[Any]) -> List[List[Any]]:
        """Divide una lista de datos en fragmentos (batches) del tamaño configurado."""
        return [data[i:i + self.batch_size] for i in range(0, len(data), self.batch_size)]

    async def process_batch_async(self, data_list: List[List[float]]) -> List[float]:
        """Procesa lotes de datos de forma asíncrona delegando el cálculo pesado a un Pool de Procesos."""
        if not data_list:
            raise ValueError("La lista de datos de entrada no puede estar vacía.")

        batches = self._chunk_data(data_list)
        loop = asyncio.get_running_loop()
        all_predictions = []

        # Usar ProcessPoolExecutor dentro del loop asíncrono
        with ProcessPoolExecutor(max_workers=self.max_workers) as executor:
            # Creamos tareas concurrentes para cada lote
            tasks = [
                loop.run_in_executor(executor, cpu_heavy_predict, batch)
                for batch in batches
            ]
            
            results = await asyncio.gather(*tasks)
            
            for res in results:
                all_predictions.extend(res)

        return all_predictions