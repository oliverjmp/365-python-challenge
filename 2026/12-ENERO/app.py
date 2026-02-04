import streamlit as st
import pandas as pd
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, confusion_matrix
from preprocesamiento import detectar_idioma, normalizar_texto
# ============================================================
# 1. DATASET AMPLIADO (POSITIVO, NEGATIVO, NEUTRO, SARCASMO, AMBIGUO)
# ============================================================

# 100 positivas
frases_positivas = [
    "Me encantó la atención, todo fue perfecto.",
    "El servicio fue excelente y muy rápido.",
    "Estoy muy satisfecho con el resultado final.",
    "La experiencia superó mis expectativas.",
    "Todo salió mejor de lo que imaginaba.",
    "El producto funciona de maravilla.",
    "Me alegra haber elegido esta opción.",
    "Fue una experiencia realmente agradable.",
    "El equipo fue amable y profesional.",
    "Volvería sin dudarlo.",
    "La calidad es impresionante.",
    "Estoy feliz con la compra.",
    "El trato fue impecable.",
    "Me hicieron sentir muy bien.",
    "Todo estuvo genial desde el principio.",
    "La atención al cliente fue excelente.",
    "Me sorprendió lo bien que salió todo.",
    "Muy recomendable.",
    "Estoy encantado con el servicio.",
    "Fue una experiencia inolvidable.",
    "Todo estuvo perfectamente organizado.",
    "Me siento muy satisfecho.",
    "El ambiente era muy agradable.",
    "La comida estaba deliciosa.",
    "El proceso fue sencillo y rápido.",
    "Me ayudaron en todo momento.",
    "El resultado fue espectacular.",
    "Estoy muy contento con la decisión.",
    "La experiencia fue fantástica.",
    "Todo funcionó a la perfección.",
    "El personal fue muy atento.",
    "Me hicieron sentir especial.",
    "La entrega fue puntual y eficiente.",
    "El diseño es hermoso.",
    "La calidad supera el precio.",
    "Estoy muy impresionado.",
    "Fue una experiencia muy positiva.",
    "Todo estuvo mejor de lo esperado.",
    "Me encantó cada detalle.",
    "El servicio fue impecable.",
    "La atención fue de primera.",
    "Estoy muy agradecido.",
    "Fue una experiencia maravillosa.",
    "Todo estuvo excelente.",
    "Me sorprendió gratamente.",
    "El producto es de alta calidad.",
    "Estoy muy feliz con el resultado.",
    "El trato fue excepcional.",
    "La experiencia fue muy agradable.",
    "Todo estuvo perfecto.",
    "Me encantó el ambiente.",
    "El servicio fue sobresaliente.",
    "Estoy muy satisfecho con la compra.",
    "La atención fue increíble.",
    "El proceso fue muy cómodo.",
    "Me encantó la rapidez del servicio.",
    "Todo estuvo muy bien organizado.",
    "Estoy muy contento con el trato.",
    "La experiencia fue muy positiva.",
    "Me encantó el resultado final.",
    "El personal fue muy amable.",
    "Todo salió excelente.",
    "Estoy muy feliz con la experiencia.",
    "La calidad es excepcional.",
    "Me encantó el servicio recibido.",
    "Fue una experiencia muy buena.",
    "Estoy muy satisfecho con todo.",
    "El producto superó mis expectativas.",
    "Me encantó la atención recibida.",
    "Todo estuvo increíble.",
    "Estoy muy contento con el resultado.",
    "La experiencia fue perfecta.",
    "El servicio fue maravilloso.",
    "Me encantó la eficiencia del equipo.",
    "Todo estuvo muy bien.",
    "Estoy muy agradecido por el servicio.",
    "La atención fue excelente.",
    "Me encantó la experiencia completa.",
    "El producto es fantástico.",
    "Estoy muy satisfecho con el proceso.",
    "Todo estuvo genial.",
    "Me encantó cómo me atendieron.",
    "La experiencia fue muy buena.",
    "Estoy muy feliz con la decisión tomada.",
    "El servicio fue muy profesional.",
    "Todo estuvo perfecto desde el inicio.",
    "Me encantó la calidad del producto.",
    "Estoy muy contento con la atención.",
    "La experiencia fue maravillosa.",
    "Todo estuvo excelente.",
    "Me encantó el trato recibido.",
    "Estoy muy satisfecho con el servicio.",
    "La atención fue espectacular.",
    "Me encantó el resultado.",
    "Todo estuvo muy bien hecho.",
    "Estoy muy feliz con el servicio.",
    "La experiencia fue increíble.",
    "Me encantó todo.",
    "El servicio fue perfecto.",
    "Estoy muy satisfecho con la experiencia."
]

