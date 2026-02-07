import re
import unicodedata
from collections import Counter
from datetime import datetime

import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer

# ============================================================
# CONFIGURACIÓN Y DICCIONARIOS (Tu lógica mejorada)
# ============================================================

STOPWORDS = {
    "la","el","los","las","de","del","y","en","a","un","una","que","se","con","por",
    "para","es","al","como","mas","menos","sus","su","o","u","ya","no","si",
    "pero","sin","sobre","entre","tambien","este","esta","estos","estas","lo","le",
    "les","me","te","mi","tu","su","nuestro","nuestra"
}

# Diccionarios temáticos (Normalizados para evitar fallos por tildes)
CATEGORIAS_LLAVES = {
    "Religioso": {"dios","jehova","senor","espiritu","cielos","creacion","bendijo","pecado","profeta","angel","gloria","mandamiento","adoracion","templo"},
    "Empresarial": {"mercado","empresa","innovacion","estrategia","productividad","clientes","competencia","liderazgo","transformacion","digital","datos","crecimiento","riesgo","oportunidad"},
    "Técnico": {"sistema","proceso","algoritmo","codigo","estructura","funcion","metodo","modelo","tecnologia","computacion","variable","parametro","analisis"},
    "Emocional": {"amor","miedo","tristeza","alegria","ira","felicidad","soledad","esperanza","ansiedad","dolor","pasion","ternura","culpa"},
    "Narrativo": {"personaje","historia","relato","narracion","aventura","conflicto","viaje","heroe","villano","escena","capitulo","cuento","novela"},
    "Científico": {"teoria","experimento","investigacion","evidencia","hipotesis","metodo","cientifico","observacion","analisis","resultados","conclusion"},
    "Fantasía": {"mago","hechizo","magia","encantamiento","dragon","hada","duende","espada","reino","castillo","pocion","hechicero","bruja","portal","criatura"},
    "Cuento": {"erase","habia","principe","princesa","bosque","aventura","villano","heroe","castillo","hada","cuento","fabuloso","molinero","gato","rey"},
    "Fábula": {"moraleja","animales","leccion","ensenanza","sabiduria","zorro","cuervo","leon","raton","fabula"}
}

CLAVES_ESTILO = {
    "poetico": {"metafora","simbolo","verso","ritmo","imagen","lirico"},
    "descriptivo": {"detallado","paisaje","sensacion","color","forma","textura"},
    "directo": {"accion","rapido","dialogo","frases","cortas"},
    "clasico": {"antiguo","reino","caballero","don","senor","villa"},
    "moderno": {"ciudad","tecnologia","urbano","actual","moderno"}
}

# ============================================================
# FUNCIONES CORE (Tu motor de análisis)
# ============================================================

def normalizar_texto(texto: str):
    """Limpia tildes y caracteres especiales."""
    texto = "".join(c for c in unicodedata.normalize('NFKD', texto) if not unicodedata.combining(c))
    texto = texto.lower()
    texto = re.sub(r"[^a-z0-9\s]", " ", texto)
    return texto.split()

def frecuencia(palabras, top=15):
    palabras_filtradas = [p for p in palabras if p not in STOPWORDS and len(p) > 2]
    return Counter(palabras_filtradas).most_common(top)

def bigramas(palabras, top=10):
    b = zip(palabras, palabras[1:])
    b = [" ".join(x) for x in b]
    return Counter(b).most_common(top)

def detectar_tipo(palabras):
    puntuaciones = {tipo: len(set(palabras).intersection(claves)) for tipo, claves in CATEGORIAS_LLAVES.items()}
    tipo_detectado = max(puntuaciones, key=puntuaciones.get)
    # Umbral de confianza
    if puntuaciones[tipo_detectado] < 2:
        return "Narrativo / General", puntuaciones
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
            if palabra in lista: conteo[emo] += 1
    dominante = max(conteo, key=conteo.get)
    etiqueta = f"Predomina {dominante}" if conteo[dominante] > 0 else "Tono mixto / neutro"
    return {"emociones": conteo, "dominante": dominante, "etiqueta": etiqueta}

