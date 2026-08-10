# Módulo D88: Singleton Pipeline Manager (`Design Patterns`)

## Descripción General
Este módulo implementa el **patrón de diseño creacional Singleton** en Python. Su propósito es restringir la creación de objetos de una clase a una sola instancia, garantizando un punto de acceso global y controlado a la conexión del Data Warehouse.

---

## Características Principales
* **Instancia Única**: Control estricto mediante el método `__new__` para reutilizar el canal de conexión existente.
* **Protección de Estado**: Uso de una bandera de inicialización (`_initialized`) para evitar sobrescribir configuraciones previas al reintentar instancias.
* **Pruebas de Identidad**: Verificación mediante `assert manager1 is manager2` para confirmar el comportamiento Singleton.

---

## Estructura del Proyecto
```text
D88-Singleton-Pipeline-Manager/
├── src/
│   ├── __init__.py
│   └── warehouse_manager.py # Implementación del patrón Singleton para el DW
├── tests/
│   ├── __init__.py
│   └── test_warehouse_manager.py # Pruebas unitarias de unicidad y consultas
├── requirements.txt # Dependencias del proyecto
└── README.md        # Documentación técnica del módulo