# 100 negativas
frases_negativas = [
    "El servicio fue terrible.",
    "Estoy muy decepcionado con el resultado.",
    "La experiencia fue pésima.",
    "No volvería jamás.",
    "El producto llegó defectuoso.",
    "La atención fue muy mala.",
    "Todo salió mal.",
    "Fue una pérdida de tiempo.",
    "El personal fue grosero.",
    "La calidad es muy baja.",
    "Estoy muy insatisfecho.",
    "La experiencia fue frustrante.",
    "Nada salió como esperaba.",
    "El servicio fue lento y deficiente.",
    "Me arrepiento de haber elegido esta opción.",
    "El ambiente era desagradable.",
    "La comida estaba horrible.",
    "El proceso fue complicado y lento.",
    "No recibí ayuda en ningún momento.",
    "El resultado fue un desastre.",
    "Estoy muy molesto.",
    "La experiencia fue muy mala.",
    "Todo estuvo mal organizado.",
    "Me trataron muy mal.",
    "La entrega fue muy tardía.",
    "El diseño es feo.",
    "La calidad no vale el precio.",
    "Estoy muy decepcionado.",
    "Fue una experiencia muy negativa.",
    "Todo estuvo peor de lo esperado.",
    "No me gustó nada.",
    "El servicio fue pésimo.",
    "La atención fue horrible.",
    "Estoy muy enojado.",
    "Fue una experiencia terrible.",
    "Todo estuvo mal.",
    "Me trataron de forma irrespetuosa.",
    "La entrega fue un desastre.",
    "El producto es de mala calidad.",
    "Estoy muy frustrado.",
    "La experiencia fue muy desagradable.",
    "Todo estuvo fatal.",
    "Me arrepiento de la compra.",
    "El servicio fue muy malo.",
    "La atención fue deficiente.",
    "Estoy muy molesto con el resultado.",
    "La experiencia fue horrible.",
    "Todo salió mal desde el principio.",
    "Me trataron muy mal.",
    "La calidad es pésima.",
    "Estoy muy insatisfecho con el servicio.",
    "La experiencia fue muy mala.",
    "Todo estuvo mal hecho.",
    "Me decepcionó completamente.",
    "El servicio fue un desastre.",
    "La atención fue muy mala.",
    "Estoy muy frustrado con el proceso.",
    "La experiencia fue terrible.",
    "Todo estuvo muy mal.",
    "Me arrepiento totalmente.",
    "El producto es pésimo.",
    "Estoy muy molesto con la atención.",
    "La experiencia fue muy negativa.",
    "Todo estuvo peor de lo esperado.",
    "Me trataron muy mal.",
    "La calidad es muy baja.",
    "Estoy muy decepcionado con el servicio.",
    "La experiencia fue horrible.",
    "Todo estuvo mal organizado.",
    "Me arrepiento de haber comprado esto.",
    "El servicio fue muy malo.",
    "La atención fue pésima.",
    "Estoy muy insatisfecho con el resultado.",
    "La experiencia fue muy mala.",
    "Todo estuvo fatal.",
    "Me trataron de forma grosera.",
    "La calidad es pésima.",
    "Estoy muy molesto con el producto.",
    "La experiencia fue terrible.",
    "Todo salió mal.",
    "Me arrepiento de la decisión.",
    "El servicio fue muy malo.",
    "La atención fue deficiente.",
    "Estoy muy frustrado con la compra.",
    "La experiencia fue muy negativa.",
    "Todo estuvo mal.",
    "Me decepcionó completamente.",
    "El producto es de mala calidad.",
    "Estoy muy insatisfecho con el servicio.",
    "La experiencia fue horrible.",
    "Todo estuvo mal hecho.",
    "Me arrepiento totalmente.",
    "El servicio fue pésimo.",
    "La atención fue muy mala.",
    "Estoy muy molesto con el resultado.",
    "La experiencia fue terrible.",
    "Todo estuvo fatal."
]

