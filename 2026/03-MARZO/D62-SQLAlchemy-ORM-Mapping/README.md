# Día 62 — SQLAlchemy ORM Mapping 🚀

## 📋 Descripción del Proyecto
El **Día 62** avanza en la **Fase 3** del reto (*SQL + Python*)[cite: 1], implementando un sistema de persistencia de datos relacional robusto con **SQLAlchemy ORM (v2.0)**. Este módulo traslada el diseño relacional tabular a objetos fuertemente tipados en Python, garantizando integridad referencial, transacciones seguras (`commit`/`rollback`) y manejo absoluto de rutas con `pathlib`.

---

## 🛠️ Tecnologías y Librerías Utilizadas
* **Python 3.x**[cite: 1] (Tipado estricto mediante anotaciones `Mapped`)
* **SQLAlchemy v2.0+** (Mapeo Objeto-Relacional y gestión de motores transaccionales)
* **SQLite** (Motor relacional integrado para persistencia local)

---

## 📂 Arquitectura de Archivos
```text
D62-SQLAlchemy-ORM-Mapping/
├── D62.py                   # Modelos ORM, motor y lógica transaccional
├── enterprise_database.db   # Base de datos SQLite generada automáticamente
└── README.md                # Documentación técnica del módulo