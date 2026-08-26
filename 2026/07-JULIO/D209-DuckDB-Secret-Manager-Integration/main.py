from src.secret_manager import SecretManager

def main():
    print("=== D209: Ejecución CLI de Secret Manager ==y==")
    try:
        manager = SecretManager()
        config = manager.validar_credenciales()
        print("[✔] Configuración validada exitosamente:")
        for k, v in config.items():
            print(f" -> {k}: {v}")
    except Exception as e:
        print(f"[✖] Error crítico en secretos: {e}")

if __name__ == "__main__":
    main()