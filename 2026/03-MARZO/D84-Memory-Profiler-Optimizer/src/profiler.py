import tracemalloc
from typing import Dict, Any, List, Tuple

class MemoryProfiler:
    def __init__(self):
        if not tracemalloc.is_tracing():
            tracemalloc.start()

    def take_snapshot(self) -> tracemalloc.Snapshot:
        """Toma una instantánea actual del uso de memoria."""
        return tracemalloc.take_snapshot()

    def compare_snapshots(self, snapshot1: tracemalloc.Snapshot, snapshot2: tracemalloc.Snapshot, limit: int = 5) -> List[Dict[str, Any]]:
        """Compara dos instantáneas para identificar bloques de memoria crecientes."""
        stats = snapshot2.compare_to(snapshot1, 'lineno')
        results = []
        for stat in stats[:limit]:
            results.append({
                "size_diff_kb": stat.size_diff / 1024,
                "count_diff": stat.count_diff,
                "traceback": str(stat.traceback)
            })
        return results

    def get_top_allocations(self, limit: int = 5) -> List[str]:
        """Obtiene las principales líneas de código que más memoria consumen."""
        snapshot = tracemalloc.take_snapshot()
        stats = snapshot.statistics('lineno')
        return [str(stat) for stat in stats[:limit]]