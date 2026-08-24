from dataset_manager_engine import PartitionedDatasetManagerEngine

def ejecutar_demostracion_d187():
    print("==================================================================")
    print("   D187 - GESTOR DE DATASETS PARTICIONADOS (PYARROW DATASETS)     ")
    print("==================================================================\n")

    manager = PartitionedDatasetManagerEngine()

    print("[1/3] Escribiendo dataset estructurado en árbol de particiones...")
    escritura = manager.escribir_dataset_particionado(120000)
    print(f" > Total filas: {escritura['filas_escritas']:,} | Tiempo: {escritura['tiempo_escritura_ms']} ms\n")

    print("[2/3] Ejecutando lectura selectiva con Partition Pruning (AMERICA, 2026-07-01)...")
    lectura = manager.leer_dataset_filtrado("AMERICA", "2026-07-01")
    print(f" > Latencia de consulta optimizada: {lectura['latencia_ms']} ms")
    print(f" > Filas recuperadas (filtradas en disco): {lectura['filas_recuperadas']:,}\n")

    print("[3/3] Muestra de registros filtrados:")
    print(lectura["dataframe_resultados"].head(5).to_string(index=False))

    print("\n==================================================================")
    print("            ¡DEMOSTRACIÓN D187 COMPLETADA CON ÉXITO!              ")
    print("==================================================================")

if __name__ == "__main__":
    ejecutar_demostracion_d187()