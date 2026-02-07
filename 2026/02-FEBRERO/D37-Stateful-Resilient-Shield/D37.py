"""
Proyecto: 365 Python Challenge
Día 37: Stateful Resilient Shield & User Warnings
Objetivo: Implementar gestión de estado y bloqueo temporal por reincidencia.
"""

import logging
import time
import unicodedata
from pathlib import Path
from datetime import datetime
import pandas as pd

# Configuración de Logging Profesional
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("Manolo-Shield-D37")

def normalize_text(text: str) -> str:
    """Limpia tildes, convierte a minúsculas y normaliza el texto."""
    text = text.lower().strip()
    return ''.join(c for c in unicodedata.normalize('NFD', text) 
                  if unicodedata.category(c) != 'Mn')

class ResilientOrchestrator:
    def __init__(self):
        self.base_path = Path(__file__).parent.absolute()
        # --- GESTIÓN DE ESTADO (MEMORIA) ---
        self.warnings = 0        # Contador de faltas
        self.max_warnings = 3    # Umbral de bloqueo
        self.is_blocked = False  # Estado del sistema

    def check_sentiment(self, text: str) -> bool:
        """
        Motor de detección de toxicidad expandido.
        Categoriza insultos, hostilidad técnica y presión negativa.
        """
        clean_text = normalize_text(text)
        
        # 1. Diccionario de Seguridad Expandido
        insultos = ['imbecil', 'estupido', 'tonto', 'inutil', 'idiota', 'basura', 'mierda', 'puto', 'pendejo', 'maldito']
        hostilidad = ['no sirves', 'horrible', 'asco', 'peor', 'error', 'mal hecho', 'inservible', 'pobre']
        presion = ['ya mismo', 'ahora', 'obligo', 'muevete', 'rapido', 'callate', 'hazlo']
        
        super_blacklist = insultos + hostilidad + presion
        
        # Búsqueda de coincidencias
        for word in super_blacklist:
            if word in clean_text:
                logger.warning(f"⚠️ Palabra bloqueada detectada: {word}")
                return True
        return False

    def process_request(self, user_input: str):
        # 1. Verificación de Bloqueo de Seguridad
        if self.is_blocked:
            return "🚫 SISTEMA BLOQUEADO. El protocolo de seguridad está activo. No responderé."

        # 2. Análisis de Sentimiento con Acumulación de Estado
        if self.check_sentiment(user_input):
            self.warnings += 1
            logger.error(f"Incidente de seguridad registrado ({self.warnings}/{self.max_warnings})")
            
            if self.warnings >= self.max_warnings:
                self.is_blocked = True
                print("\n" + "!"*50)
                print("⚠️ UMBRAL DE FALTAS ALCANZADO. BLOQUEANDO SISTEMA...")
                print("!"*50 + "\n")
                time.sleep(10)  # Bloqueo físico del hilo de ejecución
                self.warnings = 0
                self.is_blocked = False
                return "🔄 Bloqueo finalizado. Sistema reiniciado. Por favor, mantenga un tono profesional."
            
            return f"🤖 Manolo: ⚠️ Advertencia {self.warnings}/{self.max_warnings}. Detecto lenguaje inapropiado o presión excesiva."

        # 3. Procesamiento de Intenciones (Solo si pasa el escudo)
        clean_in = normalize_text(user_input)
        
        if any(w in clean_in for w in ["reporte", "excel", "informe"]):
            return self.execute_report()
        
        if any(w in clean_in for w in ["hola", "buenos", "ayuda", "manolo"]):
            # Bonus: La cortesía reduce el nivel de alerta
            if self.warnings > 0:
                self.warnings -= 1
                logger.info("Nivel de alerta reducido por tono profesional.")
            return "🤖 Manolo: 👋 Hola Oliver. Tono validado. ¿Qué proceso deseas ejecutar?"

        return "🤖 Manolo: Tono correcto, pero no reconozco la instrucción. Prueba con 'reporte'."

    def execute_report(self):
        """Generación de entregable validado"""
        filename = self.base_path / "Reporte_D37_Seguridad.xlsx"
        try:
            df = pd.DataFrame({
                'Fecha': [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
                'Día': [37],
                'Seguridad': ['Estado Resiliente Activo'],
                'Estatus': ['Validado']
            })
            df.to_excel(filename, index=False)
            return f"✅ Tono profesional verificado. Reporte generado en: {filename}"
        except Exception as e:
            return f"❌ Error de sistema: {e}"

if __name__ == "__main__":
    bot = ResilientOrchestrator()
    print("\n" + "="*55)
    print("🚀 D37: RESILIENT SHIELD & STATE MANAGEMENT ACTIVADO")
    print("="*55)
    print("Escribe tu comando (o 'salir' para finalizar):")
    
    while True:
        try:
            user_in = input("\n[Usuario]> ")
            if user_in.lower() in ['exit', 'salir', 'quit']:
                print("👋 Cerrando protocolo de seguridad. ¡Hasta mañana!")
                break
            
            respuesta = bot.process_request(user_in)
            print(respuesta)
            
        except KeyboardInterrupt:
            break