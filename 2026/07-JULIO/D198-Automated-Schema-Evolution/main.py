from src.schema_evolution import SchemaEvolutionManager

def main():
    print("🚀 Iniciando pipeline de Evolución Automática de Esquemas (PyArrow)...")
    manager = SchemaEvolutionManager(dataset_dir="data_lake")

    print("\n📦 Escribiendo Lote 1 (Esquema base)...")
    path_1 = manager.guardar_lote_inicial()
    print(f"   -> Guardado en: {path_1}")

    print("\n📦 Escribiendo Lote 2 (Esquema evolucionado)...")
    path_2 = manager.guardar_lote_evolucionado()
    print(f"   -> Guardado en: {path_2}")

    print("\n🔍 Ejecutando lectura unificada del Dataset con PyArrow...")
    tabla_unificada = manager.leer_dataset_unificado()

    print(f"\n📊 Esquema Resultante Consolidado:")
    for field in tabla_unificada.schema:
        print(f"   - Campo: {field.name} | Tipo: {field.type}")

    print(f"\n📈 Total de registros consolidados: {tabla_unificada.num_rows}")
    print("\n📋 Vista tabular completa:")
    print(tabla_unificada.to_pandas().to_string(index=False))
    print("\n✨ ¡Proceso finalizado con éxito!")

if __name__ == "__main__":
    main()