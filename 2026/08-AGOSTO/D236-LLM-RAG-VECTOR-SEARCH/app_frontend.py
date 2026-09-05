import streamlit as st
import plotly.express as px
from src.semantic_search import VectorSearchEngine

st.set_page_config(page_title="D236 - FAISS Semantic Search", layout="wide")

st.title("🧠 Motor de Búsqueda Semántica Vectorial (FAISS)")
st.markdown("Indexación y recuperación de documentos en espacios de alta dimensionalidad.")

@st.cache_resource
def load_engine():
    engine = VectorSearchEngine(embedding_dim=128)
    corpus = [
        {"categoria": "Finanzas", "text": "Proyección de ingresos y balances trimestrales."},
        {"categoria": "Data Science", "text": "Lectura y normalización desde el archivo Análisis de Datos corporativo."},
        {"categoria": "Legal", "text": "Contratos de confidencialidad y normativas GDPR."},
        {"categoria": "Operaciones", "text": "Logística de cadena de suministro y control de inventarios."}
    ]
    engine.build_index(corpus)
    return engine

engine = load_engine()

query = st.text_input("🔍 Ingrese su consulta de búsqueda:", value="Análisis de Datos")
top_k = st.slider("Resultados máximos (Top K)", 1, 4, 3)

if st.button("Buscar en Vector DB", type="primary"):
    with st.spinner("Calculando distancias euclidianas en C++..."):
        df_res = engine.search(query, top_k=top_k)
        
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Documentos Recuperados")
        st.dataframe(df_res[["categoria", "text", "distance_l2"]], use_container_width=True)
        
    with col2:
        fig = px.bar(
            df_res, 
            x="categoria", 
            y="distance_l2",
            color="distance_l2",
            color_continuous_scale="Reds",
            title="Distancia L2 (Menor es mayor similitud)"
        )
        st.plotly_chart(fig, use_container_width=True)