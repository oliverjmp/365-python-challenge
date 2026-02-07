import os
import re
from collections import Counter
from datetime import datetime

# =========================================
# CONFIGURACIÓN GENERAL
# =========================================

CARPETA_ENTRADA = "textos"
NOMBRE_ARCHIVO = "entrada.txt"
CARPETA_SALIDA = "reportes"
NOMBRE_REPORTE = "informe_tendencias.txt"

STOPWORDS = {
    "la","el","los","las","de","del","y","en","a","un","una","que","se","con","por",
    "para","es","al","como","más","menos","sus","su","sus","o","u","ya","no","sí",
    "pero","sin","sobre","entre","también","este","esta","estos","estas","lo","le",
    "les","me","te","mi","tu","su","nuestro","nuestra"
}

# Palabras clave por tipo de texto
CLAVES_RELIGIOSO = {
    "dios","jehová","señor","espíritu","cielos","creación","bendijo","pecado","profeta",
    "ángel","gloria","mandamiento","adoración","templo"
}

CLAVES_EMPRESARIAL = {
    "mercado","empresa","innovación","estrategia","productividad","clientes","competencia",
    "liderazgo","transformación","digital","datos","crecimiento","riesgo","oportunidad"
}

CLAVES_TECNICO = {
    "sistema","proceso","algoritmo","código","estructura","función","método","modelo",
    "tecnología","computación","variable","parámetro","análisis"
}

CLAVES_EMOCIONAL = {
    "amor","miedo","tristeza","alegría","ira","felicidad","soledad","esperanza",
    "ansiedad","dolor","pasión","ternura","culpa"
}

CLAVES_NARRATIVO = {
    "personaje","historia","relato","narración","aventura","conflicto","viaje","héroe",
    "villano","escena","capítulo","cuento","novela"
}

CLAVES_CIENTIFICO = {
    "teoría","experimento","investigación","evidencia","hipótesis","método","científico",
    "observación","análisis","resultados","conclusión"
}

# =========================================
# FUNCIONES BÁSICAS
# =========================================

def limpiar_texto(texto):
    texto = texto.lower()
    texto = re.sub(r"[^a-záéíóúñü0-9\s]", " ", texto)
    return texto.split()

def cargar_texto():
    carpeta = os.path.dirname(os.path.abspath(__file__))
    ruta = os.path.join(carpeta, CARPETA_ENTRADA, NOMBRE_ARCHIVO)

    if not os.path.exists(ruta):
        print(f"ERROR: No se encontró el archivo:\n{ruta}")
        return None, ruta

    with open(ruta, "r", encoding="utf-8") as f:
        contenido = f.read()

    if not contenido.strip():
        print(f"ERROR: El archivo está vacío:\n{ruta}")
        return None, ruta

    return contenido, ruta

def frecuencia(palabras, top=15):
    palabras = [p for p in palabras if p not in STOPWORDS]
    return Counter(palabras).most_common(top)

def bigramas(palabras, top=10):
    b = zip(palabras, palabras[1:])
    b = [" ".join(x) for x in b]
    return Counter(b).most_common(top)

# =========================================
# DETECCIÓN DEL TIPO DE TEXTO
# =========================================

def detectar_tipo(palabras):
    sets = {
        "Religioso": CLAVES_RELIGIOSO,
        "Empresarial": CLAVES_EMPRESARIAL,
        "Técnico": CLAVES_TECNICO,
        "Emocional": CLAVES_EMOCIONAL,
        "Narrativo": CLAVES_NARRATIVO,
        "Científico": CLAVES_CIENTIFICO
    }

    puntuaciones = {}

    for tipo, claves in sets.items():
        puntuaciones[tipo] = len(set(palabras).intersection(claves))

    tipo_detectado = max(puntuaciones, key=puntuaciones.get)

    if puntuaciones[tipo_detectado] == 0:
        return "Desconocido"

    return tipo_detectado

# =========================================
# ANÁLISIS ESPECIALIZADO POR TIPO
# =========================================

def analisis_religioso(palabras):
    temas = []
    if "creación" in palabras or "cielos" in palabras:
        temas.append("Creación y origen del mundo")
    if "dios" in palabras:
        temas.append("Relación entre Dios y la humanidad")
    if "bendijo" in palabras:
        temas.append("Bendición y propósito")

    return temas or ["Temas espirituales y simbólicos presentes en el texto."]

