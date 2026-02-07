"""
Proyecto: 365 Python Challenge
Día 38: Persistent Behavior Database
Objetivo: Guardar el historial de advertencias en un archivo JSON.
"""

import logging
import json
import unicodedata
from pathlib import Path
from datetime import datetime
import pandas as pd

# Configuración de Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("Manolo-Persistent-D38")

def normalize_text(text: str) -> str:
    text = text.lower().strip()
    return ''.join(c for c in unicodedata.normalize('NFD', text) 
                  if unicodedata.category(c) != 'Mn')

class PersistentOrchestrator:
    def __init__(self):
        self.base_path = Path(__file__).parent.absolute()
        self.db_path = self.base_path / "security_logs.json"
        self.warnings = self.load_state() # Cargar memoria del disco
        self.max_warnings = 3

    def load_state(self) -> int:
        """Carga el número de advertencias desde el archivo JSON."""
        if self.db_path.exists():
            try:
                with open(self.db_path, 'r') as f:
                    data = json.load(f)
                    return data.get("warnings", 0)
            except Exception as e:
                logger.error(f"Error cargando base de datos: {e}")
        return 0

    def save_state(self):
        """Guarda el estado actual en el archivo JSON."""
        try:
            with open(self.db_path, 'w') as f:
                json.dump({
                    "warnings": self.warnings,
                    "last_incident": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "status": "Warning Active" if self.warnings > 0 else "Clean"
                }, f, indent=4)
        except Exception as e:
            logger.error(f"Error guardando base de datos: {e}")

    def check_sentiment(self, text: str) -> bool:
        clean_text = normalize_text(text)
        # Diccionario ampliado tras el estrés del D37
        blacklist = [
            'imbecil', 'estupido', 'tonto', 'inutil', 'idiota', 'basura', 
            'mierda', 'puto', 'pendejo', 'maldito', 'maricon', 'tarado', 
            'retrasado', 'retrazado', 'toto', 'asco', 'peor'
        ]
        return any(word in clean_text for word in blacklist)

    def process_request(self, user_input: str):
        # 1. Análisis de Sentimiento
        if self.check_sentiment(user_input):
            self.warnings += 1
            self.save_state() # Persistencia inmediata
            logger.error(f"Incidente registrado. Advertencias totales: {self.warnings}")
            
            if self.warnings >= self.max_warnings:
                return f"🚫 ACCESO DENEGADO. Tienes {self.warnings} advertencias en tu historial persistente. Reinicia tu actitud."
            
            return f"🤖 Manolo: ⚠️ Advertencia {self.warnings}/{self.max_warnings}. Esto quedará grabado en tu historial."

        # 2. Procesamiento de acciones
        clean_in = normalize_text(user_input)
        if "reporte" in clean_in or "excel" in clean_in:
            if self.warnings > 0:
                self.warnings -= 1 # Recompensa por buen comportamiento
                self.save_state()
            return self.generate_report()

        return "🤖 Manolo: Tono correcto. No reconozco el comando, pero tu historial está a salvo."

    def generate_report(self):
        filename = self.base_path / "Reporte_D38_Persistente.xlsx"
        df = pd.DataFrame({'Día': [38], 'Historial': ['Persistente'], 'Alertas_Actuales': [self.warnings]})
        df.to_excel(filename, index=False)
        return f"✅ Reporte generado. Advertencias actuales: {self.warnings}. Archivo: {filename}"

if __name__ == "__main__":
    bot = PersistentOrchestrator()
    print("\n" + "="*55)
    print("🚀 D38: PERSISTENT BEHAVIOR DATABASE - MANOLO TIENE MEMORIA")
    print("="*55)
    
    while True:
        user_in = input("\n[Usuario]> ")
        if user_in.lower() in ['exit', 'salir']: break
        print(bot.process_request(user_in))