# Día 68: Data Anonymization Masking (Pandas + RegEx)

## Descripción General
Este módulo implementa un pipeline de ingeniería de datos enfocado en la **privacidad y gobernanza**, utilizando Pandas y expresiones regulares (`RegEx`) para detectar y enmascarar de forma automática Información de Identificación Personal (PII) en flujos tabulares corporativos.

## Características Principales
- **Detección por Patrones RegEx:** Identificación precisa de estructuras de correo electrónico, números telefónicos internacionales/locales, tarjetas de crédito (13-16 dígitos) y documentos de identidad españoles (DNI/NIE).
- **Enmascaramiento Parcial Seguro:** Preservación de metadatos contextuales mínimos (como el dominio del correo o los últimos 4 dígitos de tarjetas y teléfonos) para analítica sin vulnerar la privacidad.
- **Trazabilidad Empresarial:** Registro de eventos estructurado mediante el módulo nativo `logging`.
- **Validación con Faker:** Generación sintética automatizada de datos localizados (`es_ES`) para pruebas de integración y simulación de entornos reales.

## Instrucciones de Ejecución
Ejecuta el script principal con el siguiente comando en tu terminal:
```powershell
python anonymizer.py