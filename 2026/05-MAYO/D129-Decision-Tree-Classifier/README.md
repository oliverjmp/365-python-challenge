# D129 - Decision Tree Classifier

Este hito implementa un **motor robusto de clasificación basado en Árboles de Decisión** utilizando `Scikit-learn`, optimizando criterios de división (como Gini o Entropía/Ganancia de Información) y controlando la profundidad para evitar el sobreajuste (*overfitting*).

## Características Principales
- **Optimización de Ganancia de Información:** Soporta criterios avanzados de particionamiento como Entropía y GindICE.
- **Control de Profundidad (`max_depth`):** Regula la complejidad del árbol para garantizar modelos generalizables y eficientes.
- **Exportación de Estructura (Graphviz):** Permite extraer la representación gráfica en formato DOT para auditar visualmente las reglas de decisión lógicas.

## 💡 ¿Para qué se usa y Casos de Uso Prácticos?
Los árboles de decisión son modelos sumamente intuitivos porque replican la lógica humana de toma de decisiones mediante reglas condicionales claras.

### Ejemplos de Uso:
1. **Diagnóstico Médico y Triage:**
   * *Caso:* Clasificar la urgencia de un paciente basándose en constantes vitales y síntomas secuenciales.
2. **Segmentación de Clientes y Churn (Fuga):**
   * *Caso:* Identificar los factores críticos (antigüedad, consumo) que determinan si un cliente abandonará un servicio.

## 📂 Estructura del Proyecto
```text
D129-Decision-Tree-Classifier/
│
├── src/
│   ├── __init__.py
│   └── tree_engine.py
├── tests/
│   └── test_tree.py
├── run_tree.py
├── requirements.txt
└── README.md