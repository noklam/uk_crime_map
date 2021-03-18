import streamlit as st
from streamlit_folium import folium_static
import folium

# title
st.title("UK Crime Heatmap")




import folium

def generateBaseMap(default_location=[40.693943, -73.985880], default_zoom_start=12):
    base_map = folium.Map(location=default_location, control_scale=True, zoom_start=default_zoom_start)
    return base_map


def get_data():
    df = pd.read_csv()

def add_marker(coordinates, popup, tooltip):
    return folium.Marker(coordinates, popup=popup, tooltip=tooltip)

with st.echo():
    base_map = generateBaseMap()
    coord = [39.949610, -75.150282]
    popup = "Liberty Bell"
    tooltip = "Liberty Bell"
    add_marker(coord, popup=popup, tooltip=tooltip).add_to(base_map)
    folium_static(base_map)
