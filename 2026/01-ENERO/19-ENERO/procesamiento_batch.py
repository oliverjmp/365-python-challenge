import pandas as pd
from textblob import TextBlob
from pathlib import Path

def procesar_lote_bi():
    # 1. Rutas Dinámicas y Seguras
    carpeta_actual = Path(__file__).parent
    ruta_entrada = carpeta_actual / "comentarios_clientes.csv"
    ruta_salida = carpeta_actual / "reporte_sentimientos_final.csv"

    print("\n" + "="*50)
    print("🚀 PIPELINE DE BI - PROCESAMIENTO MASIVO DÍA 19")
    print("="*50)

    # 2. Leer los datos
    if not ruta_entrada.exists():
        print("❌ Error: No se encontró el archivo 'comentarios_clientes.csv'")
        return

    df = pd.read_csv(ruta_entrada)
    print(f"📊 Cargadas {len(df)} filas de datos.\n")

    # 3. Función de análisis (usando nuestra lógica del día 18)
    def obtener_sentimiento(texto):
        try:
            # Análisis rápido
            score = TextBlob(texto).translate(from_lang="es", to="en").sentiment.polarity
        except:
            # Respaldo simple si falla la traducción
            texto_lower = str(texto).lower()
            if "excelente" in texto_lower or "increible" in texto_lower: score = 0.8
            elif "lenta" in texto_lower or "no me gusta" in texto_lower: score = -0.8
            else: score = 0.0
        return score

    # 4. Aplicar análisis a toda la columna (¡Magia de Pandas!)
    print("🧠 Analizando sentimientos en bloque...")
    df['score'] = df['comentario'].apply(obtener_sentimiento)
    df['sentimiento'] = df['score'].apply(lambda s: "POSITIVO" if s > 0.1 else ("NEGATIVO" if s < -0.1 else "NEUTRO"))

    # 5. Guardar el reporte final
    df.to_csv(ruta_salida, index=False)
    
    # 6. Mostrar resumen en consola
    print("\n" + "-"*30)
    print("📈 RESUMEN DEL REPORTE:")
    print(df['sentimiento'].value_counts())
    print("-"*30)
    print(f"\n✅ Proceso completado. Reporte generado en: {ruta_salida.name}")

if __name__ == "__main__":
    procesar_lote_bi()