# D200 - Mid-Year Architecture Milestone (Git Automation + Docs)

Consolidación y etiquetado automático del hito de mitad de año en la arquitectura del portafolio de ingeniería de datos, integrando automatización de repositorios con **GitPython** y documentación formal.

## 🏛️ Componentes del Sistema
1. **Automatizador Git (`src/git_automator.py`):** Control programático del repositorio para auditoría de ramas, commits y creación de tags de hitos corporativos.
2. **Dashboard Interactivo (`app.py`):** Interfaz en **Streamlit** para visualizar el estado del repositorio y etiquetar los hitos de forma visual.
3. **Documentación Formal:** Estructura completa con MkDocs y tema corporativo índigo.

## 🚀 Ejecución y Pruebas
- **Pruebas unitarias:** `python -m pytest --cov=src --cov-report=term-missing --cache-clear`
- **CLI:** `python main.py`
- **Dashboard:** `streamlit run app.py`
- **Documentación:** `mkdocs serve`