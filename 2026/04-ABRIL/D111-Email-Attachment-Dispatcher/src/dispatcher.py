import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from cryptography.fernet import Fernet
import os
from pathlib import Path

class EmailAttachmentDispatcher:
    def __init__(self, smtp_server: str, smtp_port: int, sender_email: str, sender_password: str):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def encrypt_file(self, file_path: str, encryption_key: bytes) -> str:
        """Cifra un archivo adjunto utilizando la librería cryptography (Fernet)."""
        f = Fernet(encryption_key)
        path = Path(file_path)
        
        with open(path, "rb") as file:
            file_data = file.read()
            
        encrypted_data = f.encrypt(file_data)
        encrypted_path = path.with_suffix(path.suffix + ".enc")
        
        with open(encrypted_path, "wb") as file:
            file.write(encrypted_data)
            
        return str(encrypted_path)

    def create_message(self, receiver_email: str, subject: str, body: str, attachment_path: str = None) -> MIMEMultipart:
        """Crea el mensaje MIME con soporte para texto enriquecido y archivos adjuntos."""
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'html'))

        if attachment_path and os.path.exists(attachment_path):
            path = Path(attachment_path)
            with open(path, "rb") as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename= "{path.name}"')
            msg.attach(part)

        return msg

    def send_email(self, receiver_email: str, subject: str, body: str, attachment_path: str = None, encryption_key: bytes = None) -> bool:
        """Envía el correo electrónico a través de SMTP, cifrando opcionalmente el archivo adjunto."""
        target_attachment = attachment_path
        if attachment_path and encryption_key:
            target_attachment = self.encrypt_file(attachment_path, encryption_key)

        msg = self.create_message(receiver_email, subject, body, target_attachment)

        try:
            # En entorno de producción real se usaría SMTP_SSL o starttls
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.sender_email, self.sender_password)
            server.sendmail(self.sender_email, receiver_email, msg.as_string())
            server.quit()
            return True
        except Exception as e:
            print(f"Error al enviar el correo: {e}")
            return False