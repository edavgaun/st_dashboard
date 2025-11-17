import streamlit as st
import plotly.express as px
import pandas as pd

def render_map():
    """Renders the Choropleth map content."""
    st.header("Geographic Origin of Campers")
    
    # --- DUMMY DATA FOR MAP ---
    # In a real scenario, this data would come from your enrollment system.
    map_data = pd.DataFrame({
        "State": ["TX", "CA", "NY", "FL", "IL"],
        "Enrollment_Count": [50, 30, 25, 20, 15]
    })
    
    # --- PLOTLY CHOROPLETH ---
    try:
        fig = px.choropleth(map_data,
                            locations='State', 
                            locationmode='USA-states', 
                            color='Enrollment_Count',
                            scope='usa',
                            color_continuous_scale="Viridis",
                            title="Camper Enrollment by State"
                            )
        fig.update_layout(margin={"r":0,"t":40,"l":0,"b":0})
        st.plotly_chart(fig, use_container_width=True)
    except Exception as e:
        st.error(f"Could not render map. Ensure map data is correctly formatted. Error: {e}")
