import os
import re
import unicodedata
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

# =========================================
# CONFIGURACIÓN DE RUTAS DINÁMICAS
# =========================================
BASE_DIR = Path(__file__).resolve().parent
CARPETA_ENTRADA = BASE_DIR / "textos"
CARPETA_SALIDA = BASE_DIR / "reportes"
ARCHIVO_ENTRADA = CARPETA_ENTRADA / "entrada.txt"
ARCHIVO_REPORTE = CARPETA_SALIDA / "informe_tendencias.txt"

# =========================================
# DICCIONARIOS Y STOPWORDS
# =========================================
STOPWORDS = {
    "la","el","los","las","de","del","y","en","a","un","una","que","se","con","por",
    "para","es","al","como","mas","menos","sus","su","o","u","ya","no","si",
    "pero","sin","sobre","entre","tambien","este","esta","estos","estas","lo","le",
    "les","me","te","mi","tu","nuestro","nuestra"
}

# Diccionarios de categorías (Normalizados sin tildes para mejor match)
CATEGORIAS = {
    "Religioso": {"dios", "jehova", "senor", "espiritu", "cielos", "creacion", "bendijo", "pecado", "profeta", "angel", "gloria", "mandamiento", "adoracion", "templo"},
    "Empresarial": {"mercado", "empresa", "innovacion", "estrategia", "productividad", "clientes", "competencia", "liderazgo", "transformacion", "digital", "datos", "crecimiento", "riesgo", "oportunidad"},
    "Tecnico": {"sistema", "proceso", "algoritmo", "codigo", "estructura", "funcion", "metodo", "modelo", "tecnologia", "computacion", "variable", "parametro", "analisis"},
    "Emocional": {"amor", "miedo", "tristeza", "alegria", "ira", "felicidad", "soledad", "esperanza", "ansiedad", "dolor", "pasion", "ternura", "culpa"},
    "Cientifico": {"teoria", "experimento", "investigacion", "evidencia", "hipotesis", "metodo", "cientifico", "observacion", "analisis", "resultados", "conclusion"}
}

# =========================================
# FUNCIONES DE PROCESAMIENTO
# =========================================

def normalizar(texto):
    """Elimina tildes, caracteres especiales y pasa a minúsculas."""
    # Quitar tildes
    texto = "".join(c for c in unicodedata.normalize('NFKD', texto) if not unicodedata.combining(c))
    # Limpiar caracteres no alfanuméricos
    texto = texto.lower()
    texto = re.sub(r"[^a-z0-9\s]", " ", texto)
    return texto.split()

def detectar_tipo(palabras):
    """Detecta el tipo de texto basado en la mayor densidad de palabras clave."""
    puntuaciones = {}
    total_palabras = len(palabras) if len(palabras) > 0 else 1
    
    for tipo, claves in CATEGORIAS.items():
        coincidencias = len(set(palabras).intersection(claves))
        # Calculamos densidad (porcentaje)
        puntuaciones[tipo] = (coincidencias / total_palabras) * 100

    tipo_detectado = max(puntuaciones, key=puntuaciones.get)
    
    if puntuaciones[tipo_detectado] == 0:
        return "General / Desconocido", 0
    
    return tipo_detectado, round(puntuaciones[tipo_detectado], 2)

# =========================================
# LÓGICA PRINCIPAL
# =========================================

def generar_informe():
    print("Iniciando D09 - Analisis de Texto...")
    
    # 1. Crear carpetas y verificar archivo
    CARPETA_ENTRADA.mkdir(exist_ok=True)
    CARPETA_SALIDA.mkdir(exist_ok=True)
    
    if not ARCHIVO_ENTRADA.exists():
        # Crear un archivo de ejemplo si no existe
        with open(ARCHIVO_ENTRADA, "w", encoding="utf-8") as f:
            f.write("La innovacion y la estrategia son claves en la empresa moderna para mitigar el riesgo.")
        print(f"Aviso: Se creo un archivo de ejemplo en {ARCHIVO_ENTRADA}")

    # 2. Leer y Procesar
    with open(ARCHIVO_ENTRADA, "r", encoding="utf-8") as f:
        contenido = f.read()

    palabras_sucias = contenido.lower().split()
    palabras_limpias = normalizar(contenido)
    
    # Filtrar stopwords para estadísticas
    palabras_filtradas = [p for p in palabras_limpias if p not in STOPWORDS and len(p) > 2]
    
    # 3. Analizar
    tipo, confianza = detectar_tipo(palabras_limpias)
    top_palabras = Counter(palabras_filtradas).most_common(10)
    
    # Bigramas (Parejas de palabras)
    parejas = zip(palabras_filtradas, palabras_filtradas[1:])
    top_bigramas = Counter([" ".join(p) for p in parejas]).most_common(5)

    # 4. Construir Reporte
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    reporte = [
        "===============================================",
        "   INFORME DE INTELIGENCIA TEXTUAL - D09",
        "===============================================",
        f"Fecha: {fecha}",
        f"Archivo: {ARCHIVO_ENTRADA.name}",
        f"Palabras totales: {len(palabras_limpias)}",
        f"Categoria detectada: {tipo} ({confianza}% de densidad)",
        "-----------------------------------------------\n",
        "TOP 10 PALABRAS CLAVE:"
    ]
    
    for p, f in top_palabras:
        reporte.append(f"- {p.capitalize()}: {f} veces")
        
    reporte.append("\nTOP 5 FRASES FRECUENTES (BIGRAMAS):")
    for b, f in top_bigramas:
        reporte.append(f"- \"{b}\": {f} veces")
        
    reporte.append("\nCONCLUSION:")
    reporte.append(f"El texto analizado muestra una clara tendencia hacia el ambito {tipo.lower()}.")

    # 5. Guardar
    with open(ARCHIVO_REPORTE, "w", encoding="utf-8") as f:
        f.write("\n".join(reporte))

    print(f"D09_OK: Informe generado en {ARCHIVO_REPORTE.name}")
    return True

if __name__ == "__main__":
    if generar_informe():
        sys.exit(0)
    else:
        sys.exit(1)

