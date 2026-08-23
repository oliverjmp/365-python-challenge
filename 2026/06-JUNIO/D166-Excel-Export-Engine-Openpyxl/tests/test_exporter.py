import pandas as pd
import io
from src.exporter import generate_styled_excel

def test_generate_styled_excel():
    df = pd.DataFrame({
        "ID": [1, 2],
        "Nombre_Largo_Prueba": ["Texto muy extenso que supera la longitud de la cabecera", "B"]
    })
    
    excel_buffer = generate_styled_excel(df)
    assert isinstance(excel_buffer, io.BytesIO)
    assert excel_buffer.getbuffer().nbytes > 0