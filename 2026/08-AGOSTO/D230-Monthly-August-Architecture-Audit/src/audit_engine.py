import time
import json
from concurrent.futures import ThreadPoolExecutor, as_completed

class AuditEngine:
    def __init__(self, max_workers: int = 4):
        self.max_workers = max_workers

    def simulate_concurrent_probe(self, probe_id: int) -> dict:
        """Simula una prueba de rendimiento concurrente sobre los microservicios auditados."""
        start_time = time.time()
        time.sleep(0.05)
        duration = time.time() - start_time
        
        return {
            "probe_id": probe_id,
            "latency_ms": round(duration * 1000, 2),
            "status": "PASSED" if duration < 0.5 else "WARNING"
        }

    def run_full_audit(self, total_probes: int = 5) -> dict:
        """Ejecuta una batería completa de auditoría concurrente."""
        if total_probes <= 0:
            raise ValueError("El número de pruebas debe ser mayor a cero.")
            
        results = []
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = [executor.submit(self.simulate_concurrent_probe, i) for i in range(total_probes)]
            for future in as_completed(futures):
                results.append(future.result())
                
        passed_count = sum(1 for r in results if r["status"] == "PASSED")
        audit_summary = {
            "total_probes": total_probes,
            "passed": passed_count,
            "health_score": round((passed_count / total_probes) * 100, 2),
            "details": results
        }
        return audit_summary

    def export_audit_json(self, audit_data: dict) -> str:
        """Exporta los resultados de la auditoría en formato JSON estructurado."""
        return json.dumps(audit_data, indent=4)