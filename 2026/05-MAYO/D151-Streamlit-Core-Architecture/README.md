# D151 - Streamlit Core Architecture

Este hito implementa una **aplicación web interactiva base utilizando Streamlit**, enfocada en la gestión robusta de estado de sesión (*State Management*) y diseño responsivo.

## Características Principales
- **Gestión Desacoplada de Estado:** La lógica de negocio está separada de la interfaz gráfica mediante `StreamlitCoreManager`, facilitando la realización de pruebas unitarias.
- **Persistencia de Sesión:** Manejo de variables reactivas (`st.session_state`) para mantener el contexto del usuario entre interacciones.
- **Diseño Responsivo:** Uso de contenedores en columnas (`st.columns`) y barra lateral configurada para múltiples dispositivos.

## 💡 ¿Para qué se usa y Casos de Uso Prácticos?
Streamlit es el estándar de la industria en Python para prototipar y desplegar aplicaciones de analítica y paneles de control interactivos en cuestión de minutos.

### Ejemplos de Uso:
1. **Paneles de Control para Machine Learning (Dashboards):**
   * *Caso:* Permitir a los usuarios ajustar hiperparámetros en tiempo real y visualizar predicciones de modelos al instante.
2. **Herramientas Internas de Operaciones:**
   * *Caso:* Crear interfaces ligeras para procesamiento de datos o reportes ejecutivos sin requerir frameworks complejos de Frontend (React/Vue).

## 📂 Estructura del Proyecto
```text
D151-Streamlit-Core-Architecture/
│
├── src/
│   ├── __init__.py
│   └── app_core.py
├── tests/
│   ├── __init__.py
│   └── test_app_core.py
├── app.py
├── requirements.txt
└── README.md