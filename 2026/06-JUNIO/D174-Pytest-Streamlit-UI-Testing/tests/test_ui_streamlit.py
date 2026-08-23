from playwright.sync_api import Page, expect
import time

def test_streamlit_bi_dashboard(page: Page):
    # Asumiendo que Streamlit corre localmente en el puerto 8501
    page.goto("http://localhost:8501")

    # Validar que el título principal de la app aparezca correctamente
    expect(page.get_by_text("Panel de Business Intelligence con PostgreSQL")).to_be_visible()

    # Hacer clic en el botón de consultar base de datos
    consult_button = page.get_by_role("button", name="Consultar Base de Datos")
    expect(consult_button).to_be_visible()
    consult_button.click()

    # Validar que aparezca el mensaje de éxito o los datos en la tabla
    expect(page.get_by_text("¡Datos obtenidos con éxito!")).to_be_visible(timeout=10000)