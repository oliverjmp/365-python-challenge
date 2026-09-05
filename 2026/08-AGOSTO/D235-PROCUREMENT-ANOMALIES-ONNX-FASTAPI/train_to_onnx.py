import os
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType

def generate_onnx_model():
    os.makedirs("models", exist_ok=True)
    
    # Datos simulados de compras: [monto, frecuencia_proveedor, desviacion_precio]
    X_train = np.random.rand(100, 3)
    y_train = np.random.choice([0, 1], size=100, p=[0.9, 0.1]) # 1 = Anomalía
    
    model = RandomForestClassifier(n_estimators=10, random_state=42)
    model.fit(X_train, y_train)
    
    # Definir el tipo de entrada esperado por ONNX (Tensores flotantes de 3 características)
    initial_type = [('float_input', FloatTensorType([None, 3]))]
    onx = convert_sklearn(model, initial_types=initial_type)
    
    with open("models/anomaly_model.onnx", "wb") as f:
        f.write(onx.SerializeToString())
    print("Modelo ONNX generado exitosamente en 'models/anomaly_model.onnx'")

if __name__ == "__main__":
    generate_onnx_model()