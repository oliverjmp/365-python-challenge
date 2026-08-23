import logging
from src.interactive_plots import PlotlyInteractiveVisualizer

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("=== Iniciando Demostración Plotly Interactive Charts (D155) ===")

    visualizer = PlotlyInteractiveVisualizer(random_state=42)
    
    logging.info("Generando dataset sintético...")
    df = visualizer.generate_time_series_dataset(n_days=120)

    logging.info("Generando Gráfico de Dispersión Interactivo...")
    fig_scatter = visualizer.create_interactive_scatter(df)
    scatter_file = "interactive_scatter_d155.html"
    fig_scatter.write_html(scatter_file)
    logging.info(f"Gráfico de dispersión guardado en: {scatter_file}")

    logging.info("Generando Subplots Sincronizados...")
    fig_subplots = visualizer.create_synchronized_subplots(df)
    subplots_file = "synchronized_subplots_d155.html"
    fig_subplots.write_html(subplots_file)
    logging.info(f"Subplots sincronizados guardados en: {subplots_file}")

    logging.info("=== Hito D155 Ejecutado Exitosamente ===")

if __name__ == "__main__":
    main()