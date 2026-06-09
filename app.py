import streamlit as st
import requests
import folium
from streamlit_folium import st_folium

# Configuración del título de la pestaña del navegador
st.set_page_config(page_title="Gestión de Reclamos Urbano", layout="centered")

# --- TÍTULOS FORMALES ---
st.title("🏛️ Sistema de Gestión de Reclamos Ciudadanos")
st.subheader("Plataforma de Atención al Vecino - Municipio")

# --- FORMULARIO DE CARGA ---
st.markdown("---")
st.markdown("### 📝 Registrar Nuevo Reclamo")

with st.form("formulario_reclamo", clear_on_submit=True):
    nombre = st.text_input("Nombre completo del ciudadano:")
    email = st.text_input("Correo electrónico de contacto:")
    
    tipo = st.selectbox(
        "Tipo de Reclamo:",
        ["💡 Alumbrado público roto", 
         "🗑️ Basura acumulada", 
         "🚗 Baches / Deterioro vial", 
         "🌳 Árboles caídos o en peligro", 
         "🚦 Semáforos fuera de servicio"]
    )
    
    direccion = st.text_input("Dirección exacta / Altura de la calle:")
    descripcion = st.text_area("Descripción extendida del problema:")
    
    boton_registrar = st.form_submit_button("Registrar Reclamo")

# Lógica al apretar "Registrar"
if boton_registrar:
    if nombre and email and direccion and descripcion:
        datos_reclamo = {
            "nombre": nombre,
            "email": email,
            "tipo": tipo,
            "direccion": direccion,
            "descripcion": descripcion
        }
        try:
            url_backend = "http://localhost:8080/api/v1/reclamo" 
            # respuesta = requests.post(url_backend, json=datos_reclamo)
            
            st.success("¡Reclamo enviado con éxito al backend!")
            st.toast("El formulario se ha limpiado automáticamente.")
        except Exception as e:
            st.error(f"No se pudo conectar con el Backend: {e}")
    else:
        st.warning("Por favor, completa todos los campos del formulario antes de enviar.")

# --- VISTA DE RECLAMOS EXISTENTES (TABLA) ---
st.markdown("---")
st.markdown("### 📋 Historial y Lista de Reclamos")

# Datos simulados para la interfaz
reclamos_actuales = [
    {"id": 1, "nombre": "Juan Perez", "tipo": "🚗 Baches", "direccion": "Av. de Mayo 800", "lat": -34.6083, "lon": -58.3806, "estado": "Pendiente"},
    {"id": 2, "nombre": "Maria Lopez", "tipo": "🗑️ Basura", "direccion": "Rivadavia 1500", "lat": -34.6095, "lon": -58.3890, "estado": "Resuelto"}
]

if st.button("🔄 Actualizar Lista de Reclamos"):
    try:
        # url_get = "http://localhost:8080/api/v1/reclamos"
        # respuesta = requests.get(url_get)
        # reclamos_actuales = respuesta.json()
        st.table(reclamos_actuales)
    except:
        st.error("Error al conectar con la API.")

# --- VISUALIZACIÓN GEOGRÁFICA (MAPA LEAFLET) ---
st.markdown("---")
st.markdown("### 🗺️ Mapa Interactivo de Incidentes Activos")

mapa = folium.Map(location=[-34.6037, -58.3816], zoom_start=13)

for reclamo in reclamos_actuales:
    popup_text = f"""
    <b>Reclamo #{reclamo['id']}</b><br>
    <b>Tipo:</b> {reclamo['tipo']}<br>
    <b>Dirección:</b> {reclamo['direccion']}<br>
    <b>Estado:</b> {reclamo['estado']}
    """
    
    folium.Marker(
        location=[reclamo["lat"], reclamo["lon"]],
        popup=folium.Popup(popup_text, max_width=300),
        tooltip=reclamo["tipo"],
        icon=folium.Icon(color="red" if reclamo["estado"] == "Pendiente" else "green", icon="info-sign")
    ).add_to(mapa)

st_folium(mapa, width=700, height=450)
