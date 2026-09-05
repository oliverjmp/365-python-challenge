import pandas as pd
import great_expectations as gx

class DataQualityValidator:
    """Motor de validación de calidad de datos corporativos utilizando Great Expectations."""
    
    def __init__(self):
        # Inicializa un contexto efímero en memoria para evaluaciones ultrarrápidas
        self.context = gx.get_context(mode="ephemeral")

    def validate_procurement_data(self, df: pd.DataFrame) -> dict:
        """Ejecuta el contrato de datos sobre transacciones de compras."""
        if df.empty:
            raise ValueError("El DataFrame a evaluar se encuentra vacío. Imposible certificar calidad.")
        
        # Convertir Pandas DataFrame a un Dataset de Great Expectations
        gx_df = gx.from_pandas(df)
        
        # 1. Integridad: El monto no puede ser nulo
        gx_df.expect_column_values_to_not_be_null("monto")
        
        # 2. Rango Lógico: El monto debe ser un valor positivo
        gx_df.expect_column_values_to_be_between("monto", min_value=0.01)
        
        # 3. Consistencia Categórica: Estados permitidos en el pipeline
        gx_df.expect_column_values_to_be_in_set("estado", ["APROBADO", "RECHAZADO", "PENDIENTE"])
        
        # Ejecutar la suite de validación
        results = gx_df.validate()
        
        return {
            "success": results["success"],
            "statistics": results["statistics"],
            "details": results["results"]
        }