# D224 - Multiprocessing CPU-Bound

## 🏢 Resumen Ejecutivo y Alcance del Hito
El hito **D224** aborda la superación del cuello de botella histórico de Python: el **Bloqueo Global del Intérprete (GIL)**. Para tareas intensivas de procesamiento numérico y CPU (*CPU-Bound*), los hilos tradicionales (*threads*) no ofrecen paralelismo real. Mediante el uso del módulo **`multiprocessing`** y `ProcessPoolExecutor`, este núcleo despliega instancias de intérpretes independientes en múltiples núcleos del procesador físico, maximizando el rendimiento analítico.

---

## 📐 Pilares de Ingeniería
1. **Aislamiento de Memoria por Procesos:** Cada proceso hijo opera en su propio espacio de memoria, evitando condiciones de carrera (*race conditions*) asociadas al estado compartido.
2. **Paralelismo Real de Hardware:** Utilización simultánea de todos los cores disponibles en la CPU para cálculos pesados.
3. **Escalabilidad Dinámica:** Distribución automática de cargas de trabajo pesadas mediante colas de tareas administradas por `ProcessPoolExecutor`.