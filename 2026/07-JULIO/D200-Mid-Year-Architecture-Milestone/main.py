from src.git_automator import GitMilestoneManager

def main():
    print("🚀 Iniciando auditoría del Hito D200 (Git Automation)...")
    try:
        manager = GitMilestoneManager()
        estado = manager.obtener_estado_actual()
        
        print(f"\n📊 Estado Actual del Repositorio:")
        print(f"   - Rama Activa: {estado['branch_activa']}")
        print(f"   - Último Commit: {estado['commit_reciente']} - '{estado['mensaje_commit']}'")
        print(f"   - Tags Existentes: {estado['tags_existentes']}")
        
        print("\n✨ ¡Auditoría de Git completada con éxito!")
    except Exception as e:
        print(f"❌ Error en la automatización: {e}")

if __name__ == "__main__":
    main()