# Arquitectura del Hito D200

## 🔄 Flujo de Automatización de Git
El sistema interactúa directamente con la API de Git a través de la librería `GitPython` para realizar las siguientes operaciones de forma segura:
1. **Inspección de Estado:** Lectura de ramas activas y hashes de confirmación recientes.
2. **Creación de Tags Anotados:** Marcado formal de versiones estables del portafolio.
3. **Manejo de Excepciones:** Validación de repositorios no válidos y prevención de etiquetas duplicadas.