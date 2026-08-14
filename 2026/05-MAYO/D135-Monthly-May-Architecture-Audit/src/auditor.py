import json
import os
from typing import Dict, Any, List

class ArchitectureAuditor:
    """Motor de auditoría integral para validar artefactos de arquitectura y modelos del mes."""

    def __init__(self, base_path: str = "."):
        self.base_path = base_path

    def verify_required_artifacts(self, required_paths: List[str]) -> Dict[str, Any]:
        """Verifica la existencia física de los artefactos y directorios requeridos."""
        audit_results = {}
        missing_artifacts = []

        for path in required_paths:
            full_path = os.path.join(self.base_path, path)
            exists = os.path.exists(full_path)
            audit_results[path] = exists
            if not exists:
                missing_artifacts.append(path)

        return {
            "total_checked": len(required_paths),
            "missing_count": len(missing_artifacts),
            "missing_artifacts": missing_artifacts,
            "details": audit_results
        }

    def generate_audit_report(self, audit_data: Dict[str, Any], output_filename: str = "audit_report.json") -> str:
        """Genera un reporte consolidado en formato JSON con los resultados de la auditoría."""
        if not isinstance(audit_data, dict):
            raise ValueError("Los datos de auditoría deben ser un diccionario válido.")

        output_path = os.path.join(self.base_path, output_filename)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(audit_data, f, indent=4, ensure_ascii=False)

        return output_path