def top_tfidf_terms(texto, top_n=10):
    try:
        vectorizer = TfidfVectorizer(stop_words=list(STOPWORDS))
        tfidf_matrix = vectorizer.fit_transform([texto])
        feature_names = vectorizer.get_feature_names_out()
        scores = tfidf_matrix.toarray()[0]
        pairs = sorted(list(zip(feature_names, scores)), key=lambda x: x[1], reverse=True)
        return pairs[:top_n]
    except:
        return []

def resumen_narrativo(texto):
    oraciones = [o.strip() for o in texto.split(".") if o.strip()]
    if len(oraciones) < 3:
        return "Texto demasiado corto para un resumen narrativo estructurado."
    return f"**Inicio:** {oraciones[0]}. **Desarrollo:** {oraciones[len(oraciones)//2]}. **Final:** {oraciones[-1]}."

def detectar_estilo(palabras):
    puntuacion = {k: 0 for k in CLAVES_ESTILO}
    for estilo, claves in CLAVES_ESTILO.items():
        for palabra in palabras:
            if palabra in claves: puntuacion[estilo] += 1
    estilo_detectado = max(puntuacion, key=puntuacion.get)
    return estilo_detectado.capitalize() if puntuacion[estilo_detectado] > 0 else "Indefinido"

# ============================================================
# INTERFAZ STREAMLIT (UI Profesional)
# ============================================================

st.set_page_config(page_title="Día 10 - Analizador Ultra", layout="wide")

st.title("📊 Analizador Universal de Textos (Versión ULTRA)")
st.markdown(f"*Ejecución: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}*")
st.write("---")

col_input, col_opt = st.columns([2, 1])

with col_input:
    st.subheader("📝 Entrada de texto")
    modo = st.radio("Método de carga:", ["Pegar texto", "Subir archivo .txt"])
    if modo == "Pegar texto":
        texto = st.text_area("Contenido:", height=250, placeholder="Pega tu texto aquí...")
    else:
        archivo = st.file_uploader("Archivo:", type=["txt"])
        texto = archivo.read().decode("utf-8", errors="ignore") if archivo else ""

with col_opt:
    st.subheader("⚙️ Opciones")
    mostrar_tfidf = st.checkbox("Análisis TF-IDF (Estadístico)", value=True)
    mostrar_tono = st.checkbox("Tono Emocional", value=True)
    st.info("El análisis TF-IDF ayuda a encontrar palabras con mayor peso semántico.")

if st.button("🚀 INICIAR ANÁLISIS"):
    if not texto.strip():
        st.warning("Introduce texto para continuar.")
    else:
        # Procesar
        palabras = normalizar_texto(texto)
        tipo, scores = detectar_tipo(palabras)
        
        # UI de Resultados
        st.success(f"### Resultado: {tipo}")
        
        res_col1, res_col2, res_col3 = st.columns(3)
        res_col1.metric("Total Palabras", len(palabras))
        res_col2.metric("Estilo", detectar_estilo(palabras))
        res_col3.metric("Sentimiento", analizar_tono_emocional(palabras)["dominante"].capitalize())

        st.write("---")
        
        tab1, tab2, tab3 = st.tabs(["📊 Estadísticas", "📖 Resumen", "🔬 Detalle Técnico"])
        
        with tab1:
            c1, c2 = st.columns(2)
            with c1:
                st.write("**Palabras más frecuentes**")
                st.table(frecuencia(palabras))
            with c2:
                st.write("**Bigramas (Frases comunes)**")
                st.table(bigramas(palabras))
        
        with tab2:
            st.write("**Resumen de la estructura:**")
            st.info(resumen_narrativo(texto))
        
        with tab3:
            if mostrar_tfidf:
                st.write("**Términos clave (TF-IDF):**")
                st.json(top_tfidf_terms(texto))
            if mostrar_tono:
                st.write("**Desglose Emocional:**")
                st.bar_chart(analizar_tono_emocional(palabras)["emociones"])

