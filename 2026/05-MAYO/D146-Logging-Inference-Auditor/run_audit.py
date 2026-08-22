import time
from src.auditor import InferenceAuditor

def main():
    print("=== Iniciando Demostración de Logging Inference Auditor (D146) ===")

    auditor = InferenceAuditor(logger_name="ProductionAuditor")

    # 1. Simular una inferencia exitosa
    def dummy_model_predict():
        time.sleep(0.05)  # Simular latencia de cómputo
        return {"prediction": 1, "probability": 0.88}

    print("\nEjecutando inferencia exitosa...")
    auditor.audit_inference(
        request_id="req-uuid-abc-123",
        model_version="v2.1.0",
        features=[5.1, 3.5, 1.4, 0.2],
        inference_func=dummy_model_predict
    )

    # 2. Simular una inferencia fallida
    def dummy_failing_predict():
        time.sleep(0.02)
        raise ValueError("Vector de características con dimensiones inválidas.")

    print("\nEjecutando inferencia con fallo...")
    try:
        auditor.audit_inference(
            request_id="req-uuid-xyz-789",
            model_version="v2.1.0",
            features=[99.9],
            inference_func=dummy_failing_predict
        )
    except ValueError:
        pass  # Excepción esperada controlada

    print("\n=== Hito D146 Ejecutado Exitosamente ===")

if __name__ == "__main__":
    main()