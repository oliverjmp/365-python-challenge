import spacy
import json
import sys
from pathlib import Path

# --- INICIO DEL SCRIPT ---
print("\n" + "="*60)
print("🤖 INICIANDO PROCESAMIENTO NLP - DÍA 17")
print("="*60)

def ejecutar_analisis():
    try:
        # 1. Localización de rutas
        directorio_actual = Path(__file__).parent
        ruta_salida = directorio_actual / "resultado_nlp_dia17.json"
        
        print(f"📂 Trabajando en: {directorio_actual}")

        # 2. Carga del Modelo
        print("⏳ Cargando modelo inteligente 'es_core_news_md'...")
        # Usamos el modelo medium para mayor precisión en entidades
        nlp = spacy.load("es_core_news_md")
        print("✅ Modelo cargado exitosamente.")

        # 3. Datos de entrada (Perfil Senior)
        texto = (
            "Oliver Morales Pérez está liderando el 365 Python Challenge. "
            "Hoy analiza datos de Microsoft y Amazon en Madrid para "
            "optimizar estrategias de Business Intelligence."
        )
        print(f"\n📝 Analizando texto: '{texto[:50]}...'")

        # 4. Procesamiento
        doc = nlp(texto)

        # 5. Extracción de Entidades (NER) y Lematización
        # NER: Identifica nombres, lugares y organizaciones
        # Lematización: Lleva las palabras a su raíz (ej. 'analiza' -> 'analizar')
        resultados = {
            "entidades": [{"texto": ent.text, "tipo": ent.label_} for ent in doc.ents],
            "lemas_clave": [t.lemma_ for t in doc if not t.is_stop and not t.is_punct]
        }

        # 6. Guardado de resultados
        print("💾 Guardando resultados en JSON...")
        with open(ruta_salida, "w", encoding="utf-8") as f:
            json.dump(resultados, f, indent=4, ensure_ascii=False)

        # 7. Resumen por pantalla
        print("\n🎯 RESULTADOS DETECTADOS:")
        for ent in resultados["entidades"]:
            print(f"   - {ent['tipo']}: {ent['texto']}")
        
        print(f"\n✨ ¡DÍA 17 COMPLETADO! Archivo generado: {ruta_salida.name}")

    except Exception as e:
        print(f"\n❌ ERROR CRÍTICO: {e}")
        print("👉 Asegúrate de haber ejecutado: python -m spacy download es_core_news_md")

if __name__ == "__main__":
    ejecutar_analisis()
    print("="*60 + "\n")