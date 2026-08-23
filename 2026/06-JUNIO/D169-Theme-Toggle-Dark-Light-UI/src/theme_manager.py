def get_theme_styles(theme_name: str) -> dict:
    """
    Retorna un diccionario con los colores e hiperparámetros CSS según el tema seleccionado.
    """
    if theme_name == "Oscuro":
        return {
            "bg_color": "#0e1117",
            "text_color": "#fafafa",
            "card_bg": "#262730",
            "accent": "#ff4b4b"
        }
    else:
        return {
            "bg_color": "#ffffff",
            "text_color": "#31333f",
            "card_bg": "#f0f2f6",
            "accent": "#ff4b4b"
        }