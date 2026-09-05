# D236 - LLM RAG Vector Search (FAISS)

Motor de búsqueda semántica de ultra baja latencia basado en **FAISS (Facebook AI Similarity Search)**. Diseñado para indexar y recuperar documentos corporativos no estructurados en espacios multidimensionales, sirviendo como la capa base de recuperación (*Retrieval*) para arquitecturas RAG (*Retrieval-Augmented Generation*).

## 🏛️ Arquitectura Implementada

1. **Indexación Vectorial Exacta (`IndexFlatL2`):** Implementación de búsqueda K-Nearest Neighbors (KNN) basada en distancia euclidiana L2 sobre memoria RAM, garantizando latencias de submilisegundos en la recuperación masiva del corpus de documentos.
2. **Capa de Abstracción de Embeddings:** Interfaz modular (`_generate_embeddings`) preparada para integrarse con modelos de lenguaje grandes (LLMs) de OpenAI o HuggingFace. Utiliza una proyección matemática determinista in-memory para aislar el entorno de pruebas CI/CD sin descargas pesadas.
3. **Mapeo de Metadatos en Memoria:** Asociación estructural directa entre los vectores de alta dimensionalidad (computados en C++ por el backend de FAISS) y los diccionarios de contexto original en Python.

## 💼 Casos Prácticos de Uso Empresarial

1. **Sistemas RAG para Bases de Conocimiento:**
   - Actúa como el motor de recuperación (*Retriever*) central. Cuando un usuario consulta un manual o política, FAISS localiza los fragmentos exactos para inyectarlos como contexto al LLM, permitiendo respuestas precisas basadas en datos internos.
2. **Auditoría Semántica de Contratos y Compras:**
   - Permite escanear repositorios históricos buscando órdenes de compra o acuerdos legales que sean *semánticamente similares* a un documento nuevo, detectando riesgos, sobreprecios o duplicados que los filtros clásicos (SQL/Regex) omitirían.
3. **Motores de Recomendación Documental en Tiempo Real:**
   - Sugiere instantáneamente a los analistas de datos archivos relacionados (ej. proyecciones financieras, análisis de usuarios) basándose en la proximidad vectorial matemática de la consulta actual.

## 📂 Estructura del Proyecto

```text
D236-LLM-RAG-VECTOR-SEARCH/
├── src/
│   ├── __init__.py
│   └── semantic_search.py # Motor analítico vectorial basado en FAISS
├── tests/
│   ├── __init__.py
│   └── test_search.py     # Suite de pruebas unitarias (100% Cobertura)
├── app_frontend.py        # Dashboard interactivo para evaluar distancias L2
├── requirements.txt       # Dependencias del entorno
└── README.md              # Documentación técnica y ejecutiva