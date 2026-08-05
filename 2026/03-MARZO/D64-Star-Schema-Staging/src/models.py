from datetime import date
from typing import Optional
from sqlmodel import Field, SQLModel

class DimCustomer(SQLModel, table=True):
    __tablename__ = "dim_customer"
    customer_id: Optional[int] = Field(default=None, primary_key=True)
    customer_name: str
    country: str

class DimProduct(SQLModel, table=True):
    __tablename__ = "dim_product"
    product_id: Optional[int] = Field(default=None, primary_key=True)
    product_name: str
    category: str

class DimDate(SQLModel, table=True):
    __tablename__ = "dim_date"
    date_key: int = Field(primary_key=True)  # Formato YYYYMMDD
    full_date: date
    year: int
    month: int
    day: int

class FactTransaction(SQLModel, table=True):
    __tablename__ = "fact_transaction"
    transaction_id: Optional[int] = Field(default=None, primary_key=True)
    customer_id: int = Field(foreign_key="dim_customer.customer_id")
    product_id: int = Field(foreign_key="dim_product.product_id")
    date_key: int = Field(foreign_key="dim_date.date_key")
    quantity: int
    total_amount: float