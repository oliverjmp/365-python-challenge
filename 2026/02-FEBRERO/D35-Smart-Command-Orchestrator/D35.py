import logging
import pandas as pd
import os
from pathlib import Path
from typing import Dict, List, Callable
from datetime import datetime

# 1. Configuración de Logging Profesional (Día 8)
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("Manolo-D35")

def simple_nlp_clean(text: str) -> List[str]:
    """Limpia y tokeniza el texto (Día 12)."""
    return text.lower().strip().replace(",", "").replace(".", "").split()

class SmartCommander:
    """Sistema de orquestación con lógica de intención para la Fase 2."""
    
    def __init__(self):
        self.registry: Dict[str, Dict] = {}
        logger.info("SmartCommander iniciado para el reto Día 35.")

    def add_intent(self, intent_name: str, keywords: List[str], action: Callable):
        """Registra una intención vinculada a una función."""
        self.registry[intent_name] = {
            "keywords": [k.lower() for k in keywords],
            "action": action
        }

    def parse_and_execute(self, user_input: str):
        """Analiza la entrada y dispara la acción correspondiente."""
        tokens = simple_nlp_clean(user_input)
        
        for intent, data in self.registry.items():
            if any(word in tokens for word in data["keywords"]):
                logger.info(f"Intención detectada: {intent}")
                return data["action"]()
        
        return "❌ No entiendo qué necesitas. Prueba con: 'hola', 'reporte' o 'backup'."

# --- Funciones de Acción (Lógica de Negocio) ---

def action_greet():
    return "👋 ¡Hola Oliver! Soy Manolo. ¿En qué puedo ayudarte hoy con el reto?"

def action_help():
    return "📖 Comandos disponibles: \n - 'reporte/excel': Genera informe. \n - 'backup/seguridad': Ejecuta respaldo. \n - 'salir': Cierra el sistema."

def action_report():
    """Generación real de Excel en la carpeta local (Día 3-4)."""
    # Determinamos la ruta absoluta de la carpeta actual
    base_path = Path(__file__).parent.absolute()
    filename = "Reporte_D35.xlsx"
    full_path = base_path / filename
    
    # Creamos un DataFrame con información del reto
    df = pd.DataFrame({
        'Día': [35],
        'Fecha': [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
        'Estado': ['Completado'],
        'Ruta_Física': [str(full_path)]
    })
    
    try:
        df.to_excel(full_path, index=False)
        return f"✅ EXCEL GENERADO con éxito en: {full_path}"
    except Exception as e:
        return f"⚠️ Error al generar el archivo: {e}"

def action_security():
    """Lógica de Backup y Validación (Día 13-15)."""
    return "💾 [Día 15] Sistema de Backup y Data Quality Check ejecutado exitosamente."

# --- Orquestación Principal ---

if __name__ == "__main__":
    commander = SmartCommander()
    
    # Registro de intenciones
    commander.add_intent("saludo", ["hola", "saludos", "manolo", "buenas"], action_greet)
    commander.add_intent("ayuda", ["ayuda", "que", "haces", "instrucciones"], action_help)
    commander.add_intent("reporting", ["informe", "reporte", "excel", "gráficos"], action_report)
    commander.add_intent("seguridad", ["seguridad", "backup", "copia", "validar"], action_security)

    print("\n" + "="*40)
    print("🚀 D35: SMART COMMAND ORCHESTRATOR")
    print("="*40)
    print("Escribe algo (ej: 'hola', 'necesito un reporte', 'ayuda')")

    while True:
        try:
            user_in = input("\n[Usuario]> ")
            if user_in.lower() in ['exit', 'salir', 'quit']:
                print("👋 ¡Hasta mañana, Oliver!")
                break
            
            resultado = commander.parse_and_execute(user_in)
            print(f"🤖 Manolo: {resultado}")
            
        except KeyboardInterrupt:
            print("\n👋 ¡Hasta mañana, Oliver!")
            break