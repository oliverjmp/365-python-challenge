import re
from collections import Counter
from datetime import datetime

import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer

# =========================
# Configuración y diccionarios
# =========================

STOPWORDS = {
    "la","el","los","las","de","del","y","en","a","un","una","que","se","con","por",
    "para","es","al","como","mas","menos","sus","su","o","u","ya","no","si",
    "pero","sin","sobre","entre","tambien","este","esta","estos","estas","lo","le",
    "les","me","te","mi","tu","su","nuestro","nuestra"
}

CLAVES_RELIGIOSO = {
    "dios","jehova","senor","espiritu","cielos","creacion","bendijo","pecado","profeta",
    "angel","gloria","mandamiento","adoracion","templo"
}

CLAVES_EMPRESARIAL = {
    "mercado","empresa","innovacion","estrategia","productividad","clientes","competencia",
    "liderazgo","transformacion","digital","datos","crecimiento","riesgo","oportunidad"
}

CLAVES_TECNICO = {
    "sistema","proceso","algoritmo","codigo","estructura","funcion","metodo","modelo",
    "tecnologia","computacion","variable","parametro","analisis"
}

CLAVES_EMOCIONAL = {
    "amor","miedo","tristeza","alegria","ira","felicidad","soledad","esperanza",
    "ansiedad","dolor","pasion","ternura","culpa"
}

CLAVES_NARRATIVO = {
    "personaje","historia","relato","narracion","aventura","conflicto","viaje","heroe",
    "villano","escena","capitulo","cuento","novela","mago","ciudad","bosque"
}

CLAVES_CIENTIFICO = {
    "teoria","experimento","investigacion","evidencia","hipotesis","metodo","cientifico",
    "observacion","analisis","resultados","conclusion"
}

CLAVES_FANTASIA = {
    "mago","hechizo","magia","encantamiento","dragon","hada","duende","espada",
    "reino","castillo","pocion","hechicero","bruja","portal","criatura","fantasma"
}

CLAVES_CUENTO = {
    "erase","habia","principe","princesa","bosque","aventura","villano","heroe",
    "castillo","hada","cuento","fabuloso","molinero","gato","rey","ciudad"
}

CLAVES_FABULA = {
    "moraleja","animales","leccion","ensenanza","sabiduria","zorro","cuervo",
    "leon","raton","fabula"
}

CLAVES_ESTILO = {
    "poetico": {"metafora","simbolo","verso","ritmo","imagen","lirico"},
    "descriptivo": {"detallado","paisaje","sensacion","color","forma","textura"},
    "directo": {"accion","rapido","dialogo","frases","cortas"},
    "clasico": {"antiguo","reino","caballero","don","senor","villa"},
    "moderno": {"ciudad","tecnologia","urbano","actual","moderno"}
}

# =========================
# Funciones core
# =========================

def limpiar_texto(texto: str):
    texto = texto.lower()
    texto = re.sub(r"[^a-z0-9\s]", " ", texto)
    return texto.split()

def frecuencia(palabras, top=15):
    palabras = [p for p in palabras if p not in STOPWORDS]
    return Counter(palabras).most_common(top)

def bigramas(palabras, top=10):
    b = zip(palabras, palabras[1:])
    b = [" ".join(x) for x in b]
    return Counter(b).most_common(top)

def detectar_tipo(palabras):
    categorias = {
        "Religioso": CLAVES_RELIGIOSO,
        "Empresarial": CLAVES_EMPRESARIAL,
        "Técnico": CLAVES_TECNICO,
        "Emocional": CLAVES_EMOCIONAL,
        "Narrativo": CLAVES_NARRATIVO,
        "Científico": CLAVES_CIENTIFICO,
        "Fantasía": CLAVES_FANTASIA,
        "Cuento": CLAVES_CUENTO,
        "Fábula": CLAVES_FABULA
    }

    puntuaciones = {
        tipo: len(set(palabras).intersection(claves))
        for tipo, claves in categorias.items()
    }

    tipo_detectado = max(puntuaciones, key=puntuaciones.get)

    if puntuaciones[tipo_detectado] < 2:
        return "Narrativo", puntuaciones

    return tipo_detectado, puntuaciones

def analizar_tono_emocional(palabras):
    emociones = {
        "miedo": ["miedo","temor","pavor","asustado"],
        "tristeza": ["triste","llanto","pena","dolor"],
        "ira": ["ira","rabia","furia","enojo"],
        "alegria": ["feliz","alegria","risa","contento"],
        "tension": ["persecucion","peligro","urgencia","conflicto"]
    }

    conteo = {e: 0 for e in emociones}

    for palabra in palabras:
        for emo, lista in emociones.items():
            if palabra in lista:
                conteo[emo] += 1

    dominante = max(conteo, key=conteo.get)
    etiqueta = f"Predomina {dominante}" if conteo[dominante] > 0 else "Tono mixto / neutro"

    return {
        "emociones": conteo,
        "dominante": dominante,
        "etiqueta": etiqueta
    }

