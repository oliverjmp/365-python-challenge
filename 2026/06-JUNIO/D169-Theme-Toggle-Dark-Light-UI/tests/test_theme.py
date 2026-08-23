from src.theme_manager import get_theme_styles

def test_get_theme_styles_dark():
    styles = get_theme_styles("Oscuro")
    assert styles["bg_color"] == "#0e1117"
    assert styles["text_color"] == "#fafafa"

def test_get_theme_styles_light():
    styles = get_theme_styles("Claro")
    assert styles["bg_color"] == "#ffffff"
    assert styles["text_color"] == "#31333f"