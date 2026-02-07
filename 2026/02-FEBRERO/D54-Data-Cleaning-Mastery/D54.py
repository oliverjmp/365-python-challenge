"""
Proyecto: 365 Python Challenge
Día 54: Data Cleaning Mastery (Reforzado)
Objetivo: Limpiar un dataset realista y asegurar el guardado en la ruta correcta.
"""

import pandas as pd
import numpy as np
from pathlib import Path

class DataCleaner:
    def __init__(self):
        # 1. Gestión de rutas absoluta para evitar archivos perdidos
        self.directorio_actual = Path(__file__).parent.absolute()
        self.ruta_salida = self.directorio_actual / "datos_limpios.csv"

        # 2. Dataset "Sucio" de prueba
        raw_data = {
            'ID': [101, 102, 103, 103, 105, 106, 107], 
            'Producto': ['Laptop', 'Mouse', 'Monitor', 'Monitor', 'Teclado', None, 'Cámara'],
            'Precio': ['$1,200.00', '$25.00', '$300.00', '$300.00', 'Gratis', '$150.00', '$2,000.00'],
            'Stock': [15, 120, np.nan, np.nan, 50, 8, -5],
            'Fecha_Venta': ['2026-02-01', '2026-02-02', '03/02/2026', '03/02/2026', '2026-02-05', '06-02-26', '2026-02-07']
        }
        self.df = pd.DataFrame(raw_data)

    def clean_process(self):
        print("📁 Iniciando limpieza forense de datos...")

        # PASO 1: Eliminar Duplicados
        self.df = self.df.drop_duplicates()

        # PASO 2: Normalizar Precios (de string con símbolos a float)
        def clean_price(val):
            if val == 'Gratis': return 0.0
            return float(val.replace('$', '').replace(',', ''))

        self.df['Precio'] = self.df['Precio'].apply(clean_price)

        # PASO 3: Manejo de Nulos (NaN)
        self.df = self.df.dropna(subset=['Producto']) # Si no hay nombre de producto, fuera.
        self.df['Stock'] = self.df['Stock'].fillna(0)  # Si no hay stock, asumimos 0.

        # PASO 4: Corrección de Errores Lógicos
        self.df = self.df[self.df['Stock'] >= 0] # Eliminar stock negativo
        
        # PASO 5: Normalización de Fechas
        self.df['Fecha_Venta'] = pd.to_datetime(self.df['Fecha_Venta'], errors='coerce')
        
        print("✨ Limpieza completada con éxito.")

    def export_clean_data(self):
        print("\n✅ DATASET FINAL:")
        print(self.df)
        
        # Guardado robusto usando la ruta calculada en el constructor
        try:
            self.df.to_csv(self.ruta_salida, index=False)
            print(f"\n💾 Archivo guardado correctamente en:")
            print(f"📍 {self.ruta_salida}")
        except Exception as e:
            print(f"❌ Error al guardar el archivo: {e}")

if __name__ == "__main__":
    cleaner = DataCleaner()
    cleaner.clean_process()
    cleaner.export_clean_data()
    
    print("\n" + "═"*50)
    print("🚀 HITO D54 ACTUALIZADO: Datos limpios y localizados")
    print("═"*50)