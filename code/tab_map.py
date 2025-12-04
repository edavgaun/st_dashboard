import streamlit as st
import plotly.express as px
import pandas as pd

def render_map():
    """Renders the Choropleth map content."""
    st.header("Geographic Origin of Campers")

    # --- LOAD REAL DATA ---
    map_data = pd.read_csv("data/state_freq.csv")
    map_data.columns=['State', 'count']

    # --- PLOT ---
    try:
        fig = px.choropleth(
            map_data,
            locations="State",
            locationmode="USA-states",
            color="count",
            scope="usa",
            color_continuous_scale="Viridis",
            title="Camper Enrollment by State"
        )

        fig.update_layout(
            margin={"r": 0, "t": 40, "l": 0, "b": 0},
            paper_bgcolor="#000121",   # Dark paper background
            plot_bgcolor="#000121",    # Background behind axes (if any)
            geo_bgcolor="#000121"      # Background for the map itself
        )

        st.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        st.error(f"Could not render map. Error: {e}")
