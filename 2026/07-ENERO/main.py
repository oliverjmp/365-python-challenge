import os
from datetime import datetime

# ============================================================
# Configuración general
# ============================================================

NOMBRE_REPORTE = "informe_cripto.pdf"
DESTINATARIO_SIMULADO = "destinatario@empresa.com"  # No real
ASUNTO_SIMULADO = "Informe Ejecutivo — Mercado Cripto"
CARPETA_LOGS = "logs"

# ============================================================
# Obtener ruta del PDF generado en el Día 05
# ============================================================

def obtener_pdf():
    carpeta = os.path.dirname(os.path.abspath(__file__))
    return os.path.normpath(os.path.join(carpeta, "..", "05-ENERO", NOMBRE_REPORTE))

# ============================================================
# Crear carpeta de logs si no existe
# ============================================================

def crear_carpeta_logs():
    ruta_logs = os.path.join(os.path.dirname(os.path.abspath(__file__)), CARPETA_LOGS)
    os.makedirs(ruta_logs, exist_ok=True)
    return ruta_logs

# ============================================================
# Guardar log profesional
# ============================================================

def guardar_log(contenido):
    carpeta = crear_carpeta_logs()
    fecha = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    ruta_log = os.path.join(carpeta, f"envio_simulado_{fecha}.log")

    with open(ruta_log, "w", encoding="utf-8") as f:
        f.write(contenido)

    print(f"Log generado: {ruta_log}")

# ============================================================
# Simulación de envío de email
# ============================================================

def enviar_email_simulado():
    ruta_pdf = obtener_pdf()
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    print("\n=== ENVÍO SIMULADO — DÍA 07 ===\n")

    if not os.path.exists(ruta_pdf):
        mensaje_error = (
            f"[{fecha}] ERROR: No se encontró el archivo PDF esperado.\n"
            f"Ruta buscada: {ruta_pdf}\n"
        )
        print(mensaje_error)
        guardar_log(mensaje_error)
        return

    # Mensaje profesional en consola
    print(f"Fecha de ejecución: {fecha}")
    print("Estado: OK")
    print("Acción: Simulación de envío del informe ejecutivo")
    print(f"Destinatario simulado: {DESTINATARIO_SIMULADO}")
    print(f"Asunto simulado: {ASUNTO_SIMULADO}")
    print(f"Archivo adjunto detectado: {ruta_pdf}\n")

    print("Vista previa del email que se enviaría:\n")
    print("----------------------------------------")
    print(f"Para: {DESTINATARIO_SIMULADO}")
    print(f"Asunto: {ASUNTO_SIMULADO}")
    print("\nCuerpo:")
    print(
        "Estimado equipo,\n\n"
        "Adjunto el informe ejecutivo del mercado cripto correspondiente al día de hoy.\n\n"
        "Incluye:\n"
        "• Datos limpios\n"
        "• Dashboard premium\n"
        "• Gráficos ejecutivos\n"
        "• PDF final\n\n"
        "Saludos,\n"
        "Oliver Javier Morales Pérez\n"
        "365 Python Challenge"
    )
    print("----------------------------------------\n")

    print("Simulación completada correctamente.\n")

    # Crear log profesional
    log = (
        f"[{fecha}] ENVÍO SIMULADO EXITOSO\n"
        f"Destinatario: {DESTINATARIO_SIMULADO}\n"
        f"Asunto: {ASUNTO_SIMULADO}\n"
        f"Archivo adjunto: {ruta_pdf}\n"
        f"Nota: No se envió ningún correo real.\n"
    )

    guardar_log(log)

# ============================================================
# Ejecución principal
# ============================================================

if __name__ == "__main__":
    enviar_email_simulado()
