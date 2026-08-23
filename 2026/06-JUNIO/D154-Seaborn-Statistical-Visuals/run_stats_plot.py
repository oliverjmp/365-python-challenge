import logging
import matplotlib.pyplot as plt
from src.stats_plots import SeabornStatisticalPlotter

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("=== Iniciando Demostración Seaborn Statistical Visuals (D154) ===")

    plotter = SeabornStatisticalPlotter(random_state=42)
    
    logging.info("Generando dataset sintético con NumPy...")
    df = plotter.generate_synthetic_dataset(n_samples=500)

    logging.info("Generando Mapa de Calor de Correlación...")
    fig_heatmap = plotter.create_correlation_heatmap(df)
    heatmap_path = "correlation_heatmap_d154.png"
    fig_heatmap.savefig(heatmap_path, dpi=300, bbox_inches='tight')
    logging.info(f"Mapa de calor guardado en: {heatmap_path}")

    logging.info("Generando Distribución Bivariada (KDE)...")
    fig_bivariate = plotter.create_bivariate_distribution_plot(df, 'Variable_A', 'Variable_B')
    bivariate_path = "bivariate_kde_d154.png"
    fig_bivariate.savefig(bivariate_path, dpi=300, bbox_inches='tight')
    logging.info(f"Distribución bivariada guardada en: {bivariate_path}")

    logging.info("=== Hito D154 Ejecutado Exitosamente ===")

if __name__ == "__main__":
    main()