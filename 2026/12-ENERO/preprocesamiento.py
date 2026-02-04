import re
import unicodedata
from langdetect import detect, DetectorFactory

DetectorFactory.seed = 0  # Para resultados consistentes

# ============================
# DETECCIÓN DE IDIOMA
# ============================

def detectar_idioma(texto: str) -> str:
    try:
        idioma = detect(texto)
        return idioma
    except:
        return "unknown"

# ============================
# NORMALIZACIÓN DEL TEXTO
# ============================

def eliminar_tildes(texto: str) -> str:
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

def eliminar_urls(texto: str) -> str:
    return re.sub(r"http\S+|www\S+|https\S+", "", texto)

def eliminar_emojis(texto: str) -> str:
    emoji_pattern = re.compile(
        "[" 
        u"\U0001F600-\U0001F64F"  # emoticonos
        u"\U0001F300-\U0001F5FF"  # símbolos
        u"\U0001F680-\U0001F6FF"  # transporte
        u"\U0001F1E0-\U0001F1FF"  # banderas
        "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', texto)

def eliminar_repeticiones(texto: str) -> str:
    return re.sub(r"(.)\1{2,}", r"\1\1", texto)

def limpiar_signos(texto: str) -> str:
    return re.sub(r"[^a-zA-Z0-9áéíóúñüÁÉÍÓÚÑÜ\s]", " ", texto)

def normalizar_texto(texto: str) -> str:
    texto = texto.lower()
    texto = eliminar_urls(texto)
    texto = eliminar_emojis(texto)
    texto = eliminar_tildes(texto)
    texto = eliminar_repeticiones(texto)
    texto = limpiar_signos(texto)
    texto = re.sub(r"\s+", " ", texto).strip()
    return texto
