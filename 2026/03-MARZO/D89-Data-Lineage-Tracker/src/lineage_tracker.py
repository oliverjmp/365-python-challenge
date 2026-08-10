from typing import List, Dict, Any

class DataLineageTracker:
    def __init__(self):
        self.lineage_graph: Dict[str, List[Dict[str, Any]]] = {}

    def register_transformation(self, source_dataset: str, target_dataset: str, operation: str) -> None:
        """Registra una transformación de un dataset de origen a uno de destino."""
        if target_dataset not in self.lineage_graph:
            self.lineage_graph[target_dataset] = []
            
        record = {
            "source": source_dataset,
            "operation": operation
        }
        self.lineage_graph[target_dataset].append(record)

    def get_lineage(self, dataset: str) -> List[Dict[str, Any]]:
        """Devuelve el historial de linaje y transformaciones para un dataset dado."""
        return self.lineage_graph.get(dataset, [])