# 100 neutras
frases_neutras = [
    "El producto cumple su función.",
    "La reunión duró una hora.",
    "El paquete llegó en la fecha indicada.",
    "El servicio fue adecuado.",
    "La experiencia fue normal.",
    "El resultado fue aceptable.",
    "El ambiente era tranquilo.",
    "La comida estaba bien.",
    "El proceso fue estándar.",
    "La atención fue correcta.",
    "El diseño es simple.",
    "El producto funciona como se esperaba.",
    "La entrega fue puntual.",
    "El servicio fue razonable.",
    "La experiencia fue neutra.",
    "El resultado fue el esperado.",
    "El ambiente era normal.",
    "La comida estaba bien preparada.",
    "El proceso fue adecuado.",
    "La atención fue suficiente.",
    "El diseño es básico.",
    "El producto cumple lo prometido.",
    "La entrega fue correcta.",
    "El servicio fue aceptable.",
    "La experiencia fue estándar.",
    "El resultado fue correcto.",
    "El ambiente era adecuado.",
    "La comida estaba bien servida.",
    "El proceso fue normal.",
    "La atención fue apropiada.",
    "El diseño es funcional.",
    "El producto funciona correctamente.",
    "La entrega fue normal.",
    "El servicio fue suficiente.",
    "La experiencia fue adecuada.",
    "El resultado fue razonable.",
    "El ambiente era simple.",
    "La comida estaba bien hecha.",
    "El proceso fue correcto.",
    "La atención fue normal.",
    "El diseño es sencillo.",
    "El producto cumple su propósito.",
    "La entrega fue adecuada.",
    "El servicio fue estándar.",
    "La experiencia fue correcta.",
    "El resultado fue aceptable.",
    "El ambiente era neutro.",
    "La comida estaba bien presentada.",
    "El proceso fue suficiente.",
    "La atención fue razonable.",
    "El diseño es básico.",
    "El producto funciona como debe.",
    "La entrega fue puntual.",
    "El servicio fue adecuado.",
    "La experiencia fue normal.",
    "El resultado fue el esperado.",
    "El ambiente era tranquilo.",
    "La comida estaba bien.",
    "El proceso fue estándar.",
    "La atención fue correcta.",
    "El diseño es simple.",
    "El producto cumple lo esperado.",
    "La entrega fue correcta.",
    "El servicio fue aceptable.",
    "La experiencia fue estándar.",
    "El resultado fue correcto.",
    "El ambiente era adecuado.",
    "La comida estaba bien servida.",
    "El proceso fue normal.",
    "La atención fue apropiada.",
    "El diseño es funcional.",
    "El producto funciona correctamente.",
    "La entrega fue normal.",
    "El servicio fue suficiente.",
    "La experiencia fue adecuada.",
    "El resultado fue razonable.",
    "El ambiente era simple.",
    "La comida estaba bien hecha.",
    "El proceso fue correcto.",
    "La atención fue normal.",
    "El diseño es sencillo.",
    "El producto cumple su propósito.",
    "La entrega fue adecuada.",
    "El servicio fue estándar.",
    "La experiencia fue correcta.",
    "El resultado fue aceptable.",
    "El ambiente era neutro.",
    "La comida estaba bien presentada.",
    "El proceso fue suficiente.",
    "La atención fue razonable.",
    "El diseño es básico.",
    "El producto funciona como debe.",
    "La entrega fue puntual.",
    "El servicio fue adecuado.",
    "La experiencia fue normal.",
    "El resultado fue el esperado.",
    "El ambiente era tranquilo.",
    "La comida estaba bien.",
    "El proceso fue estándar.",
    "La atención fue correcta."
]

