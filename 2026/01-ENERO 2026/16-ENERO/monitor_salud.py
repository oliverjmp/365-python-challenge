import json
import logging
from datetime import datetime
from pathlib import Path

# --- LOGGING CONFIG ---
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("HealthMonitor")

class ProjectIntegrityChecker:
    def __init__(self):
        # FORZAMOS LA RUTA: Buscamos la carpeta '2026' desde la raíz del repo
        # Basado en tu imagen, subimos niveles hasta encontrar '2026'
        self.base_path = Path.cwd() 
        if not (self.base_path / "2026").exists():
            # Si lo ejecutas desde dentro de 16-ENERO, subimos 2 niveles
            self.base_path = Path(__file__).resolve().parent.parent
        else:
            self.base_path = self.base_path / "2026"

        self.report = {"fecha": datetime.now().isoformat(), "checks": []}

    def run(self, days: int):
        logger.info(f"🚀 Analizando carpetas en: {self.base_path}")
        for i in range(1, days + 1):
            folder_name = f"{i:02d}-ENERO"
            folder_path = self.base_path / folder_name
            
            # Verificación técnica de existencia de directorio [cite: 22, 23]
            exists = folder_path.is_dir()
            status = "✅ PASS" if exists else "❌ FAIL"
            
            logger.info(f"{status} - {folder_name}")
            self.report["checks"].append({"dia": i, "folder": folder_name, "exists": exists})

    def save(self):
        # Guardamos el reporte DENTRO de la carpeta del día 16 para orden
        output = Path(__file__).resolve().parent / "health_report_day16.json"
        with open(output, "w") as f:
            json.dump(self.report, f, indent=4)
        logger.info(f"📂 Reporte guardado en: {output}")

if __name__ == "__main__":
    checker = ProjectIntegrityChecker()
    checker.run(15) # Validamos los 15 días completados [cite: 11]
    checker.save()