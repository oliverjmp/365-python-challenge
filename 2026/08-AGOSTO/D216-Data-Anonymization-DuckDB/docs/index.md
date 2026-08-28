# Portal Técnico: D216 - Data Anonymization with DuckDB

## 🏢 Resumen Ejecutivo
El hito **D216** implementa un pipeline analítico robusto para la anonimización y enmascaramiento de Datos de Identificación Personal (PII - *Personally Identifiable Information*) directamente en el motor relacional y analítico de alto rendimiento **DuckDB**, garantizando el cumplimiento de normativas de privacidad (como GDPR).

---

## 🎯 Objetivos Clave
* **Seguridad de Datos:** Enmascaramiento de tarjetas bancarias y truncado seguro de nombres.
* **Anonimización Criptográfica:** Uso de funciones hash (`SHA256`) para correos electrónicos, permitiendo trazabilidad analítica sin exponer datos reales.
* **Alto Rendimiento:** Procesamiento in-memory ultrarrápido impulsado por el motor SQL columnar de DuckDB.