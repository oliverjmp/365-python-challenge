# D156 - Streamlit MultiPage Router

Este hito implementa una **arquitectura modular de aplicación web multipágina orientada a diferentes perfiles de negocio** utilizando Streamlit y un sistema de enrutamiento centralizado.

## Características Principales
- **Enrutamiento Modular (`StreamlitRouter`):** Registro dinámico de vistas y control de acceso por perfiles de negocio (Administradores vs. Clientes).
- **Separación de Responsabilidades:** Vistas desacopladas en módulos independientes para facilitar el mantenimiento y escalabilidad.
- **Pruebas Unitarias Robustas:** Cobertura total de validaciones de rutas, excepciones y renderizado dinámico.

## Requisitos y Ejecución
1. Instalar dependencias: `pip install -r requirements.txt`
2. Ejecutar pruebas unitarias con cobertura: `$env:PYTHONPATH="."; python -m pytest --cov=src --cov-report=term-missing`
3. Ejecutar aplicación Streamlit: `streamlit run app.py`