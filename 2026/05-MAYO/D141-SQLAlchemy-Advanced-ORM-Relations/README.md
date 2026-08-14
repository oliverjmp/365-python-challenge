# D141 - SQLAlchemy Advanced ORM Relations (Many-to-Many)

Este hito implementa el **modelado de relaciones complejas Many-to-Many utilizando tablas asociativas (junction tables)** en bases de datos relacionales mediante `SQLAlchemy ORM`.

## Características Principales
- **Tablas Asociativas Optimizadas:** Uso de objetos `Table` puros para conectar entidades relacionales de manera eficiente.
- **Relaciones Bidireccionales Automáticas:** Configuración simétrica mediante el parámetro `secondary` y `back_populates`.
- **Gestión de Ciclo de Vida ORM:** Soporte completo para asociaciones, desvinculaciones y consultas cruzadas complejas.

## 💡 ¿Para qué se usa y Casos de Uso Prácticos?
En arquitectura de software y diseño de bases de datos, las relaciones de muchos a muchos son indispensables cuando un registro en una tabla principal puede asociarse con múltiples registros de otra, y viceversa.

### Ejemplos de Uso:
1. **Plataformas Educativas (Estudiantes y Cursos):**
   * *Caso:* Un estudiante puede inscribirse en muchos cursos, y un curso puede tener muchos estudiantes.
2. **Gestión de Proyectos y Desarrolladores:**
   * *Caso:* Un desarrollador participa en multiples proyectos corporativos, y un proyecto cuenta con un equipo de múltiples desarrolladores.

## 📂 Estructura del Proyecto
```text
D141-SQLAlchemy-Advanced-ORM-Relations/
│
├── src/
│   ├── __init__.py
│   └── models.py
├── tests/
│   └── test_relations.py
├── run_relations.py
├── requirements.txt
└── README.md