import pandas as pd
from pathlib import Path

def sistema_alertas_criticas():
    # 1. Configuración de rutas seguras (como ya es costumbre)
    carpeta_actual = Path(__file__).parent
    # Buscamos los datos en la carpeta del día 19 o 20
    ruta_datos = carpeta_actual.parent / "20-ENERO" / "reporte_sentimientos_final.csv"
    ruta_log_alertas = carpeta_actual / "LOG_ALERTAS_CRITICAS.txt"

    print("\n" + "!"*50)
    print("⚠️  SISTEMA DE MONITOREO DE ALERTAS - DÍA 21")
    print("!"*50)

    # 2. Verificar si existen los datos
    if not ruta_datos.exists():
        print("❌ Error: No se encontraron datos para monitorear.")
        return

    df = pd.read_csv(ruta_datos)
    
    # 3. Filtrar casos críticos (Umbral de urgencia: -0.7)
    umbral_critico = -0.7
    alertas = df[df['score'] <= umbral_critico]

    if not alertas.empty:
        print(f"🚨 SE HAN DETECTADO {len(alertas)} CASOS CRÍTICOS 🚨\n")
        
        with open(ruta_log_alertas, "w", encoding="utf-8") as f:
            f.write(f"--- REPORTE DE INCIDENCIAS CRÍTICAS DÍA 21 ---\n")
            
            for index, fila in alertas.iterrows():
                mensaje_alerta = f"🔴 URGENTE: El usuario '{fila['usuario']}' reportó: '{fila['comentario']}' (Score: {fila['score']})"
                print(mensaje_alerta)
                f.write(mensaje_alerta + "\n")
                
        print(f"\n📂 Se ha generado un log de urgencia en: {ruta_log_alertas.name}")
    else:
        print("✅ No se detectaron sentimientos críticos en este lote.")

    print("!"*50 + "\n")

if __name__ == "__main__":
    sistema_alertas_criticas()