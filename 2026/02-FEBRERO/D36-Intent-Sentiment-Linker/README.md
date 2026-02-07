### 🤖 Proyecto Día 36: Intent & Sentiment Linker 🧠🎭

En este hito, el orquestador bidireccional evoluciona hacia un sistema con **Conciencia Emocional**. Ya no es solo un receptor de comandos, sino que actúa como un **Middleware de Seguridad Crítica** (Safety Gatekeeper). El sistema analiza el tono del usuario y aplica un "cortocircuito" lógico: si detecta agresividad o lenguaje no profesional, bloquea cualquier ejecución de procesos de negocio (como reportes o backups).

#### **Hitos Técnicos Alcanzados:**
1.  **Middleware de Seguridad (Early Return Pattern):** Implementación de una arquitectura de validación prioritaria. Si el análisis de sentimiento resulta negativo, el sistema interrumpe la ejecución inmediatamente, impidiendo que comandos válidos (como "excel") sean procesados bajo un contexto de agresión.
2.  **Motor de Sentimientos con Normalización Unicode:** Integración de la librería `unicodedata` para normalizar el texto (eliminación de tildes, diéresis y limpieza de caracteres especiales). Esto permite que el sistema identifique insultos y palabras clave independientemente de variaciones ortográficas o de teclado.
3.  **Refuerzo de Diccionario de Toxicidad (Blacklist):** Ampliación del dataset de términos prohibidos y de presión negativa basado en pruebas de estrés en tiempo real, mejorando la precisión del modelo del Día 11 aplicado a la interacción directa.
4.  **Trazabilidad y Auditoría de Interacción:** Configuración de `logging` avanzado para registrar no solo la acción ejecutada, sino el diagnóstico emocional previo realizado por el sistema, fundamental para el monitoreo de IA en entornos corporativos.

#### **Tecnologías Utilizadas:**
* **NLP (Natural Language Processing):** Pipeline de normalización, tokenización y clasificación de sentimientos.
* **Pandas:** Gestión de la persistencia de datos para reportes validados por seguridad.
* **Unicodedata:** Motor de normalización de texto para robustez lingüística.
* **Pathlib:** Gestión de rutas dinámicas para asegurar que los entregables se mantengan en el contexto del proyecto.

#### **Flujo de Decisión del Sistema:**
1.  **Entrada:** Recepción de mensaje del usuario.
2.  **Capa 1 (Sentiment Check):** ¿El tono es profesional? 
    * **NO:** Bloqueo de seguridad y mensaje de advertencia.
    * **SÍ:** Pasa a la Capa 2.
3.  **Capa 2 (Intent Mapping):** Identificación de la acción (Reporte, Backup, Ayuda).
4.  **Ejecución:** Generación de archivo físico o tarea de sistema.