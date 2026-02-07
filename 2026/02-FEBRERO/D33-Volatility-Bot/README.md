### 🚀 Proyecto Día 33: Bot de Monitoreo de Volatilidad (Live) 🚨
En este segundo día de conectividad, el objetivo fue evolucionar del "Snapshot" (foto estática) al **Monitoreo Continuo**. El script analiza el flujo de datos en tiempo real para detectar variaciones porcentuales bruscas en el mercado.

#### **Hitos Técnicos Alcanzados:**
1.  **Manejo de Estados:** Implementación de lógica de memoria para comparar el `precio_actual` vs el `precio_anterior`.
2.  **Cálculo de Delta Porcentual:** Algoritmo para determinar la volatilidad en tiempo real: 
    $$\Delta\% = \left( \frac{V_{actual} - V_{anterior}}{V_{anterior}} \right) \times 100$$
3.  **Control de Flujo de Red:** Uso de `time.sleep()` para gestionar el **Rate Limiting** de servicios gratuitos.

#### **Lecciones del "Mundo Real" (Debugging):**
Durante la ejecución, se detectó un error de clave (`KeyError: 'bitcoin'`). 
* **Causa:** La API de CoinGecko activó un bloqueo temporal por exceso de peticiones (Rate Limit), devolviendo un JSON vacío o un mensaje de error.
* **Solución para el Día 34:** Implementar validación de códigos de estado HTTP (429 Too Many Requests) y verificación de existencia de llaves en diccionarios antes del acceso.

#### **Tecnologías Utilizadas:**
* **Requests:** Peticiones cíclicas al endpoint.
* **Time:** Gestión de pausas entre peticiones.
* **Math Logic:** Cálculo de variaciones de mercado.

---

### 📊 Ejemplo de Salida en Consola:
```text Bitcoin: $68,567.00 | Var: +0.0000% | ⚖️ Estable Bitcoin: $68,673.00 | Var: +0.1546% | 🔥 MOVIMIENTO DETECTADO