def analisis_empresarial(palabras):
    temas = []
    if "innovación" in palabras:
        temas.append("Innovación como motor estratégico")
    if "riesgo" in palabras:
        temas.append("Gestión de riesgos en entornos cambiantes")
    if "clientes" in palabras:
        temas.append("Enfoque en experiencia del cliente")

    return temas or ["Texto empresarial general sin enfoque dominante."]

def analisis_tecnico(palabras):
    return ["Contenido técnico basado en procesos, sistemas o algoritmos."]

def analisis_emocional(palabras):
    emociones = []
    for e in CLAVES_EMOCIONAL:
        if e in palabras:
            emociones.append(e)
    return emociones or ["Emociones implícitas sin predominancia clara."]

def analisis_narrativo(palabras):
    return ["Estructura narrativa con personajes, escenas o conflicto."]

def analisis_cientifico(palabras):
    return ["Contenido científico basado en evidencia y análisis."]

def analisis_desconocido():
    return ["No se pudo determinar el tipo de texto con claridad."]

# =========================================
# GENERACIÓN DEL INFORME
# =========================================

def generar_informe():
    texto, ruta = cargar_texto()
    if texto is None:
        return

    palabras = limpiar_texto(texto)
    total = len(palabras)

    tipo = detectar_tipo(palabras)

    # Selección del análisis según tipo
    if tipo == "Religioso":
        analisis = analisis_religioso(palabras)
    elif tipo == "Empresarial":
        analisis = analisis_empresarial(palabras)
    elif tipo == "Técnico":
        analisis = analisis_tecnico(palabras)
    elif tipo == "Emocional":
        analisis = analisis_emocional(palabras)
    elif tipo == "Narrativo":
        analisis = analisis_narrativo(palabras)
    elif tipo == "Científico":
        analisis = analisis_cientifico(palabras)
    else:
        analisis = analisis_desconocido()

    # Construcción del informe
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    reporte = []
    reporte.append("=== INFORME DE ANÁLISIS UNIVERSAL — DÍA 09 ===\n\n")
    reporte.append(f"Fecha: {fecha}\n")
    reporte.append(f"Archivo analizado: {ruta}\n")
    reporte.append(f"Total de palabras: {total}\n")
    reporte.append(f"Tipo de texto detectado: {tipo}\n")
    reporte.append("-" * 60 + "\n\n")

    reporte.append("1) Palabras más frecuentes\n")
    for p, f in frecuencia(palabras):
        reporte.append(f"- {p}: {f}\n")
    reporte.append("\n")

    reporte.append("2) Expresiones frecuentes (bigramas)\n")
    for b, f in bigramas(palabras):
        reporte.append(f"- \"{b}\": {f}\n")
    reporte.append("\n")

    reporte.append("3) Análisis especializado según tipo de texto\n")
    for linea in analisis:
        reporte.append(f"- {linea}\n")
    reporte.append("\n")

    reporte.append("4) Resumen ejecutivo adaptado\n")

    if tipo == "Religioso":
        reporte.append(
            "El texto presenta una estructura simbólica y espiritual, con énfasis en temas de origen, propósito y relación entre lo divino y lo humano.\n"
        )
    elif tipo == "Narrativo":
        reporte.append(
            "El texto desarrolla una secuencia narrativa con elementos de trama, personajes y progresión temática.\n"
        )
    elif tipo == "Empresarial":
        reporte.append(
            "El contenido refleja dinámicas estratégicas, tendencias de mercado y elementos clave para la toma de decisiones.\n"
        )
    elif tipo == "Técnico":
        reporte.append(
            "El texto se centra en procesos, sistemas o conceptos estructurados propios del ámbito técnico.\n"
        )
    elif tipo == "Emocional":
        reporte.append(
            "El texto transmite emociones explícitas o implícitas que influyen en el tono general del contenido.\n"
        )
    elif tipo == "Científico":
        reporte.append(
            "El texto presenta un enfoque basado en evidencia, análisis y razonamiento estructurado.\n"
        )
    else:
        reporte.append(
            "El texto no encaja claramente en una categoría específica, pero presenta patrones lingüísticos relevantes.\n"
        )

    # Guardar
    carpeta = os.path.dirname(os.path.abspath(__file__))
    salida = os.path.join(carpeta, CARPETA_SALIDA)
    os.makedirs(salida, exist_ok=True)

    ruta_reporte = os.path.join(salida, NOMBRE_REPORTE)

    with open(ruta_reporte, "w", encoding="utf-8") as f:
        f.write("".join(reporte))

    print(f"\nInforme generado correctamente:\n{ruta_reporte}")

# =========================================
# EJECUCIÓN
# =========================================

if __name__ == "__main__":
    generar_informe()

