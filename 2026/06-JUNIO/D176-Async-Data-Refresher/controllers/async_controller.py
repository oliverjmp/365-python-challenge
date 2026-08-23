import asyncio
import pandas as pd
from models.database import fetch_data_from_db

async def fetch_data_async(query: str) -> pd.DataFrame:
    """
    Ejecuta la consulta de forma no bloqueante simulando tareas en segundo plano.
    """
    # Simulamos una tarea de red o procesamiento pesado asíncrono
    await asyncio.sleep(1.5)
    
    # Llamada a la base de datos (puedes adaptarlo según tu motor síncrono/asíncrono)
    df = fetch_data_from_db(query)
    return df

def run_async_query(query: str) -> tuple[pd.DataFrame, bool]:
    """
    Envuelve la ejecución asíncrona para que Streamlit pueda invocarla fácilmente.
    """
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
    df = loop.run_until_complete(fetch_data_async(query))
    if not df.empty:
        return df, True
    return pd.DataFrame(), False