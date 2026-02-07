"""
Proyecto: 365 Python Challenge
Día 45: Automatic Zip Backup
Objetivo: Crear un respaldo comprimido antes de procesar archivos.
"""

import zipfile
from pathlib import Path
from datetime import datetime

class BackupSystem:
    def __init__(self):
        self.base_path = Path(__file__).parent.absolute()
        self.source_dir = self.base_path / "Workspace_Prueba"
        self.backup_dir = self.base_path / "Backups"
        
        # Asegurar carpetas
        self.source_dir.mkdir(exist_ok=True)
        self.backup_dir.mkdir(exist_ok=True)

    def create_backup(self):
        """Comprime el contenido del Workspace en un archivo .zip"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        zip_name = self.backup_dir / f"backup_full_{timestamp}.zip"
        
        print(f"📦 Creando respaldo de seguridad en: {zip_name.name}...")

        try:
            with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
                # Caminamos por el directorio
                files_found = list(self.source_dir.rglob("*"))
                
                if not files_found:
                    print("⚠️ No hay archivos para respaldar.")
                    return False

                for file in files_found:
                    if file.is_file() and "Backups" not in str(file):
                        # Escribir archivo en el ZIP
                        # arcname define cómo se verá dentro del ZIP (ruta relativa)
                        zipf.write(file, arcname=file.relative_to(self.source_dir))
                
            print(f"✅ Backup completado con éxito. ({len(files_found)} elementos)")
            return True
        except Exception as e:
            print(f"❌ Error crítico en el backup: {e}")
            return False

if __name__ == "__main__":
    # 1. Preparar archivos de prueba
    ws = Path(__file__).parent.absolute() / "Workspace_Prueba"
    ws.mkdir(exist_ok=True)
    (ws / "config.txt").write_text("Dato confidencial v1")
    (ws / "imagen_pro.png").touch()

    # 2. Ejecutar Sistema de Backup
    sys = BackupSystem()
    if sys.create_backup():
        print("\n🚀 Ahora es seguro proceder con la automatización del Día 44.")
    else:
        print("\n🛑 Abortando: El backup falló.")