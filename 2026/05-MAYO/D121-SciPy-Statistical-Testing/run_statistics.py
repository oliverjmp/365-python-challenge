import logging
from src.statistics_engine import BusinessStatisticalEngine

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("=== Iniciando Motor de Pruebas Estadísticas para Negocios (D121) ===")
    
    engine = BusinessStatisticalEngine(alpha=0.05)
    
    # 1. Simulación ANOVA: Rendimiento de ventas en 3 regiones distintas (Campañas)
    logging.info("Ejecutando análisis ANOVA para rendimiento de campañas...")
    campaign_a = [120, 135, 125, 130, 128]
    campaign_b = [140, 145, 150, 142, 148]
    campaign_c = [115, 110, 122, 118, 120]
    
    anova_res = engine.perform_anova([campaign_a, campaign_b, campaign_c])
    logging.info(f"Resultados ANOVA: F-Stat={anova_res['statistic']:.4f}, p-value={anova_res['p_value']:.4e}")
    logging.info(f"Interpretación: {anova_res['interpretation']}")
    
    # 2. Simulación Chi-Cuadrado: Preferencia de método de pago por segmento de cliente
    logging.info("\nEjecutando prueba Chi-cuadrado de independencia...")
    # Filas: Segmentos (Nuevo, Frecuente), Columnas: Métodos (Tarjeta, Efectivo, Crypto)
    contingency_data = [
        [45, 25, 30],
        [15, 50, 35]
    ]
    
    chi_res = engine.perform_chi_square(contingency_data)
    logging.info(f"Resultados Chi-Square: Chi2={chi_res['statistic']:.4f}, p-value={chi_res['p_value']:.4e}")
    logging.info(f"Interpretación: {chi_res['interpretation']}")
    
    logging.info("=== Hito D121 Ejecutado Exitosamente ===")

if __name__ == "__main__":
    main()