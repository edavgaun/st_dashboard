import streamlit as st
import plotly.express as px
import pandas as pd

def render_map():
    """Renders the Choropleth map content."""
    st.header("Geographic Origin of Campers")

    # --- LOAD REAL DATA ---
    try:
        map_data = pd.read_csv("data/state_freq.csv")

        # --- CLEAN & VALIDATE ---
        # Normalize column names
        map_data.columns = map_data.columns.str.strip().str.capitalize()

        # Ensure expected columns exist
        if "State" not in map_data.columns or "Count" not in map_data.columns:
            st.error("CSV must contain 'State' and 'Count' columns.")
            st.write("Columns found:", list(map_data.columns))
            return

    except Exception as e:
        st.error(f"Error loading CSV: {e}")
        return

    # --- PLOT ---
    try:
        fig = px.choropleth(
            map_data,
            locations="State",
            locationmode="USA-states",
            color="Count",
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
