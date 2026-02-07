### 🤖 Proyecto Día 37: Stateful Resilient Shield & User Warnings 🛡️🛑

En este hito, evolucionamos la seguridad del orquestador introduciendo **Gestión de Estado (State Management)**. El sistema ya no solo analiza el sentimiento de forma aislada, sino que mantiene un historial de comportamiento del usuario durante la sesión. Si se alcanza un umbral de faltas de respeto, el sistema activa un protocolo de bloqueo temporal.

#### **Hitos Técnicos Alcanzados:**
1.  **Gestión de Estado Persistente (Session State):** Implementación de un contador de advertencias interno para rastrear la conducta del usuario sin necesidad de una base de datos externa, optimizando el uso de memoria.
2.  **Protocolo de Bloqueo Temporal (Soft Ban):** Uso del módulo `time` para suspender la capacidad de respuesta del sistema tras detectar reincidencia en comportamientos no profesionales (3 strikes rule).
3.  **Lógica de Reincidencia Exponencial:** Diseño de un flujo donde cada falta de respeto incrementa la severidad de la respuesta, mejorando la autoridad del sistema automatizado.
4.  **Refactorización a Clase Singleton-Pattern:** Estructuración del código para asegurar que el estado del usuario sea consistente en toda la ejecución del programa.

#### **Tecnologías Utilizadas:**
* **Python 3.13:** Lógica avanzada de control de flujo y manejo de estados.
* **Time Module:** Control de latencia y bloqueos temporales del hilo de ejecución.
* **Logging:** Registro de incidentes de seguridad y bloqueos de usuario.
* **NLP Normalization:** Reutilización del motor de limpieza del Día 36 para consistencia.