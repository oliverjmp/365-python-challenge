from src.pipeline_runner import DockerDuckDBPipeline

def main():
    print("🐳 Ejecutando pipeline analítico en contenedor (D203)...")
    pipeline = DockerDuckDBPipeline()
    df_resultados = pipeline.ejecutar_proceso()
    
    print("\n📊 Resultados del Pipeline:")
    print(df_resultados.to_string(index=False))
    print("\n✨ ¡Pipeline ejecutado exitosamente dentro de Docker!")

if __name__ == "__main__":
    main()