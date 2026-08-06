import pandas as pd
import pytest
from anonymizer import PIIAnonymizer

@pytest.fixture
def anonymizer_engine() -> PIIAnonymizer:
    return PIIAnonymizer()

def test_mask_email(anonymizer_engine: PIIAnonymizer) -> None:
    email = "oliver.data@empresa.es"
    masked = anonymizer_engine.mask_email(email)
    assert masked.startswith("o***@")
    assert masked.endswith("empresa.es")

def test_mask_phone(anonymizer_engine: PIIAnonymizer) -> None:
    phone = "+34 600 123 456"
    masked = anonymizer_engine.mask_phone(phone)
    assert masked == "***-***-3456"

def test_mask_credit_card(anonymizer_engine: PIIAnonymizer) -> None:
    cc = "4532-1234-5678-9012"
    masked = anonymizer_engine.mask_credit_card(cc)
    assert masked == "****-****-****-9012"

def test_anonymize_dataframe(anonymizer_engine: PIIAnonymizer) -> None:
    raw_data = pd.DataFrame({
        "email": ["test@example.com"],
        "phone": ["912345678"],
        "credit_card": ["1234567812345678"],
        "dni": ["12345678A"]
    })
    secured_df = anonymizer_engine.anonymize_dataframe(raw_data)
    assert secured_df["email"].iloc[0] == "t***@example.com"
    assert secured_df["phone"].iloc[0] == "***-***-5678"
    assert secured_df["credit_card"].iloc[0] == "****-****-****-5678"
    assert secured_df["dni"].iloc[0] == "****5678-A"