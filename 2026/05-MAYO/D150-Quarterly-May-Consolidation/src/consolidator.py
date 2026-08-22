import os
from typing import Dict, List, Any

class MayConsolidator:
    """Clase para consolidar y auditar el estado del bloque de hitos del mes de mayo."""

    def __init__(self, base_path: str = "."):
        self.base_path = base_path

    def check_milestones_status(self, milestone_list: List[str]) -> Dict[str, bool]:
        """Verifica la existencia física de las carpetas de los hitos en el directorio."""
        status = {}
        for milestone in milestone_list:
            path = os.path.join(self.base_path, milestone)
            status[milestone] = os.path.exists(path) and os.path.isdir(path)
        return status

    def generate_consolidation_report(self, milestone_list: List[str]) -> Dict[str, Any]:
        """Genera un reporte consolidado del progreso y cobertura del bloque mensual."""
        status = self.check_milestones_status(milestone_list)
        total = len(milestone_list)
        completed = sum(1 for v in status.values() if v)
        
        return {
            "total_milestones": total,
            "completed_milestones": completed,
            "completion_rate": (completed / total) * 100 if total > 0 else 0.0,
            "details": status
        }