import pandas as pd
from pathlib import Path
from datetime import datetime

def generar_notificacion_email():
    # 1. LOCALIZACIÓN ABSOLUTA (Busca en todo el reto de Python)
    # Buscamos la carpeta raíz '365-python-challenge'
    ruta_script = Path(__file__).resolve()
    raiz_proyecto = None
    
    # Subimos niveles hasta encontrar la carpeta del reto
    for parent in ruta_script.parents:
        if parent.name == "365-python-challenge":
            raiz_proyecto = parent
            break
    
    if not raiz_proyecto:
        # Si no la encuentra, usamos el padre del padre como plan B
        raiz_proyecto = ruta_script.parent.parent.parent

    # Buscamos el archivo en cualquier parte de la carpeta 2026
    print(f"🔍 Buscando datos en: {raiz_proyecto}")
    posibles_rutas = list(raiz_proyecto.rglob("reporte_sentimientos_final.csv"))

    if not posibles_rutas:
        print("❌ Error: No se encontró 'reporte_sentimientos_final.csv' en ninguna carpeta.")
        print("👉 Asegúrate de que el Día 19 generó el archivo correctamente.")
        return

    ruta_datos = posibles_rutas[0]
    ruta_email = ruta_script.parent / "PLANTILLA_EMAIL_URGENTE.txt"

    print("\n" + "📧" * 20)
    print("SISTEMA DE NOTIFICACIONES EJECUTIVAS - DÍA 22")
    print(f"✅ Archivo encontrado en: {ruta_datos.relative_to(raiz_proyecto)}")
    print("📧" * 20)

    # 2. Leer datos y filtrar (El resto del código es igual de sólido)
    df = pd.read_csv(ruta_datos)
    
    # Filtro de seguridad por si las columnas se llaman distinto
    col_score = 'score' if 'score' in df.columns else df.columns[-1]
    alertas = df[df[col_score] <= -0.7]

    if not alertas.empty:
        fecha_hoy = datetime.now().strftime("%d/%m/%Y %H:%M")
        cuerpo_email = f"ASUNTO: 🚨 ALERTA CRÍTICA DETECTADA ({fecha_hoy})\n\n"
        cuerpo_email += "Se han detectado comentarios con alta insatisfacción:\n\n"

        for _, fila in alertas.iterrows():
            comentario = fila.get('comentario', 'N/A')
            score = fila.get(col_score, 0)
            cuerpo_email += f"💬 \"{comentario}\" | 📊 Score: {score}\n"
            cuerpo_email += f"{'-'*40}\n"

        with open(ruta_email, "w", encoding="utf-8") as f:
            f.write(cuerpo_email)

        print(f"✅ ¡ÉXITO! Plantilla redactada en: {ruta_email.name}")
    else:
        print("✅ Todo en orden. No hay alertas críticas hoy.")

if __name__ == "__main__":
    generar_notificacion_email()