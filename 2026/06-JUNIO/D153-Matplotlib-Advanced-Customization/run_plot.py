import logging
import numpy as np
import matplotlib.pyplot as plt
from src.plots import CorporateDashboardPlotter

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("=== Iniciando Demostración Matplotlib OOP API (D153) ===")

    # Datos analíticos de prueba simulados
    x_vals = np.array(["Sem 1", "Sem 2", "Sem 3", "Sem 4", "Sem 5"])
    volume_data = np.array([1200, 1850, 1600, 2200, 2600])
    efficiency_data = np.array([65.5, 78.0, 72.5, 88.0, 94.2])

    # Instanciar el generador corporativo con paleta de colores personalizada
    plotter = CorporateDashboardPlotter(primary_color="#2E4057", secondary_color="#048A81")

    logging.info("Generando gráfico analítico estilizado con doble eje...")
    fig = plotter.create_dual_axis_analytics_chart(x_vals, volume_data, efficiency_data)

    output_path = "dashboard_corporativo_d153.png"
    fig.savefig(output_path, dpi=300, bbox_inches='tight')
    logging.info(f"Gráfico guardado exitosamente en disco como: {output_path}")

    # Mostrar de forma interactiva si se ejecuta en un entorno con soporte GUI
    # plt.show()
    
    logging.info("=== Hito D153 Ejecutado Exitosamente ===")

if __name__ == "__main__":
    main()