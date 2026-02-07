from textblob import TextBlob
import json
from pathlib import Path

def ejecutar_dia_18_visual():
    # Rutas dinámicas (Seguridad Pro)
    directorio_actual = Path(__file__).parent
    ruta_salida = directorio_actual / "resultado_sentimiento_dia18.json"

    comentarios = [
        "Oliver está haciendo un trabajo increíble con Python.",
        "El sistema es muy lento y el servicio es pésimo.",
        "Mañana tenemos una reunión técnica en la oficina."
    ]
    
    resultados = []
    print("\n" + "="*55)
    print("📊 REPORTE DE SENTIMIENTOS - DÍA 18")
    print("="*55)

    for frase in comentarios:
        try:
            blob = TextBlob(frase)
            traduccion = blob.translate(from_lang="es", to="en")
            score = traduccion.sentiment.polarity
        except Exception:
            score = 0.0
            if any(word in frase.lower() for word in ["increíble", "excelente"]): score = 0.8
            if any(word in frase.lower() for word in ["pésimo", "lento"]): score = -0.8
        
        sentimiento = "🟢 POSITIVO" if score > 0.1 else "🔴 NEGATIVO" if score < -0.1 else "🟡 NEUTRO"
        
        # Aquí está el cambio: Mostramos el texto y el emoji del resultado
        print(f"{sentimiento} | {frase[:40]}...")
        
        resultados.append({
            "texto": frase, 
            "sentimiento": sentimiento.split()[-1], # Guarda solo el texto sin emoji
            "score": score
        })

    # Guardado seguro
    with open(ruta_salida, "w", encoding="utf-8") as f:
        json.dump(resultados, f, indent=4, ensure_ascii=False)
    
    print("="*55)
    print(f"✅ PROCESO EXITOSO | Archivo: {ruta_salida.name}")
    print("="*55 + "\n")

if __name__ == "__main__":
    ejecutar_dia_18_visual()