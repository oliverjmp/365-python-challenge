# D116 - Design Pattern Factory (Connectors)

Este hito implementa el **patrón de diseño Factoría (Factory Pattern) para la instanciación dinámica de conectores de datos** en arquitecturas orientadas a objetos desacopladas.

## Características Principales
- **Desacoplamiento de Código:** Oculta la lógica compleja de creación de objetos y permite instanciar clases basándose en cadenas de texto identificadoras.
- **Principio Open/Closed (SOLID):** Permite registrar nuevos conectores en tiempo de ejecución sin alterar el código existente mediante el método `register_connector`.
- **Interfaces Estrictas:** Uso de clases abstractas (`ABC`) para asegurar contratos de comportamiento idénticos en todos los conectores.

## 💡 ¿Para qué se usa y Casos de Uso Prácticos?
En sistemas que necesitan conectarse a múltiples bases de datos o servicios externos de manera dinámica según archivos de configuración o peticiones de usuario:

### Ejemplos de Uso:
1. **Sistemas Multi-Tenant o ETLs Dinámicos:**
   * *Caso:* Seleccionar y conectar automáticamente a PostgreSQL, MySQL o MongoDB dependiendo de la fuente de datos configurada para cada cliente sin llenar el código de condicionales `if/else`.
2. **Plugins y Extensiones de Frameworks:**
   * *Caso:* Cargar drivers o adaptadores de terceros de forma centralizada bajo demanda.

## 📂 Estructura del Proyecto
```text
D116-Design-Pattern-Factory/
│
├── src/
│   ├── __init__.py
│   └── connectors.py
├── tests/
│   └── test_connectors.py
├── run_factory.py
├── requirements.txt
└── README.md