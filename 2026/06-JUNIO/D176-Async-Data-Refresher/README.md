# ⚡ D176: Sistema de Actualización Asíncrona de Datos (`asyncio` + Streamlit)

## 📋 Descripción del Reto
Desafío orientado a la implementación de un sistema de actualización de datos en segundo plano de forma no bloqueante utilizando **`asyncio`** integrado con **Streamlit**, garantizando una experiencia de usuario fluida y reactiva incluso al procesar tareas pesadas de consulta o red.

## 🏛️ Arquitectura del Proyecto (Patrón MVC)
* **Modelo (`models/database.py`)**: Gestiona la persistencia y la conexión relacional con PostgreSQL vía SQLAlchemy.
* **Controlador (`controllers/async_controller.py`)**: Envuelve la lógica de negocio ejecutando operaciones asíncronas concurrentes sin congelar el hilo principal.
* **Vista (`app_bi.py`)**: Interfaz gráfica en Streamlit con indicadores de carga amigables (`st.spinner`).

## 🛠️ Tecnologías Utilizadas
* **Python 3.11+**
* **Streamlit** (UI)
* **Asyncio** (Concurrencia y asincronía)
* **Pandas & SQLAlchemy** (Procesamiento y datos)
* **PostgreSQL** (Base de datos)

## 📂 Estructura del Proyecto
```text
D176-Async-Data-Refresher/
├── app_bi.py                 # Vista principal (Streamlit)
├── models/
│   ├── __init__.py
│   └── database.py           # Conexión base a PostgreSQL (Modelo)
├── controllers/
│   ├── __init__.py
│   └── async_controller.py   # Lógica asíncrona (Controlador)
└── requirements.txt