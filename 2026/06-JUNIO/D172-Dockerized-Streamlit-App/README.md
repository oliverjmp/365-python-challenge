# D172 - Dockerized Streamlit App

Contenedorización optimizada mediante un `Dockerfile` de múltiples etapas (`multi-stage`) para empaquetar de forma ligera, segura y eficiente la aplicación analítica basada en Streamlit.

## Características Principales
- **Multi-stage Build:** Separación de la fase de compilación e instalación de dependencias pesadas de la imagen final de ejecución para reducir drásticamente el tamaño del contenedor.
- **Optimización para Producción:** Configuración de variables de entorno específicas para ejecutar Streamlit en modo desatendido (`headless`).
- **Despliegue Estable:** Preparado para garantizar portabilidad y estabilidad en cualquier servicio de la nube.

## Estructura del Proyecto
```text
D172-Dockerized-Streamlit-App/
├── src/
│   ├── __init__.py
│   └── data_processor.py
├── tests/
│   ├── __init__.py
│   └── test_processor.py
├── app.py
├── requirements.txt
├── Dockerfile
└── README.md