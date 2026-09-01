"""Motor OLAP in-memory de alta velocidad basado en DuckDB para datos masivos de Procurement OpEx."""

import logging
from typing import Dict, Any
import duckdb
import numpy as np
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class ProcurementDatabaseManager:
    """Gestiona el motor DuckDB in-memory e ingesta datasets masivos de compra OpEx."""

    def __init__(self, record_count: int = 50000):
        self.record_count = record_count
        self.conn = duckdb.connect(database=":memory:")
        self._seed_database()

    def _seed_database(self) -> None:
        """Genera e ingesta 50,000 registros sintéticos enterprise con integridad referencial."""
        logging.info("Generando dataset sintético de Procurement con %d registros...", self.record_count)
        np.random.seed(42)

        categories = [
            "IT Hardware", 
            "Logistics", 
            "Office Supplies", 
            "Consulting", 
            "Facilities Services", 
            "Cloud Infrastructure"
        ]
        statuses = ["APPROVED", "PENDING", "REJECTED", "CANCELLED"]
        payment_terms = ["NET30", "NET60", "NET90", "IMMEDIATE"]
        cost_centers = ["CC-101-FINANCE", "CC-202-IT", "CC-303-OPS", "CC-404-HR", "CC-505-MARKETING"]

        df_orders = pd.DataFrame({
            "order_id": [f"PO-2026-{100000 + i}" for i in range(self.record_count)],
            "supplier_id": np.random.randint(100, 600, size=self.record_count),
            "category": np.random.choice(categories, size=self.record_count, p=[0.25, 0.20, 0.15, 0.15, 0.15, 0.10]),
            "cost_center": np.random.choice(cost_centers, size=self.record_count),
            "status": np.random.choice(statuses, size=self.record_count, p=[0.70, 0.15, 0.10, 0.05]),
            "payment_terms": np.random.choice(payment_terms, size=self.record_count, p=[0.4, 0.3, 0.2, 0.1]),
            "unit_price": np.round(np.random.exponential(scale=500, size=self.record_count) + 10, 2),
            "quantity": np.random.randint(1, 100, size=self.record_count),
            "order_date": pd.date_range(start="2024-01-01", periods=self.record_count, freq="min").strftime("%Y-%m-%d %H:%M:%S")
        })

        # Cálculo explícito de monto total
        df_orders["total_amount"] = np.round(df_orders["unit_price"] * df_orders["quantity"], 2)

        df_suppliers = pd.DataFrame({
            "supplier_id": np.arange(100, 600),
            "supplier_name": [f"Proveedor Global {i} S.L." for i in range(100, 600)],
            "country": np.random.choice(["ES", "FR", "DE", "IT", "UK", "US"], size=500),
            "supplier_rating": np.round(np.random.uniform(1.0, 5.0, size=500), 2)
        })

        self.conn.register("purchase_orders_temp", df_orders)
        self.conn.register("suppliers_temp", df_suppliers)

        self.conn.execute("CREATE TABLE purchase_orders AS SELECT * FROM purchase_orders_temp")
        self.conn.execute("CREATE TABLE suppliers AS SELECT * FROM suppliers_temp")
        logging.info("Tablas 'purchase_orders' y 'suppliers' creadas exitosamente en DuckDB.")

    def get_schema_info(self) -> str:
        """Retorna la definición DDL estructurada para inyección contextual en el prompt."""
        return """
        CREATE TABLE purchase_orders (
            order_id VARCHAR PRIMARY KEY,
            supplier_id INTEGER,
            category VARCHAR,
            cost_center VARCHAR,
            status VARCHAR,
            payment_terms VARCHAR,
            unit_price DOUBLE,
            quantity INTEGER,
            total_amount DOUBLE,
            order_date TIMESTAMP,
            FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
        );

        CREATE TABLE suppliers (
            supplier_id INTEGER PRIMARY KEY,
            supplier_name VARCHAR,
            country VARCHAR,
            supplier_rating DOUBLE
        );
        """

    def execute_query(self, query: str) -> pd.DataFrame:
        """Ejecuta una consulta SQL formateada y valida que no contenga sentencias destructivas."""
        sanitized_query = query.strip().rstrip(";")
        forbidden_keywords = ["DROP", "DELETE", "UPDATE", "INSERT", "ALTER", "TRUNCATE"]
        
        for kw in forbidden_keywords:
            if f" {kw} " in f" {sanitized_query.upper()} ":
                raise ValueError(f"Seguridad SQL: Operación restringida '{kw}' detectada.")

        return self.conn.execute(sanitized_query).df()