# 50 sarcásticas
frases_sarcasticas = [
    "Sí, claro, fue maravilloso esperar tres horas para que me atendieran.",
    "Qué alegría, otra vez se rompió el sistema justo cuando más lo necesitaba.",
    "Fantástico, ahora tengo que empezar todo el proceso desde cero.",
    "Genial, justo lo que quería: más problemas.",
    "Perfecto, otro error inesperado. Qué sorpresa.",
    "Maravilloso, el pedido llegó roto. Justo lo que esperaba.",
    "Excelente, ahora funciona peor que antes.",
    "Qué bien, otra vez tengo que llamar al soporte técnico.",
    "Increíble, el servicio fue tan rápido como una tortuga.",
    "Qué suerte, me cobraron de más. Fantástico.",
    "Perfecto, ahora no funciona nada.",
    "Qué emoción, otra vez tengo que reiniciar todo.",
    "Genial, el sistema se cayó justo cuando estaba trabajando.",
    "Qué maravilla, el producto duró exactamente un día.",
    "Excelente, otra actualización que no arregla nada.",
    "Qué bien, ahora tengo más problemas que antes.",
    "Fantástico, el servicio fue tan útil como una piedra.",
    "Qué alegría, el envío se retrasó otra semana.",
    "Perfecto, justo lo que necesitaba: más complicaciones.",
    "Qué emoción, el soporte no responde nunca.",
    "Genial, ahora tengo que repetir todo el proceso.",
    "Qué maravilla, el sistema falló otra vez.",
    "Excelente, el producto dejó de funcionar sin motivo.",
    "Qué bien, otra vez tengo que esperar horas.",
    "Fantástico, el servicio fue un desastre total.",
    "Qué suerte, el pedido llegó incompleto.",
    "Perfecto, ahora tengo que empezar de nuevo.",
    "Qué emoción, el sistema se bloqueó otra vez.",
    "Genial, el servicio fue tan útil como un adorno.",
    "Qué maravilla, el producto no hace nada de lo que promete.",
    "Excelente, otra vez tengo que llamar al soporte.",
    "Qué bien, el sistema se cayó justo ahora.",
    "Fantástico, el servicio fue tan rápido como un caracol.",
    "Qué suerte, el pedido llegó tarde otra vez.",
    "Perfecto, ahora tengo que reiniciar todo.",
    "Qué emoción, el producto dejó de funcionar.",
    "Genial, el servicio fue tan útil como un ladrillo.",
    "Qué maravilla, el sistema falló de nuevo.",
    "Excelente, otra vez tengo que repetir todo.",
    "Qué bien, el servicio fue un desastre.",
    "Fantástico, el producto llegó roto.",
    "Qué suerte, el sistema se bloqueó.",
    "Perfecto, ahora tengo más problemas.",
    "Qué emoción, el soporte no responde.",
    "Genial, el servicio fue inútil.",
    "Qué maravilla, el producto no sirve.",
    "Excelente, el sistema falló.",
    "Qué bien, el pedido llegó mal.",
    "Fantástico, el servicio fue pésimo.",
    "Qué suerte, todo salió mal."
]

# 50 ambiguas
frases_ambiguas = [
    "No estuvo mal, pero tampoco fue increíble.",
    "El servicio fue bueno, aunque esperaba más.",
    "La experiencia fue aceptable, pero podría mejorar.",
    "No fue lo peor, pero tampoco lo mejor.",
    "El producto funciona, aunque no como esperaba.",
    "La atención fue correcta, pero un poco lenta.",
    "La comida estaba bien, aunque el ambiente no tanto.",
    "El proceso fue sencillo, pero algo confuso al inicio.",
    "El resultado fue bueno, aunque no perfecto.",
    "La experiencia fue agradable, pero con algunos problemas.",
    "El servicio fue rápido, aunque no muy amable.",
    "El producto cumple, pero no sorprende.",
    "La atención fue buena, aunque un poco fría.",
    "La experiencia fue positiva, pero con detalles a mejorar.",
    "El resultado fue aceptable, aunque esperaba más.",
    "El ambiente era agradable, pero algo ruidoso.",
    "La comida estaba rica, aunque un poco salada.",
    "El proceso fue fácil, pero tardó más de lo esperado.",
    "La atención fue amable, pero poco eficiente.",
    "La experiencia fue buena, aunque no memorable.",
    "El servicio fue correcto, pero podría ser mejor.",
    "El producto funciona bien, aunque no es perfecto.",
    "La atención fue rápida, pero poco personalizada.",
    "La experiencia fue neutra, aunque con momentos buenos.",
    "El resultado fue razonable, pero no excelente.",
    "El ambiente era cómodo, pero algo oscuro.",
    "La comida estaba bien, aunque un poco fría.",
    "El proceso fue adecuado, pero algo largo.",
    "La atención fue suficiente, pero no destacable.",
    "La experiencia fue normal, aunque esperaba más.",
    "El servicio fue aceptable, pero no sobresaliente.",
    "El producto cumple, aunque no destaca.",
    "La atención fue correcta, pero poco cálida.",
    "La experiencia fue buena, aunque con altibajos.",
    "El resultado fue adecuado, pero no sorprendente.",
    "El ambiente era tranquilo, pero algo pequeño.",
    "La comida estaba bien, aunque un poco grasosa.",
    "El proceso fue normal, pero algo tedioso.",
    "La atención fue razonable, pero no excelente.",
    "La experiencia fue aceptable, aunque no perfecta.",
    "El servicio fue suficiente, pero no memorable.",
    "El producto funciona, aunque no destaca.",
    "La atención fue adecuada, pero un poco lenta.",
    "La experiencia fue correcta, aunque esperaba más.",
    "El resultado fue bueno, pero no excelente.",
    "El ambiente era agradable, pero algo frío.",
    "La comida estaba bien, aunque un poco simple.",
    "El proceso fue sencillo, pero algo largo.",
    "La atención fue amable, pero poco eficiente.",
    "La experiencia fue positiva, aunque no perfecta."
]

