"""
Proyecto: 365 Python Challenge
Día 46: Ultimate Automation Orchestrator 
Objetivo: Integración Total con Rutas Absolutas y Blindaje de Codificación.
"""

import os
import shutil
import zipfile
import logging
import sys
from pathlib import Path
from datetime import datetime

# ==========================================================
# 1. ANCLAJE DE RUTAS (Evita que los archivos se salgan de la carpeta)
# ==========================================================
BASE_DIR = Path(__file__).parent.absolute()
LOG_PATH = BASE_DIR / "master_automation.log"

# ==========================================================
# 2. CONFIGURACIÓN ROBUSTA DE LOGS (UTF-8 y Consola)
# ==========================================
logger = logging.getLogger("UltimateBot")
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Handler para Archivo (Forzamos UTF-8 y Ruta Local)
fh = logging.FileHandler(LOG_PATH, encoding="utf-8")
fh.setFormatter(formatter)
logger.addHandler(fh)

# Handler para Consola (Manejo de flujo estándar)
ch = logging.StreamHandler(sys.stdout)
ch.setFormatter(formatter)
logger.addHandler(ch)

class UltimateOrchestrator:
    def __init__(self, target_folder_name="Workspace_Final"):
        # Todas las rutas son ahora hijas de BASE_DIR
        self.source_dir = BASE_DIR / target_folder_name
        self.backup_dir = BASE_DIR / "Backups"
        self.trash_dir = self.source_dir / "Papelera"
        
        self.categories = {
            "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
            "Imagenes": [".jpg", ".png", ".svg"],
            "Scripts": [".py", ".js", ".html"]
        }
        
        # Inicializar estructura de carpetas
        self.source_dir.mkdir(exist_ok=True)
        self.backup_dir.mkdir(exist_ok=True)

    def step_1_backup(self):
        """Fase de Protección: Snapshot ZIP."""
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        zip_path = self.backup_dir / f"pre_process_backup_{ts}.zip"
        
        try:
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                files = [f for f in self.source_dir.rglob("*") if f.is_file() and self.backup_dir not in f.parents]
                for file in files:
                    zipf.write(file, arcname=file.relative_to(self.source_dir))
            logger.info(f"Backup creado exitosamente: {zip_path.name}")
            return True
        except Exception as e:
            logger.error(f"Error critico en backup: {e}")
            return False

    def step_2_process_files(self):
        """Fase de Ejecucion: Filtro, Rename y Move."""
        timestamp = datetime.now().strftime("%Y-%m-%d")
        files = [f for f in self.source_dir.iterdir() if f.is_file()]
        
        if not files:
            logger.info("No se encontraron archivos nuevos para procesar.")
            return

        for item in files:
            size = item.stat().st_size
            
            # 1. Filtro de Archivos Vacíos
            if size == 0:
                self.trash_dir.mkdir(exist_ok=True)
                shutil.move(str(item), str(self.trash_dir / item.name))
                logger.warning(f"Archivo vacio detectado y movido: {item.name}")
                continue

            # 2. Clasificación por Categoría
            category = "Otros"
            for cat, exts in self.categories.items():
                if item.suffix.lower() in exts:
                    category = cat
                    break
            
            # 3. Preparar Destino con Timestamp
            dest_folder = self.source_dir / category
            dest_folder.mkdir(exist_ok=True)
            new_name = f"{timestamp}_{item.name}"
            dest_path = dest_folder / new_name

            # 4. Movimiento Físico
            try:
                shutil.move(str(item), str(dest_path))
                logger.info(f"PROCESADO: {item.name} -> {category}/{new_name}")
            except Exception as e:
                logger.error(f"Error procesando {item.name}: {e}")

    def run_pipeline(self):
        print("\n" + "═"*60)
        print("🚀 INICIANDO PIPELINE DE AUTOMATIZACIÓN TOTAL")
        print("═"*60)
        
        # El flujo solo avanza si el backup es exitoso (Seguridad Industrial)
        if self.step_1_backup():
            self.step_2_process_files()
            
        print("\n" + "═"*60)
        print(f"✨ PROCESO FINALIZADO. Log en: {LOG_PATH.name}")
        print("═"*60)

if __name__ == "__main__":
    # --- Setup de entorno de prueba controlado ---
    ws = BASE_DIR / "Workspace_Final"
    ws.mkdir(exist_ok=True)
    
    # Creamos archivos de prueba si la carpeta está vacía
    if not any(ws.iterdir()):
        (ws / "balance_mensual.xlsx").write_text("Datos financieros")
        (ws / "script_backup.py").write_text("# Python Script")
        (ws / "error_log.tmp").touch() # Archivo vacío de 0 bytes
        print("📝 Archivos de prueba generados en Workspace_Final.")

    # Ejecución del Orquestador
    bot = UltimateOrchestrator()
    bot.run_pipeline()