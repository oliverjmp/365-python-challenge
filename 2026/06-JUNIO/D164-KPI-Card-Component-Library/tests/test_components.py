from src.components import format_currency_metric, render_kpi_card

def test_format_currency_metric():
    result = format_currency_metric(1500.5)
    assert result == "$1,500.50"
    
    result_zero = format_currency_metric(0.0)
    assert result_zero == "$0.00"

def test_render_kpi_card():
    # Invocamos la función para cubrir las líneas de renderizado HTML y metadatos
    try:
        render_kpi_card("Total Ventas", "$45,000", delta="+10%", delta_color="normal")
        assert True
    except Exception as e:
        assert False, f"La función falló: {e}"