# 🤖 Proyecto Día 40: Integrated Security Alerting & Persistence System 🚨🛡️

¡Hito alcanzado! El Día 40 marca la culminación de la **Fase de Orquestación y Seguridad**. En este proyecto, el sistema "Manolo" ha evolucionado de un simple script a un **Orquestador Resiliente** capaz de autogestionar su seguridad, persistir estados de usuario y escalar incidentes críticos.

## 🎯 Objetivo
Implementar un sistema de alertas de nivel industrial que bloquee usuarios reincidentes, guarde el historial de forma persistente en JSON y genere registros de auditoría forense (`.log`).

---

## 🛠️ Hitos Técnicos Alcanzados

1. **Jerarquía de Capas de Control:**
   - **Capa 0 (Estado):** Verificación inmediata de bloqueo persistente.
   - **Capa 1 (Seguridad):** Análisis de sentimiento y detección de toxicidad antes de procesar cualquier comando.
   - **Capa 2 (UX/Ayuda):** Módulo de autodescubrimiento para guiar al usuario en las capacidades del bot.
   - **Capa 3 (Acción):** Ejecución de lógica de negocio (Reportes/Auditoría).

2. **Persistencia de Datos Robusta:**
   - Sincronización en tiempo real con `security_logs.json`.
   - El estado de "Bloqueado" sobrevive al reinicio del programa o del sistema.

3. **Escalación de Incidentes Críticos:**
   - Uso de `logging.CRITICAL` para marcar brechas de seguridad.
   - Generación automática de un `security_alerts.log` para revisión de administradores.

4. **Normalización NLP Avanzada:**
   - Limpieza de Unicode (NFD) para evitar que el usuario se salte los filtros usando tildes o caracteres especiales.

---

## 📊 Arquitectura del Sistema



## 📋 Tabla de Seguimiento (Cierre Fase 2)

| Día | Hito | Descripción | Estado |
| :---: | :--- | :--- | :---: |
| 36 | 🎭 Sentiment Gatekeeper | Detección de lenguaje inapropiado inicial. | ✅ |
| 37 | 🛡️ Stateful Shield | Gestión de advertencias (warnings) en memoria. | ✅ |
| 38 | 🗄️ Persistent DB | Migración del estado de memoria a archivo JSON. | ✅ |
| 39 | 📊 Audit Reporting | Cruce de datos entre historial de conducta y Excel. | ✅ |
| 40 | 🚨 Security Alerts | **Sistema de bloqueo total y alertas críticas.** | ✅ |

---

## 🚀 Cómo probar el sistema
1. Ejecuta `python D40.py`.
2. Escribe `ayuda` para ver qué puede hacer Manolo.
3. Intenta forzar el sistema con insultos: al llegar al 3º, el sistema se cerrará y quedará **bloqueado permanentemente** en el archivo JSON.
4. Intenta reiniciar el script; Manolo recordará que estás bloqueado y no te permitirá el acceso.

---
**Próximo Paso:** Fase 3 - Automatización Masiva de Archivos (OS Module Deep Dive).