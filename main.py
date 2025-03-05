import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
import plotly.express as px
from utils.data_processor import process_city_data
from utils.location_scorer import score_locations
from utils.map_generator import create_map
from utils.visualization import create_heatmap, create_traffic_flow

# Page configuration
st.set_page_config(
    page_title="EV Charging Station Optimizer - India",
    page_icon="🔌",
    layout="wide"
)

# Custom CSS
with open('assets/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Header
st.title("🔌 EV Charging Station Location Optimizer - India")
st.markdown("Optimize EV charging station locations across major Indian cities")

# Sidebar for inputs
st.sidebar.header("City Parameters")

# City selection (Indian cities)
city = st.sidebar.selectbox(
    "Select City",
    ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai", "Kolkata", "Pune", "Ahmedabad"]
)

# Input parameters adjusted for Indian context
population_density = st.sidebar.slider(
    "Population Density (people/km²)",
    1000, 50000, 20000,
    help="Indian cities typically have high population density"
)

traffic_volume = st.sidebar.slider(
    "Average Daily Traffic Volume",
    5000, 200000, 50000,
    help="Daily traffic volume in selected area"
)

existing_stations = st.sidebar.number_input(
    "Number of Existing Charging Stations",
    0, 1000, 5,
    help="Current number of EV charging stations in the area"
)

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Interactive Map")

    # Create and display map
    m = create_map(city)
    folium_static(m, width=800)

with col2:
    st.subheader("Location Score Analysis")

    # Calculate and display scores
    scores = score_locations(population_density, traffic_volume, existing_stations)

    # Display top locations
    st.write("Top Recommended Locations:")
    for idx, (loc, score) in enumerate(scores[:5], 1):
        st.write(f"{idx}. {loc}: {score:.2f}")

# Visualization section
st.header("Data Visualization")

tab1, tab2, tab3 = st.tabs(["Population Density", "Traffic Flow", "Station Distribution"])

with tab1:
    st.plotly_chart(create_heatmap(city), use_container_width=True)

with tab2:
    st.plotly_chart(create_traffic_flow(city), use_container_width=True)

with tab3:
    # Sample station distribution plot
    df = pd.read_csv('data/sample_data.csv')
    fig = px.scatter_map(
        df,
        lat='latitude',
        lon='longitude',
        color='usage_rate',
        size='capacity',
        title='Existing Station Distribution'
    )
    st.plotly_chart(fig, use_container_width=True)

# Report generation
if st.button("Generate Report"):
    st.download_button(
        label="Download Report",
        data=process_city_data(city, population_density, traffic_volume, existing_stations),
        file_name=f"{city}_ev_charging_report.csv",
        mime="text/csv"
    )