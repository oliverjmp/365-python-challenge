# D162 - Estrategias de Caché en Streamlit

Optimización de rendimiento y gestión de estado mediante el almacenamiento en caché en memoria (`@st.cache_data`) para consultas pesadas de bases de datos y transformaciones de datos en interfaces analíticas.

## Características Principales
- **Optimización de Rendimiento:** Uso del decorador `@st.cache_data` para almacenar en memoria los resultados de consultas pesadas y evitar llamadas repetitivas e innecesarias.
- **Expiración Temporal Controlada (`ttl`):** Configuración de tiempos de vida para asegurar la actualización automática de los datos en caché de forma periódica.
- **Gestión Interactiva:** Mecanismos de invalidación y limpieza manual de la caché directamente desde el panel de control lateral.

## Ejemplos de Uso Real
- **Consultas a Bases de Datos:** Almacenamiento de DataFrames obtenidos mediante consultas pesadas de SQLAlchemy o SQL plano para mejorar la fluidez de la interfaz.
- **Procesamiento de Grandes Volúmenes:** Caché aplicada a funciones de agregación, filtrado y limpieza de datos masivos en Pandas.
- **Llamadas a APIs Externas:** Protección contra límites de peticiones (*rate limits*) almacenando temporalmente respuestas JSON de servicios remotos.

## 📂 Estructura del Proyecto
```text
D162-Caching-Strategies-Streamlit/
├── src/
│   ├── __init__.py
│   └── data_loader.py
├── tests/
│   ├── __init__.py
│   └── test_cache.py
├── app_cached.py
├── requirements.txt
└── README.md