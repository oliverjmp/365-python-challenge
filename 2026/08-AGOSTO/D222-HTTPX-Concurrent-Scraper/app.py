import asyncio
import streamlit as st
from src.scraper_core import HTTPXConcurrentScraper

st.set_page_config(
    page_title="D222 - HTTPX Concurrent Scraper Enterprise",
    page_icon="🌐",
    layout="wide"
)

st.title("🌐 D222: Panel de Ingesta Web Concurrente Masiva (HTTPX + Keep-Alive)")
st.markdown("""
Este panel ejecutivo demuestra la eficiencia de la ingesta web asíncrona de alta densidad 
mediante la reutilización agresiva de conexiones HTTP persistentes (**Keep-Alive** y **HTTP/2**).
""")

st.sidebar.header("Configuración de Ingesta")
default_urls = (
    "https://httpbin.org/status/200\n"
    "https://httpbin.org/json\n"
    "https://httpbin.org/uuid\n"
    "https://httpbin.org/headers\n"
    "https://httpbin.org/user-agent"
)
urls_input = st.sidebar.text_area("URLs a consultar (una por línea)", value=default_urls, height=150)

if st.button("🚀 Lanzar Scraping Concurrente", type="primary"):
    urls = [line.strip() for line in urls_input.split("\n") if line.strip()]
    
    if not urls:
        st.warning("Por favor introduce al menos una URL válida.")
    else:
        scraper = HTTPXConcurrentScraper()
        with st.spinner(f"Ingestando {len(urls)} fuentes en paralelo..."):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            summary = loop.run_until_complete(scraper.scrape_batch(urls))
            loop.close()

        col1, col2, col3 = st.columns(3)
        col1.metric("URLs Totales", summary["total_urls"])
        col2.metric("Peticiones Exitosas", summary["successful_requests"])
        col3.metric("Peticiones Fallidas", summary["failed_requests"])

        st.success("¡Ingesta completada satisfactoriamente mediante conexiones persistentes!")
        with st.expander("🔍 Ver resultados detallados por endpoint"):
            st.dataframe(summary["results"], use_container_width=True)
else:
    st.info("Configura los endpoints en el panel izquierdo y haz clic en **Lanzar Scraping Concurrente**.")