# 🏗️ D175: Refactorización Estructural - Patrón MVC en BI Stack

## 📋 Descripción del Reto
Desafío orientado a la refactorización arquitectónica del código base de la aplicación de Business Intelligence, aplicando estrictamente el patrón de diseño **Modelo-Vista-Controlador (MVC)** para mejorar la mantenibilidad, escalabilidad y separación de responsabilidades del proyecto.

## 🏛️ Arquitectura MVC Implementada
* **Modelo (`models/`)**: Encargado de la persistencia de datos, configuración de SQLAlchemy y ejecución de consultas directas hacia PostgreSQL.
* **Controlador (`controllers/`)**: Gestiona la lógica de negocio, el procesamiento de los DataFrames de Pandas y la validación de resultados.
* **Vista (`app_bi.py`)**: Responsable de renderizar exclusivamente los componentes visuales e interactivos utilizando Streamlit.

## 🛠️ Tecnologías Utilizadas
* **Python 3.11+**
* **Streamlit** (Vista)
* **Pandas & SQLAlchemy** (Modelo y Controlador)
* **PostgreSQL** (Base de datos relacional)

## 📂 Estructura del Proyecto
```text
D175-Code-Refactoring-Modular-BI/
├── app_bi.py                 # Vista principal (Streamlit)
├── models/
│   └── database.py           # Conexión y consultas SQL (Modelo)
├── controllers/
│   └── kpi_controller.py     # Lógica de negocio (Controlador)
└── requirements.txt