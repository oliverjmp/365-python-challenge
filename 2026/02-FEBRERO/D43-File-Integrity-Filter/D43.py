"""
Proyecto: 365 Python Challenge
Día 43: File Integrity Filter
Objetivo: Detectar archivos vacíos (0 bytes) y segregarlos.
"""

import os
import shutil
from pathlib import Path
from datetime import datetime

class QualityOrganizer:
    def __init__(self):
        self.source_dir = Path(__file__).parent.absolute() / "Workspace_Prueba"
        self.trash_dir = self.source_dir / "Papelera_Reciclaje"
        self.total_processed_size = 0
        self.trash_count = 0

    def check_quality(self):
        if not self.source_dir.exists():
            print("❌ Workspace no encontrado.")
            return

        print(f"🔍 Escaneando integridad en: {self.source_dir}\n")

        for item in self.source_dir.iterdir():
            # Solo procesar archivos en la raíz del workspace
            if item.is_file():
                size = os.path.getsize(item)
                
                # 1. Filtro de Integridad: ¿Archivo vacío?
                if size == 0:
                    self.move_to_trash(item)
                    continue
                
                # 2. Si el archivo es válido, proceder con el Día 42 (Rename + Move)
                self.process_valid_file(item, size)

        self.show_summary()

    def move_to_trash(self, file_path):
        self.trash_dir.mkdir(exist_ok=True)
        try:
            shutil.move(str(file_path), str(self.trash_dir / file_path.name))
            print(f"🗑️ [BASURA] {file_path.name} detectado como vacío (0 bytes).")
            self.trash_count += 1
        except Exception as e:
            print(f"❌ Error al desechar {file_path.name}: {e}")

    def process_valid_file(self, file_path, size):
        # Lógica de categorías simplificada
        dest_folder = self.source_dir / "Procesados"
        dest_folder.mkdir(exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y-%m-%d")
        new_name = f"{timestamp}_{file_path.name}"
        
        try:
            shutil.move(str(file_path), str(dest_folder / new_name))
            self.total_processed_size += size
            print(f"✅ [VALIDO] {file_path.name} ({size} bytes) -> {new_name}")
        except Exception as e:
            print(f"❌ Error al procesar {file_path.name}: {e}")

    def show_summary(self):
        print("\n" + "="*40)
        print("📊 RESUMEN DE CALIDAD")
        print("="*40)
        print(f"📁 Archivos segregados a papelera: {self.trash_count}")
        print(f"📦 Datos útiles procesados: {self.total_processed_size / 1024:.2f} KB")
        print("="*40)

if __name__ == "__main__":
    # Setup de prueba: Archivos útiles vs Archivos basura
    base = Path(__file__).parent.absolute() / "Workspace_Prueba"
    base.mkdir(exist_ok=True)
    
    # Crear archivo útil
    with open(base / "data_importante.txt", "w") as f:
        f.write("Este archivo tiene contenido valioso.")
    
    # Crear archivo basura (vacío)
    (base / "temp_corrupto.log").touch()
    
    quality_bot = QualityOrganizer()
    quality_bot.check_quality()