# D234: Enterprise Procurement Text-to-SQL Engine (DuckDB + LangChain)

## 📌 Descripción del Caso de Negocio
Este sistema permite a Directores Financieros y Analistas de Procurement realizar consultas en lenguaje natural sobre datasets masivos de compras OpEx. La solución traduce preguntas complejas en español directamente a sentencias SQL ANSI ejecutables en milisegundos sobre un motor **DuckDB** in-memory.

## 🏗️ Arquitectura del Sistema
1. **User Question**: Pregunta ingresada mediante interfaz Streamlit o consola CLI.
2. **Schema Context Injection**: Generación dinámica del contexto DDL de DuckDB.
3. **LangChain LCEL Pipeline**: Orquestación con `ChatGoogleGenerativeAI` para generación de SQL determinista.
4. **OLAP Engine Execution**: Validación de seguridad y ejecución de alta velocidad en DuckDB (50.000 filas).
5. **Interactive Visualization**: Renderizado de tablas y gráficos dinámicos.

## 🛠️ Stack Tecnológico
- **Python 3.11+**
- **LangChain (LCEL)**
- **Google GenAI SDK (`google-genai` / `langchain-google-genai`)**
- **DuckDB (Motor OLAP)**
- **Streamlit & Pandas**
- **Pytest**

## 🚀 Instalación y Ejecución

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Configurar variable de entorno
echo "GEMINI_API_KEY=tu_api_key_aqui" > .env

# 3. Ejecutar pipeline de prueba por consola
python run_pipeline.py

# 4. Lanzar la aplicación interactiva
streamlit run app.py