import pytest
from src.statistics_engine import BusinessStatisticalEngine

@pytest.fixture
def stat_engine():
    return BusinessStatisticalEngine(alpha=0.05)

def test_perform_anova_significant(stat_engine):
    """Prueba ANOVA con muestras que presentan diferencias claras."""
    group_a = [10.5, 11.0, 10.8, 11.2, 10.9]
    group_b = [15.2, 14.8, 15.0, 15.5, 15.1]
    group_c = [20.1, 19.8, 20.5, 20.0, 20.3]
    
    result = stat_engine.perform_anova([group_a, group_b, group_c])
    
    assert result["test"] == "ANOVA"
    assert result["reject_null"] is True
    assert result["p_value"] < 0.05

def test_perform_chi_square_independent(stat_engine):
    """Prueba Chi-cuadrado con tabla de contingencia."""
    # Tabla de contingencia 2x2 simulada
    table = [
        [50, 10],
        [10, 50]
    ]
    
    result = stat_engine.perform_chi_square(table)
    
    assert result["test"] == "Chi-Square"
    assert result["degrees_of_freedom"] == 1
    assert "statistic" in result