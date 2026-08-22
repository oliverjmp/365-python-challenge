import os
import joblib
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier

def train_and_save_model():
    os.makedirs("src/models", exist_ok=True)
    X, y = make_classification(n_samples=100, n_features=4, random_state=42)
    model = RandomForestClassifier(random_state=42)
    model.fit(X, y)
    
    model_path = "src/models/model.joblib"
    joblib.dump(model, model_path)
    print(f"Modelo entrenado y guardado exitosamente en: {model_path}")

if __name__ == "__main__":
    train_and_save_model()