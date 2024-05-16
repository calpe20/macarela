import streamlit as st
from streamlit_option_menu import option_menu
import folium
from streamlit_folium import st_folium
import streamlit.components.v1 as components


page_title = "Macarela Voley Playa"
page_icon = ":volleyball:"
layout = "centered"

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
    url = "https://www.facebook.com/profile.php?id=61553346112578&sk=photos"
    st.markdown(f'<iframe src="{url}" width="100%" height="600"></iframe>', unsafe_allow_html=False)

