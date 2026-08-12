import json
from pathlib import Path
import logging

class QuarterlyPipelineAudit:
    def __init__(self, metrics_file_path: str = "data/pipeline_metrics.json"):
        self.metrics_path = Path(metrics_file_path)

    def load_metrics(self) -> dict:
        """Carga y analiza el archivo JSON con las métricas de los pipelines."""
        if not self.metrics_path.exists():
            logging.error(f"[X] El archivo de métricas no existe: {self.metrics_path}")
            return {}
        
        try:
            with open(self.metrics_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data
        except json.JSONDecodeError as e:
            logging.error(f"[X] Error al decodificar el archivo JSON: {e}")
            return {}

    def generate_health_report(self) -> dict:
        """Calcula estadísticas clave y el estado de salud global del trimestre."""
        data = self.load_metrics()
        pipelines = data.get("pipelines", [])

        total_pipelines = len(pipelines)
        if total_pipelines == 0:
            return {"status": "EMPTY", "total": 0, "success_rate": 0.0}

        success_count = sum(1 for p in pipelines if p.get("status") == "SUCCESS")
        failed_count = sum(1 for p in pipelines if p.get("status") == "FAILED")
        warning_count = sum(1 for p in pipelines if p.get("status") == "WARNING")
        
        success_rate = (success_count / total_pipelines) * 100.0

        report = {
            "quarter": data.get("quarter", "Q1"),
            "total_pipelines": total_pipelines,
            "success_count": success_count,
            "failed_count": failed_count,
            "warning_count": warning_count,
            "success_rate_percent": round(success_rate, 2),
            "health_status": "HEALTHY" if success_rate >= 75.0 else "CRITICAL"
        }
        return report