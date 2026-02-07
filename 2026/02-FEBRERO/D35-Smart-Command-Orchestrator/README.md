### 🤖 Proyecto Día 35: Smart Command Orchestrator 🚀

En este hito, el proyecto evoluciona de scripts aislados a un sistema centralizado de toma de decisiones. Hemos implementado un **Orquestador de Comandos** que actúa como el "cerebro" del sistema, permitiendo una interacción bidireccional mediante el mapeo de intenciones (Intents) y conectando los logros de automatización de la Fase 1.

#### **Hitos Técnicos Alcanzados:**
1.  **Arquitectura de Despacho Dinámico:** Implementación de un `CommandDispatcher` basado en diccionarios ($O(1)$), lo que permite un acoplamiento débil entre la entrada del usuario y la ejecución de funciones específicas.
2.  **Normalización NLP Inicial:** Desarrollo de una capa de limpieza de texto (tokenización y normalización) para identificar palabras clave de intención, superando la rigidez de los comandos exactos.
3.  **Gestión Robusta de Rutas (Pathlib):** Configuración de un sistema de localización de archivos mediante `pathlib`, garantizando que todos los entregables (Excel) se generen exclusivamente dentro de la subcarpeta del proyecto, evitando conflictos en entornos compartidos como OneDrive.
4.  **Integración Transversal de Módulos:** Capacidad de invocar de forma segura procesos previos, como la generación de reportes (Días 3-4) y el sistema de backup (Día 15), desde una interfaz de usuario unificada.

#### **Tecnologías Utilizadas:**
* **Python 3.13:** Núcleo del sistema con implementación de Tipado Estático (Type Hinting) para mayor mantenibilidad.
* **Pandas:** Motor de persistencia para la creación de reportes profesionales en formato Excel.
* **Pathlib:** Estándar senior para la manipulación de rutas del sistema de archivos de forma absoluta.
* **Logging:** Sistema de trazabilidad para la auditoría de detecciones de intención y ejecución de procesos en tiempo real.