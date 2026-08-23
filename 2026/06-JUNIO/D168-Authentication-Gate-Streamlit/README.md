# D168 - Authentication Gate con Streamlit

Capa robusta de seguridad y control de acceso basado en roles (RBAC) para proteger tableros analíticos corporativos y aplicaciones web de Streamlit.

## Características Principales
- **Autenticación Segura:** Validación de credenciales mediante hashes y tokens JWT gestionados por cookies.
- **Control de Acceso por Roles (RBAC):** Segmentación de vistas y funcionalidades según permisos de usuario (*admin*, *viewer*, etc.).
- **Gestión de Configuración Externa:** Cifrado y lectura estructurada mediante ficheros YAML seguros.

## 📂 Estructura del Proyecto
```text
D168-Authentication-Gate-Streamlit/
├── src/
│   ├── __init__.py
│   └── auth_manager.py
├── tests/
│   ├── __init__.py
│   └── test_auth.py
├── config.yaml
├── app_auth.py
├── requirements.txt
└── README.md