import streamlit as st
from streamlit_option_menu import option_menu
import folium
from streamlit_folium import st_folium
import streamlit.components.v1 as components


page_title = "Macarela Voley Playa"
page_icon = ":volleyball:"
layout = "centered"

horas = ["14:00","15:00","16:00","17:00","18:00","19:00","20:00","21:00", "22:00", "23:00"]

st.set_page_config(
    page_title=page_title,
    page_icon=page_icon,
    layout=layout
)

st.image("./assets/principal.jpg")

st.title("Macarela Voley PLaya")
st.text("Jr Pachitea c/ Zaplana Belliza")

selected = option_menu(menu_title=None, 
                       options=["Reservar", "Galeria", "Detalles"],
                       icons=["calendar-date", "camera", "list"],
                       orientation="horizontal")
if selected == "Reservar":
    st.subheader("Reservar")
    c1, c2 = st.columns(2)
    c1.text_input("Tu nombre", placeholder="Nombre")
    c2.text_input("Tu Número Celular")
    c1.date_input("Fecha")
    c2.multiselect("Hora", horas, placeholder="Seleccione las horas a Reservar")
    st.text_area("Notas")


if selected == "Galeria":
    st.subheader("Galería de Imágenes con Deslizamiento")

    # Lista de URLs de imágenes
    image_urls = [
        "https://scontent-lim1-1.xx.fbcdn.net/v/t39.30808-6/424880342_122126771720111537_7494779318361705032_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=5f2048&_nc_eui2=AeG1-_NqhSgQWmM7HHFA_Xe-Zmzc2dzzriJmbNzZ3POuIgMniLdLw9tyUTt6iAU4WBY&_nc_ohc=7HL5jo3QPmgQ7kNvgHuF9jw&_nc_ht=scontent-lim1-1.xx&cb_e2o_trans=t&oh=00_AYCWJgaKaQb9Esx0k6cJWBHtmz-dT7yqOnsptBUFNarsPg&oe=664B71F5",
        "https://via.placeholder.com/600x400.png?text=Imagen+2",
        "https://via.placeholder.com/600x400.png?text=Imagen+3",
        "https://via.placeholder.com/600x400.png?text=Imagen+4"
    ]

    for a in image_urls:
        st.image(a)

if selected == "Detalles":
    m = folium.Map(location=[-8.37343, -74.53733], zoom_start=18)  # Ejemplo: Madrid, España

    # Agregar un marcador
    folium.Marker(
        location=[-8.37343, -74.53733],
        popup="Madrid",
        icon=folium.Icon(icon="cloud"),
    ).add_to(m)

    # Mostrar el mapa en Streamlit
    st_folium(m, width=800, height=300)
    st.subheader("Horarios")
    dia, hora = st.columns(2)
    dia.text("Lunes")
    hora.text("14:00 - 23:00")
    dia.text("Martes")
    hora.text("14:00 - 23:00")
    dia.text("Miercoles")
    hora.text("14:00 - 23:00")
    dia.text("Jueves")
    hora.text("14:00 - 23:00")
    dia.text("Viernes")
    hora.text("14:00 - 23:00")
    dia.text("Sabado")
    hora.text("14:00 - 23:00")
    dia.text("Domingo")
    hora.text("14:00 - 23:00")

    contacto, facebook = st.columns(2)
    contacto.subheader("Contacto")
    contacto.text("📱 944 173 183" )
    facebook.subheader("Facebook")
    facebook.markdown("Sìguenos [aqui](https://www.facebook.com/profile.php?id=61553346112578) en Facebook")