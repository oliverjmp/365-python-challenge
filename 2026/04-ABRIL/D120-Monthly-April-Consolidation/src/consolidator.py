import os
from typing import Dict, List

class AprilBlockConsolidator:
    """Consolidador y verificador de salud técnica del bloque de abril."""
    def __init__(self, april_path: str = "."):
        self.april_path = april_path

    def audit_milestones(self, milestones: List[str]) -> Dict[str, bool]:
        """Verifica la existencia de los hitos principales del mes de abril."""
        audit_results = {}
        for milestone in milestones:
            milestone_dir = os.path.join(self.april_path, milestone)
            # Consideramos que existe si la carpeta o un archivo clave está presente
            exists = os.path.exists(milestone_dir)
            audit_results[milestone] = exists
        return audit_results

    def generate_consolidation_report(self, milestones: List[str]) -> str:
        """Genera un reporte consolidado del estado de los hitos del bloque."""
        results = self.audit_milestones(milestones)
        total = len(results)
        passed = sum(1 for status in results.values() if status)
        
        report = f"=== REPORTE DE CONSOLIDACIÓN - BLOQUE ABRIL ===\n"
        report += f"Hitos auditados: {total}\n"
        report += f"Hitos confirmados: {passed}\n"
        report += f"Estado general: {'100% COMPLETADO' if passed == total else 'REVISIÓN PENDIENTE'}\n"
        return report