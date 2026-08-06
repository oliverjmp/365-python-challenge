from sqlalchemy import Column, DateTime, Float, Integer, String
from database import Base


class CustomerModel(Base):
  __tablename__ = "dim_customer"

  customer_id = Column(Integer, primary_key=True, index=True)
  customer_name = Column(String, nullable=False)
  country = Column(String, nullable=False)