def top_tfidf_terms(texto, top_n=10):
    vectorizer = TfidfVectorizer(stop_words=None)
    tfidf_matrix = vectorizer.fit_transform([texto])
    feature_names = vectorizer.get_feature_names_out()
    scores = tfidf_matrix.toarray()[0]
    pairs = list(zip(feature_names, scores))
    pairs.sort(key=lambda x: x[1], reverse=True)
    return pairs[:top_n]

def analisis_especializado(tipo, palabras):
    if tipo in ("Narrativo","Cuento","Fantasía","Fábula"):
        return ["Texto narrativo con elementos de historia, personajes y posible componente fantástico o moral."]
    if tipo == "Empresarial":
        return ["Contenido empresarial con enfoque estratégico o de mercado."]
    if tipo == "Técnico":
        return ["Contenido técnico basado en procesos, sistemas o algoritmos."]
    if tipo == "Emocional":
        return ["Texto con carga emocional explícita o implícita."]
    if tipo == "Científico":
        return ["Contenido científico basado en evidencia y análisis estructurado."]
    if tipo == "Religioso":
        return ["Contenido espiritual o simbólico."]
    return ["No se pudo determinar un tipo claro."]

def resumen_narrativo(texto):
    oraciones = [o.strip() for o in texto.split(".") if o.strip()]
    if len(oraciones) < 3:
        return "Texto demasiado corto para un resumen narrativo."

    inicio = oraciones[0]
    nudo = oraciones[len(oraciones)//2]
    final = oraciones[-1]

    return f"Inicio: {inicio}. Desarrollo: {nudo}. Final: {final}."

def detectar_estilo(palabras):
    puntuacion = {k: 0 for k in CLAVES_ESTILO}

    for estilo, claves in CLAVES_ESTILO.items():
        for palabra in palabras:
            if palabra in claves:
                puntuacion[estilo] += 1

    estilo_detectado = max(puntuacion, key=puntuacion.get)

    return estilo_detectado if puntuacion[estilo_detectado] > 0 else "Indefinido"

# =========================
# Streamlit UI
# =========================

st.set_page_config(page_title="Día 10 - Analizador Universal ULTRA", layout="wide")

st.title("📊 Día 10 — Analizador Universal de Textos (Versión ULTRA)")
st.write("Interfaz web + análisis avanzado + modelos estadísticos.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Entrada de texto")
    modo = st.radio("¿Cómo quieres cargar el texto?", ["Pegar texto", "Subir archivo .txt"])

    texto = ""
    if modo == "Pegar texto":
        texto = st.text_area("Pega aquí el contenido a analizar", height=300)
    else:
        archivo = st.file_uploader("Sube un archivo .txt", type=["txt"])
        if archivo is not None:
            texto = archivo.read().decode("utf-8", errors="ignore")

with col2:
    st.subheader("Opciones de análisis")
    mostrar_tfidf = st.checkbox("Incluir términos clave por TF-IDF", value=True)
    mostrar_tono = st.checkbox("Incluir análisis de tono emocional", value=True)

if st.button("🔍 Analizar texto", type="primary"):
    if not texto or not texto.strip():
        st.error("El texto está vacío. Por favor, introduce o sube contenido.")
    else:
        palabras = limpiar_texto(texto)
        total = len(palabras)

        tipo, puntuaciones = detectar_tipo(palabras)
        freqs = frecuencia(palabras, top=15)
        bigs = bigramas(palabras, top=10)
        tono = analizar_tono_emocional(palabras) if mostrar_tono else {"etiqueta": "no evaluado", "emociones": {}, "dominante": "ninguna"}
        tfidf_terms = top_tfidf_terms(texto, top_n=10) if mostrar_tfidf else []

        analisis_tipo = analisis_especializado(tipo, palabras)

        st.success(f"Tipo de texto detectado: **{tipo}**")
        st.write(f"Total de palabras: **{total}**")

        col_a, col_b = st.columns(2)

        with col_a:
            st.subheader("Palabras más frecuentes")
            st.table({"Palabra": [p for p, _ in freqs], "Frecuencia": [f for _, f in freqs]})

            st.subheader("Bigramas más frecuentes")
            st.table({"Bigrama": [b for b, _ in bigs], "Frecuencia": [f for _, f in bigs]})

        with col_b:
            if mostrar_tfidf and tfidf_terms:
                st.subheader("Términos clave (TF-IDF)")
                st.table({"Término": [t for t, _ in tfidf_terms], "Score": [round(s, 4) for _, s in tfidf_terms]})

            if mostrar_tono:
                st.subheader("Tono emocional")
                st.write(f"- Emoción dominante: **{tono['dominante']}**")
                st.write(f"- Detalle: {tono['emociones']}")

        st.subheader("Análisis especializado según tipo de texto")
        for linea in analisis_tipo:
            st.markdown(f"- {linea}")

        st.subheader("Resumen narrativo automático")
        st.write(resumen_narrativo(texto))

        st.subheader("Estilo literario detectado")
        st.write(detectar_estilo(palabras))

