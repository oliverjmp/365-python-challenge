"""
Proyecto: 365 Python Challenge
Día 36: Intent & Sentiment Linker (Versión Blindada)
"""

import logging
from pathlib import Path
import pandas as pd
from datetime import datetime
import unicodedata

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def normalize_text(text: str) -> str:
    text = text.lower().strip()
    return ''.join(c for c in unicodedata.normalize('NFD', text) 
                  if unicodedata.category(c) != 'Mn')

def analyze_sentiment(text: str) -> str:
    clean_text = normalize_text(text)
    # Lista negra extendida basada en tus pruebas
    blacklist = ['mal', 'basura', 'odio', 'imbecil', 'puto', 'mierda', 'estupido']
    
    # Comprobamos si alguna palabra prohibida está EN CUALQUIER PARTE del texto
    if any(word in clean_text for word in blacklist):
        return "NEGATIVO"
    return "POSITIVO/NEUTRAL"

class SentimentOrchestrator:
    def __init__(self):
        self.base_path = Path(__file__).parent.absolute()

    def process_request(self, user_input: str):
        sentiment = analyze_sentiment(user_input)
        
        # --- BLOQUEO DE SEGURIDAD (EL CAMBIO CRÍTICO) ---
        if sentiment == "NEGATIVO":
            return "🤖 Manolo: ⚠️ DETECTO AGRESIVIDAD. Por política de seguridad, no procesaré ninguna acción hasta que el tono sea profesional."

        # --- SI PASA EL FILTRO, BUSCAMOS LA INTENCIÓN ---
        clean_input = normalize_text(user_input)
        
        if "reporte" in clean_input or "excel" in clean_input:
            return self.generate_report()
        
        if "hola" in clean_input or "buenos" in clean_input:
            return "🤖 Manolo: 👋 Buenos días Oliver. El tono es correcto, ¿qué proceso necesitas?"

        return "🤖 Manolo: Tono amable detectado, pero no entiendo la instrucción. Prueba con 'reporte'."

    def generate_report(self):
        filename = self.base_path / "Reporte_D36_Seguro.xlsx"
        df = pd.DataFrame({'Día': [36], 'Validacion': ['Exitosa'], 'Timestamp': [datetime.now()]})
        df.to_excel(filename, index=False)
        return f"✅ Tono profesional validado. Reporte generado en: {filename}"

if __name__ == "__main__":
    bot = SentimentOrchestrator()
    print("\n🚀 D36: SISTEMA CON FILTRO DE SENTIMIENTOS (BLINDADO)")
    
    while True:
        user_in = input("\n[Usuario]> ")
        if user_in.lower() in ['exit', 'salir']: break
        print(bot.process_request(user_in))