"""
Proyecto: 365 Python Challenge
Día 39: Security Audit Reporting (v3 TOTAL)
Objetivo: Fusionar Seguridad Persistente (D38) con Auditoría Contextual.
"""

import logging
import json
import pandas as pd
import unicodedata
from pathlib import Path
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("Manolo-Total")

def normalize_text(text: str) -> str:
    text = text.lower().strip()
    return ''.join(c for c in unicodedata.normalize('NFD', text) 
                  if unicodedata.category(c) != 'Mn')

class TotalOrchestrator:
    def __init__(self):
        self.base_path = Path(__file__).parent.absolute()
        self.db_path = self.base_path / "security_logs.json"
        self.load_state()

    def load_state(self):
        if not self.db_path.exists():
            self.state = {"warnings": 0, "last_incident": "N/A", "status": "Clean"}
        else:
            with open(self.db_path, 'r') as f:
                self.state = json.load(f)

    def save_state(self):
        with open(self.db_path, 'w') as f:
            json.dump(self.state, f, indent=4)

    def check_security(self, text: str) -> bool:
        """Recuperamos el escudo del Día 38."""
        clean_text = normalize_text(text)
        blacklist = ['imbecil', 'estupido', 'puto', 'mierda', 'basura', 'tonto']
        if any(word in clean_text for word in blacklist):
            self.state["warnings"] += 1
            self.state["last_incident"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.save_state()
            return True
        return False

    def generate_report(self):
        filename = self.base_path / "Reporte_Auditoria_D39.xlsx"
        df = pd.DataFrame({
            'Métrica': ['Total Warnings', 'Status'],
            'Valor': [self.state['warnings'], self.state['status']]
        })
        df.to_excel(filename, index=False)
        return f"✅ Reporte generado: {filename}"

    def process_command(self, user_input: str):
        # 1. FILTRO DE SEGURIDAD (Prioridad 1)
        if self.check_security(user_input):
            return f"🤖 Manolo: ⚠️ Insulto detectado. Advertencias: {self.state['warnings']}/3. No haré nada."

        clean_in = normalize_text(user_input)
        
        # 2. MANEJO DE NEGACIÓN (Prioridad 2)
        if any(word in clean_in for word in ["no", "cancelar", "noup"]):
            return "🤖 Manolo: Entendido. Proceso cancelado. ¿Hay algo más en lo que pueda ayudarte?"

        # 3. ACCIÓN O CONFIRMACIÓN
        if any(word in clean_in for word in ["si", "claro", "reporte", "auditoria"]):
            return self.generate_report()
            
        return "🤖 Manolo: No reconozco el comando. Escribe 'reporte', 'si' para confirmar o 'no' para cancelar."

if __name__ == "__main__":
    bot = TotalOrchestrator()
    print("\n🚀 D39: ORQUESTADOR TOTAL (SEGURIDAD + AUDITORÍA)")
    print("🤖 Manolo: ¿Deseas generar el reporte de auditoría?")
    
    while True:
        user_in = input("\n[Usuario]> ")
        if user_in.lower() in ['exit', 'salir']: break
        print(bot.process_command(user_in))