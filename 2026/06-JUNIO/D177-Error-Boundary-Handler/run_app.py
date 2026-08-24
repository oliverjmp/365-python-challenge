import logging
from src.error_boundary import ErrorBoundary, ComponentRenderError

def main():
    logging.info("=== Iniciando Sistema de Prueba para Error Boundary (D177) ===")
    
    boundary = ErrorBoundary(fallback_message="La interfaz se ha recuperado con éxito de un fallo de renderizado.")
    
    # 1. Simulación de ejecución exitosa
    def widget_ok():
        return "Datos del gráfico renderizados correctamente."
    
    print("\n--- Ejecutando Widget Estable ---")
    res_ok = boundary.catch(widget_ok)
    print(f"Resultado: {res_ok}")
    
    # 2. Simulación de fallo catastrófico en la UI
    def widget_failed():
        raise ComponentRenderError("Error crítico de conexión al renderizar tabla de datos.")
    
    print("\n--- Ejecutando Widget con Fallo ---")
    res_fail = boundary.catch(widget_failed)
    print(f"Resultado: {res_fail}")
    print(f"¿Hubo error en el boundary?: {boundary.has_error}")
    
    logging.info("=== Hito D177 Ejecutado Exitosamente ===")

if __name__ == "__main__":
    main()