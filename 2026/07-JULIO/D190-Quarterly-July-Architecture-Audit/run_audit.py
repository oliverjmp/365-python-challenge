import logging
from src.audit_engine import QuarterlyArchitectureAuditor

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    print("==================================================================")
    print("   D190 - AUDITORÍA INTEGRAL DE ARQUITECTURA (JULIO / FASE 4)    ")
    print("==================================================================\n")
    
    auditor = QuarterlyArchitectureAuditor(storage_path="data_lake/architecture_state.json")
    
    try:
        logging.info("Cargando y validando estado de la arquitectura desde el Data Lake...")
        raw_data = auditor.load_raw_data()
        print(f" > Carga exitosa del archivo JSON. Trimestre: {raw_data.get('quarter')}")
        
        logging.info("Ejecutando motor de auditoría y métricas de rendimiento...")
        summary = auditor.audit_architecture()
        
        print("\n------------------ INFORME EJECUTIVO DE AUDITORÍA ------------------")
        print(f" • Trimestre Evaluado        : {summary['quarter']}")
        print(f" • Fase del Proyecto         : {summary['phase']}")
        print(f" • Total Módulos Analizados  : {summary['total_components']}")
        print(f" • Módulos Conformes         : {summary['components_conformes']}")
        print(f" • Índice de Cumplimiento    : {summary['compliance_rate']:.1f}%")
        print(f" • Rendimiento Promedio      : {summary['average_performance_score']} pts")
        print(f" • Dictamen Final            : ✅ {summary['status']}")
        print("--------------------------------------------------------------------\n")
        
        logging.info("=== Hito D190 Ejecutado Exitosamente ===")
        
    except Exception as e:
        logging.error(f"Error crítico durante la auditoría: {e}")

if __name__ == "__main__":
    main()