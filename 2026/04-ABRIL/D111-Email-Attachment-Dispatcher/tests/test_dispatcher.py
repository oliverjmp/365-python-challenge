import pytest
from src.dispatcher import EmailAttachmentDispatcher
from cryptography.fernet import Fernet
import os

@pytest.fixture
def dispatcher():
    return EmailAttachmentDispatcher("smtp.testserver.com", 587, "admin@test.com", "securepass")

def test_encryption_process(dispatcher, tmp_path):
    d_file = tmp_path / "reporte.xlsx"
    d_file.write_text("Datos financieros de prueba confidenciales")
    
    key = Fernet.generate_key()
    encrypted_path = dispatcher.encrypt_file(str(d_file), key)
    
    assert os.path.exists(encrypted_path)
    assert encrypted_path.endswith(".enc")
    
    # Validar desencriptación correcta
    with open(encrypted_path, "rb") as f:
        encrypted_data = f.read()
    
    f_dec = Fernet(key)
    decrypted_data = f_dec.decrypt(encrypted_data)
    assert b"Datos financieros" in decrypted_data

def test_create_message_structure(dispatcher, tmp_path):
    d_file = tmp_path / "documento.pdf"
    d_file.write_text("Contenido PDF")
    
    msg = dispatcher.create_message("cliente@test.com", "Reporte Mensual", "<p>Adjunto su reporte</p>", str(d_file))
    
    assert msg['From'] == "admin@test.com"
    assert msg['To'] == "cliente@test.com"
    assert msg['Subject'] == "Reporte Mensual"
    assert len(msg.get_payload()) == 2 # Texto MIME + Archivo Adjunto

def test_send_email_mocked(dispatcher, monkeypatch, tmp_path):
    d_file = tmp_path / "doc.txt"
    d_file.write_text("Hola")
    
    class MockSMTP:
        def __init__(self, server, port):
            pass
        def starttls(self):
            pass
        def login(self, user, password):
            pass
        def sendmail(self, sender, receiver, msg):
            pass
        def quit(self):
            pass

    monkeypatch.setattr("smtplib.SMTP", MockSMTP)
    
    key = Fernet.generate_key()
    result = dispatcher.send_email("destinatario@test.com", "Asunto Prueba", "Cuerpo", str(d_file), key)
    assert result is True

def test_send_email_exception_handling(dispatcher, monkeypatch):
    class MockSMTPError:
        def __init__(self, server, port):
            pass
        def starttls(self):
            raise Exception("Fallo de conexión SMTP simulado")

    monkeypatch.setattr("smtplib.SMTP", MockSMTPError)
    
    result = dispatcher.send_email("destinatario@test.com", "Asunto", "Cuerpo")
    assert result is False