# 🧪 D174: Pruebas End-to-End (E2E) con Playwright y Pytest

## 📋 Descripción del Reto
Este desafío forma parte del reto de 365 días de desarrollo profesional en Python. Consiste en la implementación de una suite automatizada de pruebas end-to-end (E2E) utilizando **Playwright** y **Pytest** para validar de manera robusta la interfaz de usuario (UI) y la interacción de componentes de la aplicación de Business Intelligence desarrollada en Streamlit.

## 🛠️ Tecnologías y Herramientas Utilizadas
* **Python 3.11 / 3.13**
* **Streamlit** (Interfaz de usuario)
* **Pytest** (Framework de pruebas)
* **Playwright** (Automatización de navegadores web)

## ⚙️ Estructura del Proyecto
```text
D174-Pytest-Streamlit-UI-Testing/
├── app_bi.py              # Aplicación principal de Streamlit
├── src/
│   └── db_connector.py    # Lógica de conexión a la base de datos
├── tests/
│   └── test_ui_streamlit.py # Suite de pruebas E2E con Playwright
└── requirements.txt