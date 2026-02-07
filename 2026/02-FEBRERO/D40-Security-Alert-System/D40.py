"""
Proyecto: 365 Python Challenge
Día 40: Security Alert System (Versión Final)
Objetivo: Bloqueo persistente, alertas críticas y manejo de ayuda.
"""

import logging
import json
import unicodedata
import time
from pathlib import Path
from datetime import datetime

# Configuración de Logging: Registramos INFO en consola y CRITICAL para incidentes
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("Security-D40")

def normalize_text(text: str) -> str:
    """Limpia tildes, convierte a minúsculas y normaliza el texto."""
    text = text.lower().strip()
    return ''.join(c for c in unicodedata.normalize('NFD', text) 
                  if unicodedata.category(c) != 'Mn')

class SecurityAlertSystem:
    def __init__(self):
        self.base_path = Path(__file__).parent.absolute()
        self.db_path = self.base_path / "security_logs.json"
        self.alert_log = self.base_path / "security_alerts.log"
        self.load_state()

    def load_state(self):
        """Carga el historial desde el JSON. Si no existe, lo inicializa."""
        if self.db_path.exists():
            with open(self.db_path, 'r') as f:
                self.state = json.load(f)
        else:
            self.state = {"warnings": 0, "status": "Active", "last_event": "None"}
            self.save_state()

    def save_state(self):
        """Persiste el estado en el disco."""
        with open(self.db_path, 'w') as f:
            json.dump(self.state, f, indent=4)

    def trigger_critical_alert(self):
        """Genera una alerta de nivel crítico y bloquea el acceso."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        alert_msg = f"🚨 ALERT CRITICAL: Usuario BLOQUEADO permanentemente. Fecha: {timestamp}"
        
        # 1. Log en consola (Nivel Crítico)
        logger.critical(alert_msg)
        
        # 2. Persistencia en archivo de texto (Audit Trail)
        with open(self.alert_log, "a") as f:
            f.write(alert_msg + "\n")
            
        return "🚫 ACCESO RESTRINGIDO. Tu historial muestra 3+ advertencias. Se ha enviado un reporte al administrador."

    def process_input(self, user_input: str):
        # --- CAPA 0: VERIFICACIÓN DE BLOQUEO PERSISTENTE ---
        if self.state.get("status") == "Blocked":
            return self.trigger_critical_alert()

        clean_in = normalize_text(user_input)

        # --- CAPA 1: SEGURIDAD (SENTIMENT GATEKEEPER) ---
        blacklist = ['imbecil', 'puto', 'mierda', 'estupido', 'basura', 'tonto', 'pendejo']
        if any(word in clean_in for word in blacklist):
            self.state["warnings"] += 1
            self.state["last_event"] = f"Insulto detectado: {datetime.now()}"
            
            if self.state["warnings"] >= 3:
                self.state["status"] = "Blocked"
                self.save_state()
                return self.trigger_critical_alert()
            
            self.save_state()
            return f"🤖 Manolo: ⚠️ Tono inadecuado. Advertencia {self.state['warnings']}/3."

        # --- CAPA 2: AYUDA Y AUTODESCUBRIMIENTO ---
        ayuda_keywords = ["que puedes hacer", "ayuda", "comandos", "que puedo pedir", "capacidades"]
        if any(kw in clean_in for kw in ayuda_keywords):
            return (
                "\n🤖 **MANOLO CAPABILITIES V4.0**\n"
                "----------------------------------\n"
                "1. **Reportes:** Di 'genera reporte' para crear un Excel.\n"
                "2. **Seguridad:** Analizo tu tono en tiempo real.\n"
                "3. **Memoria:** Registro advertencias de forma persistente.\n"
                "4. **Auditoría:** Di 'auditoria' para ver tu estatus legal.\n"
                "----------------------------------"
            )

        # --- CAPA 3: PROCESAMIENTO DE INTENCIONES ---
        if "reporte" in clean_in or "excel" in clean_in:
            return f"✅ Generando reporte solicitado... Sincronizando con {self.db_path.name}. (Proceso exitoso)"
        
        if "hola" in clean_in or "buenos dias" in clean_in:
            return "🤖 Manolo: Hola Oliver. Sistema activo y monitoreando. ¿Qué necesitas hoy?"

        if "auditoria" in clean_in:
            return f"📊 Estatus Actual: {self.state['warnings']} advertencias. Estado: {self.state['status']}."

        # --- CAPA 4: FALLBACK (RESPUESTA POR DEFECTO) ---
        return "🤖 Manolo: No reconozco esa instrucción. Prueba preguntando: '¿Qué puedes hacer?'"

if __name__ == "__main__":
    sys = SecurityAlertSystem()
    print("\n" + "="*60)
    print("🚀 D40: SISTEMA DE SEGURIDAD INTEGRADO Y PERSISTENTE")
    print("="*60)
    print("Estado del sistema cargado. Escribe 'ayuda' para ver comandos.")
    
    while True:
        try:
            u_in = input("\n[Usuario]> ")
            if u_in.lower() in ['exit', 'salir', 'quit']:
                print("👋 Cerrando sistema de seguridad. ¡Hasta mañana, Oliver!")
                break
            
            # Procesar y mostrar respuesta
            print(sys.process_input(u_in))
            
        except KeyboardInterrupt:
            print("\n⚠️ Interrupción forzada. Guardando estado...")
            sys.save_state()
            break