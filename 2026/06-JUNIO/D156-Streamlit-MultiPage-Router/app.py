import streamlit as st
from src.app_router import StreamlitRouter
from src.views_admin import render_admin_view
from src.views_client import render_client_view

def main():
    st.set_page_config(page_title="D156 Multi-Page Router", layout="wide")

    router = StreamlitRouter()
    router.register_route("Administración", render_admin_view)
    router.register_route("Portal Clientes", render_client_view)

    st.sidebar.title("Navegación de Negocio")
    role_choice = st.sidebar.radio("Seleccione el Perfil:", list(router.routes.keys()))

    st.sidebar.markdown("---")
    st.sidebar.info("Desarrollado para el desafío 365 Python Challenge (Hito D156).")

    if role_choice:
        router.render_navigation(role_choice)

if __name__ == "__main__":
    main()