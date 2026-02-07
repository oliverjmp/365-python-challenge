### 🤖 Proyecto Día 36: Intent & Sentiment Linker 🧠🎭

En este hito, evolucionamos el orquestador bidireccional dotándolo de inteligencia emocional. El sistema ya no solo entiende "qué" se le pide, sino que evalúa el "cómo", actuando como un **Middleware de Seguridad** que filtra peticiones agresivas antes de ejecutar procesos críticos de negocio.

#### **Hitos Técnicos Alcanzados:**
1.  **Middleware de Sentimientos (NLP):** Implementación de una capa de análisis previo para clasificar el input del usuario en categorías de tono (Positivo vs. Negativo).
2.  **Normalización de Caracteres Especiales:** Integración de limpieza de tildes y normalización de minúsculas para robustecer la detección frente a variaciones ortográficas.
3.  **Lógica de Bloqueo Condicional:** Diseño de un cortafuegos lógico que impide la generación de reportes si se detecta un lenguaje no profesional.
4.  **Trazabilidad Detallada:** Uso de `Logging` para monitorear el proceso de decisión: Entrada -> Tokenización -> Sentimiento -> Acción.

#### **Tecnologías Utilizadas:**
* **NLP (Natural Language Processing):** Lógica de clasificación y tokenización de texto.
* **Pandas:** Motor de persistencia para la creación de reportes validados.
* **Pathlib:** Gestión avanzada de rutas dinámicas dentro del repositorio.