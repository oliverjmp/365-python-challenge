from src.benchmark_runner import BenchmarkRunner

def main():
    print("⚡ Iniciando Benchmark D202 (Pandas vs DuckDB)...")
    runner = BenchmarkRunner(num_filas=500_000)
    res = runner.ejecutar_comparativa()
    
    print(f"\n📊 Resultados para {res['filas']:,} registros:")
    print(f"   - Pandas (segundos): {res['pandas_segundos']:.5f} s")
    print(f"   - DuckDB (segundos): {res['duckdb_segundos']:.5f} s")
    print(f"   - Mejora de velocidad: {res['mejora_x']}x más rápido con DuckDB 🚀")
    
    print("\n✨ ¡Benchmark completado con éxito!")

if __name__ == "__main__":
    main()