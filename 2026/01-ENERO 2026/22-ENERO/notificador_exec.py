import pandas as pd
from pathlib import Path
from datetime import datetime

def generar_notificacion_email():
    # 1. Rutas
    carpeta_actual = Path(__file__).parent
    ruta_datos = carpeta_actual.parent / "20-ENERO" / "reporte_sentimientos_final.csv"
    ruta_email = carpeta_actual / "PLANTILLA_EMAIL_URGENTE.txt"

    print("\n" + "📧"*20)
    print("SISTEMA DE NOTIFICACIONES EJECUTIVAS - DÍA 22")
    print("📧"*20)

    if not ruta_datos.exists():
        print("❌ Error: Faltan los datos del reporte.")
        return

    df = pd.read_csv(ruta_datos)
    alertas = df[df['score'] <= -0.7]

    if not alertas.empty:
        # 2. Construcción de la Plantilla Profesional
        fecha_hoy = datetime.now().strftime("%d/%m/%Y %H:%M")
        
        cuerpo_email = f"""ASUNTO: 🚨 ALERTA CRÍTICA: INSATISFACCIÓN DE CLIENTE DETECTADA ({fecha_hoy})

Estimado Equipo de Operaciones,

Se ha detectado una anomalía en el sentimiento de los clientes procesados el día de hoy. 
A continuación, se detallan los casos que requieren atención inmediata para evitar pérdida de clientes (Churn):

"""
        # 3. Iteración para añadir los casos al cuerpo del mensaje
        for _, fila in alertas.iterrows():
            cuerpo_email += f"📍 CLIENTE: {fila['usuario']}\n"
            cuerpo_email += f"💬 COMENTARIO: \"{fila['comentario']}\"\n"
            cuerpo_email += f"📊 SCORE: {fila['score']}\n"
            cuerpo_email += f"{'-'*40}\n"

        cuerpo_email += f"\nEste es un mensaje generado automáticamente por el sistema de BI de Oliver.\n"
        cuerpo_email += f"Por favor, no responder a este correo."

        # 4. Guardar la plantilla
        with open(ruta_email, "w", encoding="utf-8") as f:
            f.write(cuerpo_email)

        print(f"✅ Notificación redactada automáticamente.")
        print(f"📂 Archivo listo para enviar: {ruta_email.name}")
        print("\n--- VISTA PREVIA DEL ASUNTO ---")
        print(f"📢 {cuerpo_email.splitlines()[0]}")
    else:
        print("✅ Todo en orden. No hay alertas para notificar hoy.")

if __name__ == "__main__":
    generar_notificacion_email()