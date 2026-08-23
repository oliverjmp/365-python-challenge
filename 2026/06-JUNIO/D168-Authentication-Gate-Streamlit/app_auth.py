import streamlit as st
from src.auth_manager import load_config, init_authenticator

st.set_page_config(
    page_title="D168 - Enterprise Authentication Gate",
    page_icon="🔒",
    layout="wide"
)

# Cargar configuración y preparar autenticador
config = load_config()
authenticator = init_authenticator(config)

# Renderizar el widget de inicio de sesión en la barra lateral
login_result = authenticator.login(location='sidebar')

# Validar si el resultado devolvió la tupla esperada o None
if login_result is not None:
    name, authentication_status, username = login_result
else:
    name, authentication_status, username = None, None, None

if authentication_status == False:
    st.error('❌ Usuario o contraseña incorrectos')
elif authentication_status == None:
    st.warning('⚠️ Por favor, introduce tus credenciales en la barra lateral para acceder.')
elif authentication_status:
    # Botón de cierre de sesión
    authenticator.logout('Cerrar Sesión', location='sidebar')
    
    st.title(f"🔐 Panel Ejecutivo Protegido - Bienvenido/a, {name}")
    st.success(f"Sesión iniciada exitosamente con el usuario: **{username}**")
    
    # Obtener el rol del usuario conectado
    user_roles = config['credentials']['usernames'][username].get('roles', [])
    
    st.markdown("---")
    st.subheader("📊 Módulo de Analítica Corporativa")
    
    if "admin" in user_roles:
        st.info("🛠️ **Vista de Administrador:** Tienes acceso total de lectura, escritura y gestión.")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Presupuesto Global Anual", "$1,450,000", "+12%")
        with col2:
            st.metric("Auditorías de Seguridad", "100% OK", "0 incidencias")
    else:
        st.warning("👁️ **Vista de Visualizador (Viewer):** Acceso restringido exclusivamente a lectura.")
        st.metric("Indicador de Desempeño Operativo", "94.8%", "+2.1%")