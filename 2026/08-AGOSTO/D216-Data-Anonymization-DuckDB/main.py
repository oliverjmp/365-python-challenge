import pandas as pd
from src.anonymizer import DuckDBAnonymizer

def main():
    print("=== D216: Pipeline de Anonimización de PII con DuckDB ===")
    
    # Datos de ejemplo simulados con información sensible (PII)
    df_raw = pd.DataFrame({
        "id": [101, 102, 103],
        "nombre": ["Lucia Mendez", "Roberto Sanchez", "Elena Torres"],
        "tarjeta_credito": ["4532-1111-2222-3333", "5412-7777-8888-9999", "3782-4444-5555-6666"],
        "email": ["lucia.mendez@test.com", "roberto.s@corp.org", "elena.torres@mail.net"],
        "pais": ["España", "Argentina", "Colombia"],
        "monto": [1200.00, 450.50, 890.25]
    })
    
    print("\n--- Datos Originales (Con PII) ---")
    print(df_raw[["nombre", "tarjeta_credito", "email"]])
    
    # Ejecutar pipeline en DuckDB
    anonymizer = DuckDBAnonymizer()
    anonymizer.load_dataframe_as_table(df_raw, "source_table")
    df_anon = anonymizer.anonymize_pii("source_table")
    anonymizer.close()
    
    print("\n--- Datos Anonimizados y Enmascarados (SQL Pipeline) ---")
    print(df_anon[["nombre_anonimo", "tarjeta_anonima", "email_hash"]])
    
    print("\n[✔] Pipeline de enmascaramiento ejecutado exitosamente.")

if __name__ == "__main__":
    main()