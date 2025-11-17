import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from code.charts import create_stacked_bar_plot, create_enrollment_timeline_plot

def render_analysis(dataframe, longdataframe):
    """
    Renders the Analysis & KPIs tab with a fixed KPI column (left)
    and a 2x3 grid of visuals (right).
    """
    st.header("Enrollment Performance: Analysis & KPIs")
    
    # --- MAIN LAYOUT SPLIT: KPI (1) vs. VISUALS (6) ---
    # Col_KPI takes 1/8th of the width (e.g., for the KPI card)
    # Col_Visuals takes 7/8ths of the width (for the 6 plots)
    col_kpi, col_visuals = st.columns([1, 7])
    
    # --- 1. LEFT COLUMN: STATIC KPI CARD ---
    with col_kpi:
        st.subheader("Key Metric")
        # Replace these with real calculated values
        total_enrollment = 985
        
        # KPI Card for Total Enrollment
        st.metric(label="Total Enrollment (Count)", 
                  value=f"{total_enrollment}", 
                  delta="x.x% vs. Last Year", delta_color="normal")
        
        # Add a placeholder for vertical alignment or more context if needed
        st.markdown("**Status:** Enrollment period has finished.")

    # --- 2. RIGHT COLUMN: 6 PLOTS (2x3 GRID) ---
    with col_visuals:
        df=dataframe
        df_long_data=longdataframe
        st.subheader("Enrollment Visualizations (Weekly & Program Breakdown)")
        
        # Row 1 (Visuals 1 and 2 - STATIC)
        row1_col1, row1_col2 = st.columns(2)
        
        with row1_col1:
            stacked_fig = create_stacked_bar_plot(df)
            if stacked_fig:
                st.plotly_chart(stacked_fig, use_container_width=True)
            else:
                st.warning("Data for Stacked Bar Plot is unavailable or invalid.")
            
        with row1_col2:
            line_plot = create_enrollment_timeline_plot(df)
            if line_plot:
                st.plotly_chart(line_plot, use_container_width=True)
            else:
                st.warning("Data for Timeline Plot is unavailable or invalid.")

        # Row 2 (Visuals 3 and 4 - DYNAMIC/PLACEHOLDER)
        row2_col1, row2_col2 = st.columns(2)
        
        with row2_col1:
            selected_date = st.select_slider(
                    'Select Enrollment Date:',
                    options=date_options,
                    value=date_options[-1] if date_options else None, # Default to the latest date
                    help="Select the date for which to view the Commuter vs. Residential breakdown."
                )
            if selected_date and not df_long_data.empty:
                commute_fig = student_commute_plot(df_long_data, selected_date)
                st.pyplot(commute_fig, use_container_width=True)
            else:
                st.info("Select a date to view the attendance breakdown.")
            
        with row2_col2:
            st.caption("Visual 4 (Dynamic): Placeholder")
            st.info("Chart 4 will be placed here.")
            
        # Row 3 (Visuals 5 and 6 - DYNAMIC/PLACEHOLDER)
        row3_col1, row3_col2 = st.columns(2)
        
        with row3_col1:
            st.caption("Visual 5 (Dynamic): Placeholder")
            st.info("Chart 5 will be placed here.")
            
        with row3_col2:
            st.caption("Visual 6 (Dynamic): Placeholder")
            st.info("Chart 6 will be placed here.")