# ============================================================
# 2. COMBINAR TODO EL DATASET
# ============================================================

data = []

for frase in frases_positivas:
    data.append((frase, "positivo"))

for frase in frases_negativas:
    data.append((frase, "negativo"))

for frase in frases_neutras:
    data.append((frase, "neutro"))

for frase in frases_sarcasticas:
    data.append((frase, "sarcasmo"))

for frase in frases_ambiguas:
    data.append((frase, "ambiguo"))

# Mezclar aleatoriamente
random.shuffle(data)

df = pd.DataFrame(data, columns=["texto", "sentimiento"])

# ============================================================
# 3. ENTRENAMIENTO DEL MODELO
# ============================================================

@st.cache_resource
def entrenar_modelo():
    X = df["texto"]
    y = df["sentimiento"]

    modelo = Pipeline([
        ("tfidf", TfidfVectorizer()),
        ("clf", LogisticRegression(max_iter=2000))
    ])

    modelo.fit(X, y)

    # Métricas sobre el dataset ampliado
    y_pred = modelo.predict(X)
    reporte = classification_report(y, y_pred, zero_division=0)
    matriz = confusion_matrix(y, y_pred, labels=["positivo", "negativo", "neutro", "sarcasmo", "ambiguo"])

    return modelo, reporte, matriz


modelo, reporte, matriz = entrenar_modelo()
# ============================================================
# 4. INTERFAZ STREAMLIT
# ============================================================

st.set_page_config(
    page_title="Día 12 — NLP Pipeline Inteligente",
    layout="wide"
)

st.title("🧠 Día 12 — Analizador de Sentimientos con Preprocesamiento Inteligente")
st.write("Clasificación de sentimiento con detección de idioma y normalización avanzada del texto.")
st.markdown("---")


st.subheader("Dataset de entrenamiento (resumen)")
st.write(df.head(20))

st.subheader("Métricas del modelo")
st.text(reporte)

st.write("Matriz de confusión (orden: positivo, negativo, neutro, sarcasmo, ambiguo)")
st.dataframe(
    pd.DataFrame(
        matriz,
        index=["Real positivo", "Real negativo", "Real neutro", "Real sarcasmo", "Real ambiguo"],
        columns=["Pred positivo", "Pred negativo", "Pred neutro", "Pred sarcasmo", "Pred ambiguo"]
    ),
    use_container_width=True
)

st.markdown("---")

st.subheader("Probar el modelo con tu propio texto")

texto_usuario = st.text_area(
    "Escribe un texto en español para analizar su sentimiento:",
    height=150,
    placeholder="Ejemplo: Me encantó la experiencia, volvería sin dudarlo."
)

if st.button("🔍 Analizar sentimiento", type="primary"):
    if not texto_usuario.strip():
        st.error("Por favor, escribe un texto antes de analizar.")
    else:
        idioma = detectar_idioma(texto_usuario)

        st.write(f"**Idioma detectado:** {idioma}")

        if idioma != "es":
            st.warning("El texto no parece estar en español. El modelo podría fallar.")
        
        texto_normalizado = normalizar_texto(texto_usuario)

        st.subheader("Texto normalizado")
        st.code(texto_normalizado)

        pred = modelo.predict([texto_normalizado])[0]
        proba = modelo.predict_proba([texto_normalizado])[0]
        etiquetas = modelo.classes_

        st.success(f"Sentimiento detectado: **{pred.upper()}**")

        st.subheader("Probabilidades por clase")
        st.table({
            "Sentimiento": etiquetas,
            "Probabilidad": [round(p, 4) for p in proba]
        })