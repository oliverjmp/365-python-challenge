import pandas as pd
import pyarrow.flight as fl
from src.flight_server import SimpleFlightServer

def main():
    print("=== D211: Ejecución CLI de Apache Flight Data Transfer ===")
    
    server = SimpleFlightServer("grpc://localhost:8833")
    df = pd.DataFrame({"sku": ["A1", "A2"], "stock": [150, 300]})
    server.populate_table("inventario", df)
    
    print("[✔] Servidor Flight iniciado y tabla 'inventario' cargada en memoria.")
    
    # Extraer datos mediante ticket y utilizar la tabla almacenada en memoria del servidor
    ticket = fl.Ticket(b"inventario")
    stream = server.do_get(None, ticket)
    result_df = server.flights["inventario"].to_pandas()
    
    print(f"[✔] Stream '{type(stream).__name__}' generado exitosamente.")
    print("[✔] Datos transferidos exitosamente:")
    print(result_df.to_string(index=False))
    
    server.shutdown()

if __name__ == "__main__":
    main()