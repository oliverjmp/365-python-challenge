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
        # Localizamos la carpeta '01-ENERO' que es la madre de tus proyectos
        # Buscamos hacia arriba desde donde esté este script
        self.script_path = Path(__file__).resolve().parent
        # Según tu estructura: 365-python-challenge/2026/01-ENERO/D16-...
        # La carpeta '01-ENERO' es el padre de la carpeta del script
        self.base_path = self.script_path.parent 
        
        self.report = {"fecha": datetime.now().isoformat(), "proyectos_detectados": []}

    def run(self, last_day: int):
        logger.info(f"🚀 Analizando subproyectos en: {self.base_path}")
        
        for i in range(1, last_day + 1):
            # Buscamos carpetas que empiecen por "D" + número (ej: D01*)
            prefix = f"D{i:02d}"
            
            # Buscamos en la carpeta base alguna subcarpeta que empiece con el prefijo
            encontrado = list(self.base_path.glob(f"{prefix}*"))
            
            if encontrado and encontrado[0].is_dir():
                folder_name = encontrado[0].name
                status = "✅ PASS"
                exists = True
                logger.info(f"{status} - {folder_name}")
            else:
                folder_name = f"D{i:02d}-MISSING"
                status = "❌ FAIL"
                exists = False
                logger.warning(f"{status} - No se encontró el proyecto para el día {i}")
            
            self.report["proyectos_detectados"].append({
                "dia": i, 
                "folder": folder_name, 
                "exists": exists
            })

    def save(self):
        output = self.script_path / "health_report_day16.json"
        with open(output, "w", encoding="utf-8") as f:
            json.dump(self.report, f, indent=4, ensure_ascii=False)
        logger.info(f"📂 Reporte guardado en: {output}")

if __name__ == "__main__":
    checker = ProjectIntegrityChecker()
    # Analizamos desde el día 1 hasta el 15 (ayer)
    checker.run(15) 
    checker.save()