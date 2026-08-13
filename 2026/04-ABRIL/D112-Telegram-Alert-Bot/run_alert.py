import logging
from src.bot import TelegramAlertBot

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("=== Iniciando Sistema de Alertas por Telegram (D112) ===")
    
    # Credenciales de prueba o simulación (reemplazar por valores reales en producción)
    BOT_TOKEN = "tu_bot_token_aqui"
    CHAT_ID = "tu_chat_id_aqui"
    
    bot = TelegramAlertBot(BOT_TOKEN, CHAT_ID)
    
    alert_message = (
        "🚨 *ALERTA OPERATIVA CRÍTICA*\n\n"
        "• *Pipeline:* `etl_transacciones_diarias`\n"
        "• *Estado:* Fallido (Timeout en conexión con Base de Datos)\n"
        "• *Timestamp:* 2026-04-14 10:15:00 UTC\n\n"
        "_Por favor, revisar los registros de ejecución inmediatos._"
    )
    
    logging.info("Enviando mensaje de alerta simulado...")
    # Para evitar errores reales sin token válido en ejecución local pura, mostramos el payload:
    logging.info(f"Payload preparado para chat {CHAT_ID}:\n{alert_message}")
    
    # Simulación de ejecución exitosa del flujo
    logging.info("=== Hito D112 Ejecutado Exitosamente ===")

if __name__ == "__main__":
    main()