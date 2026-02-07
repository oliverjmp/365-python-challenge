"""
Proyecto: 365 Python Challenge
Día 54: Data Cleaning Mastery
Objetivo: Limpiar un dataset realista con errores, nulos y tipos incorrectos.
"""

import pandas as pd
import numpy as np

class DataCleaner:
    def __init__(self):
        # 1. Creamos un dataset "Socio" para practicar (Simulando un CSV mal formado)
        raw_data = {
            'ID': [101, 102, 103, 103, 105, 106, 107], # El 103 está duplicado
            'Producto': ['Laptop', 'Mouse', 'Monitor', 'Monitor', 'Teclado', None, 'Cámara'],
            'Precio': ['$1,200.00', '$25.00', '$300.00', '$300.00', 'Gratis', '$150.00', '$2,000.00'],
            'Stock': [15, 120, np.nan, np.nan, 50, 8, -5], # Nulos y negativos
            'Fecha_Venta': ['2026-02-01', '2026-02-02', '03/02/2026', '03/02/2026', '2026-02-05', '06-02-26', '2026-02-07']
        }
        self.df = pd.DataFrame(raw_data)

    def clean_process(self):
        print("📁 Dataset Original (Sucio):")
        print(self.df)

        # --- PASO 1: Eliminar Duplicados ---
        self.df = self.df.drop_duplicates()
        print("\n✨ Paso 1: Duplicados eliminados.")

        # --- PASO 2: Limpieza de la columna Precio ---
        # Queremos convertir '$1,200.00' y 'Gratis' en números reales.
        def clean_price(val):
            if val == 'Gratis': return 0.0
            return float(val.replace('$', '').replace(',', ''))

        self.df['Precio'] = self.df['Precio'].apply(clean_price)
        print("✨ Paso 2: Precios normalizados a float.")

        # --- PASO 3: Manejo de Nulos (NaN) ---
        # Si el Producto es nulo, eliminamos la fila. Si el Stock es nulo, ponemos 0.
        self.df = self.df.dropna(subset=['Producto'])
        self.df['Stock'] = self.df['Stock'].fillna(0)
        print("✨ Paso 3: Valores nulos gestionados.")

        # --- PASO 4: Corrección de Errores Lógicos ---
        # No puede haber stock negativo
        self.df = self.df[self.df['Stock'] >= 0]
        
        # --- PASO 5: Normalización de Fechas ---
        self.df['Fecha_Venta'] = pd.to_datetime(self.df['Fecha_Venta'], errors='coerce')
        print("✨ Paso 4 y 5: Errores lógicos y fechas corregidas.")

    def export_clean_data(self):
        print("\n✅ DATASET FINAL LIMPIO:")
        print(self.df)
        print("\n📊 Tipos de datos finales:")
        print(self.df.dtypes)
        
        # Guardamos el resultado
        self.df.to_csv("datos_limpios.csv", index=False)
        print("\n💾 Archivo 'datos_limpios.csv' generado con éxito.")

if __name__ == "__main__":
    cleaner = DataCleaner()
    cleaner.clean_process()
    cleaner.export_clean_data()