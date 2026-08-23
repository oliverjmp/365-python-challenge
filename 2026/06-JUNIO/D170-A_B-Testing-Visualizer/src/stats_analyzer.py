import scipy.stats as stats
import numpy as np

def calculate_ab_test(visitors_a: int, conversions_a: int, visitors_b: int, conversions_b: int) -> dict:
    """
    Realiza una prueba Z de dos proporciones utilizando SciPy para comparar los grupos A y B.
    """
    if visitors_a <= 0 or visitors_b <= 0:
        return {"p_value": 1.0, "significant": False, "lift": 0.0, "rate_a": 0.0, "rate_b": 0.0}

    rate_a = conversions_a / visitors_a
    rate_b = conversions_b / visitors_b
    
    # Cálculo del lift porcentual
    lift = ((rate_b - rate_a) / rate_a) * 100 if rate_a > 0 else 0.0

    # Cálculo manual robusto de la prueba Z de dos proporciones con SciPy
    p_pooled = (conversions_a + conversions_b) / (visitors_a + visitors_b)
    
    if p_pooled == 0 or p_pooled == 1:
        p_value = 1.0
    else:
        se = np.sqrt(p_pooled * (1 - p_pooled) * (1 / visitors_a + 1 / visitors_b))
        if se == 0:
            p_value = 1.0
        else:
            z_stat = (rate_b - rate_a) / se
            # Prueba bilateral (two-tailed z-test)
            p_value = float(2 * (1 - stats.norm.cdf(abs(z_stat))))

    return {
        "rate_a": rate_a,
        "rate_b": rate_b,
        "lift": lift,
        "p_value": p_value,
        "significant": bool(p_value < 0.05)
    }