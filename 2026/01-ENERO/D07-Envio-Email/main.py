import sys
from datetime import datetime
from pathlib import Path

# ============================================================
# CONFIGURACIÓN DE RUTAS DINÁMICAS
# ============================================================
BASE_DIR = Path(__file__).resolve().parent
# Buscamos el PDF exactamente donde lo dejó el Día 05
RUTA_PDF_DIA5 = BASE_DIR.parent / "D05-Reporte-PDF" / "informe_cripto_ejecutivo.pdf"

DESTINATARIO = "destinatario@empresa.com"
ASUNTO = "Informe Ejecutivo - Mercado Cripto"

def guardar_log(contenido):
    logs_dir = BASE_DIR / "logs"
    logs_dir.mkdir(exist_ok=True)
    fecha_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    ruta_log = logs_dir / f"envio_simulado_{fecha_str}.log"
    
    with open(ruta_log, "w", encoding="utf-8") as f:
        f.write(contenido)
    return ruta_log

def enviar_email_simulado():
    fecha_hoy = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print("Iniciando D07 - Simulacion de Envio...")

    if not RUTA_PDF_DIA5.exists():
        msg_err = f"[{fecha_hoy}] ERROR: No se encontro el PDF en: {RUTA_PDF_DIA5}"
        print(f"STDERR: {msg_err}")
        guardar_log(msg_err)
        return False

    # Simulación de log de envío
    log_content = (
        f"--- ENVIO SIMULADO ---\n"
        f"Fecha: {fecha_hoy}\n"
        f"Para: {DESTINATARIO}\n"
        f"Asunto: {ASUNTO}\n"
        f"Adjunto Detectado: {RUTA_PDF_DIA5.name}\n"
        f"Estado: Exitoso (Simulado)\n"
    )

    print(f"Detectado: {RUTA_PDF_DIA5.name}")
    print(f"Destinatario: {DESTINATARIO}")
    
    guardar_log(log_content)
    print("D07_OK: Simulación completada.")
    return True

if __name__ == "__main__":
    if enviar_email_simulado():
        sys.exit(0)
    else:
        sys.exit(1)