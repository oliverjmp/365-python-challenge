from src.spatial_runner import SpatialQueryRunner

def main():
    print("🌍 Inicializando motor geoespacial D201...")
    runner = SpatialQueryRunner()
    resultados = runner.ejecutar_consulta_espacial()
    
    print("\n📍 Resultados de Puntos de Interés Geoespacial:")
    for row in resultados:
        print(f"   - ID: {row[0]} | Ubicación: {row[1]} | Lat/Lon: ({row[2]}, {row[3]}) | WKT: {row[4]}")
    
    print("\n✨ ¡Ejecución geoespacial completada con éxito!")

if __name__ == "__main__":
    main()