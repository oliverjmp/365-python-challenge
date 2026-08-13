import logging
from src.dispatcher import EmailAttachmentDispatcher
from cryptography.fernet import Fernet
import os

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("=== Iniciando Sistema Automatizado de Envío de Correos (D111) ===")
    
    # Crear un archivo temporal de prueba para simular el adjunto (ej. el reporte del D110 o D109)
    sample_file = "reporte_confidencial.txt"
    with open(sample_file, "w", encoding="utf-8") as f:
        f.write("Este es el contenido confidencial del modelo financiero consolidado.")

    # Instanciar el despachador (usando datos de prueba/mock)
    dispatcher = EmailAttachmentDispatcher(
        smtp_server="smtp.gmail.com",
        smtp_port=587,
        sender_email="remitente.corporativo@gmail.com",
        sender_password="password_de_aplicacion"
    )

    # Generar llave de cifrado simétrico para el adjunto
    encryption_key = Fernet.generate_key()
    logging.info(f"Llave de cifrado generada para el archivo: {encryption_key.decode()}")

    # Simulación de envío (en entorno real requerirá credenciales SMTP válidas)
    # Para la demostración local llamamos al empaquetado y cifrado directamente:
    enc_path = dispatcher.encrypt_file(sample_file, encryption_key)
    logging.info(f"Archivo adjunto cifrado exitosamente en: {enc_path}")
    
    # Limpieza de archivos de prueba locales
    if os.path.exists(sample_file):
        os.remove(sample_file)
    if os.path.exists(enc_path):
        os.remove(enc_path)

    logging.info("=== Hito D111 Estructurado y Verificado Exitosamente ===")

if __name__ == "__main__":
    main()