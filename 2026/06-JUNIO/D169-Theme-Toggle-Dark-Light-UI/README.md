# D169 - Theme Toggle Dark/Light UI con Streamlit

Implementación de un sistema de gestión y conmutación de temas visuales (Modo Claro y Modo Oscuro) interactivo para aplicaciones analíticas en Streamlit.

## Características Principales
- **Conmutador de Tema (Toggle/Selectbox):** Permite al usuario alternar dinámicamente entre la paleta de colores clara y oscura.
- **Inyección de Estilos CSS Personalizados:** Aplicación de variables de diseño mediante estilos dinámicos adaptados al tema activo.
- **Persistencia de Estado:** Uso de `st.session_state` para recordar la preferencia visual del usuario durante su sesión.

## Estructura del Proyecto
```text
D169-Theme-Toggle-Dark-Light-UI/
├── src/
│   ├── __init__.py
│   └── theme_manager.py
├── tests/
│   ├── __init__.py
│   └── test_theme.py
├── app_theme.py
├── requirements.txt
└── README.md