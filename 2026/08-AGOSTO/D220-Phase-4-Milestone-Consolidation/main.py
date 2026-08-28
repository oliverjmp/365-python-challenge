from src.pipeline_validator import MilestonePipelineValidator

def main():
    print("=== D220: Cierre y Consolidación de la Fase 4 (Git CI/CD Automation) ===")
    status = MilestonePipelineValidator.verify_consolidation_status("Fase-4-Milestone")
    print(f"[✔] Estado del Hito: {status}")

if __name__ == "__main__":
    main()