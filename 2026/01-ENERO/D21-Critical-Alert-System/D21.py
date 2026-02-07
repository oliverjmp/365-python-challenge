import pandas as pd
from pathlib import Path

def sistema_alertas_criticas():
    # 1. Configuración de rutas seguras
    carpeta_actual = Path(__file__).parent
    # Buscamos los datos en la carpeta del día anterior (D19/D20)
    # Ajustamos la ruta para que encuentre tu reporte de BI
    ruta_datos = carpeta_actual.parent / "D19-Massive-BI-Pipeline" / "reporte_sentimientos_final.csv"
    ruta_log_alertas = carpeta_actual / "LOG_ALERTAS_CRITICAS.txt"

    print("\n" + "!"*50)
    print("⚠️  SISTEMA DE MONITOREO DE ALERTAS - DÍA 21")
    print("!"*50)

    # 2. Verificar si existen los datos
    if not ruta_datos.exists():
        print(f"❌ Error: No se encontraron datos en: {ruta_datos}")
        print("👉 Asegúrate de haber ejecutado el Día 19 primero.")
        return

    df = pd.read_csv(ruta_datos)
    
    # 3. Filtrar casos críticos (Umbral de urgencia: -0.7)
    # Solo lo que sea realmente negativo
    umbral_critico = -0.7
    alertas = df[df['score'] <= umbral_critico]

    if not alertas.empty:
        print(f"🚨 SE HAN DETECTADO {len(alertas)} CASOS CRÍTICOS 🚨\n")
        
        with open(ruta_log_alertas, "w", encoding="utf-8") as f:
            f.write(f"--- REPORTE DE INCIDENCIAS CRÍTICAS DÍA 21 ---\n")
            f.write(f"Generado el: {pd.Timestamp.now()}\n\n")
            
            for index, fila in alertas.iterrows():
                # Nota: Usamos fila.get para evitar errores si las columnas varían
                comentario = fila.get('comentario', 'Sin texto')
                score = fila.get('score', 0)
                
                mensaje_alerta = f"🔴 URGENTE: '{comentario}' (Score: {score})"
                print(mensaje_alerta)
                f.write(mensaje_alerta + "\n")
                
        print(f"\n📂 Se ha generado un log de urgencia en: {ruta_log_alertas.name}")
    else:
        print("✅ No se detectaron sentimientos críticos en este lote. ¡Todo bajo control!")

    print("!"*50 + "\n")

if __name__ == "__main__":
    sistema_alertas_criticas()