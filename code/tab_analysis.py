import streamlit as st
import pandas as pd
import numpy as np

def render_analysis(dataframe):
    """
    Renders the Analysis & KPIs tab with a fixed KPI column (left)
    and a 2x3 grid of visuals (right).
    """
    st.header("Enrollment Performance: Analysis & KPIs")
    
    # --- MAIN LAYOUT SPLIT: KPI (1) vs. VISUALS (4) ---
    # Col_KPI takes 1/5th of the width (e.g., for the KPI card)
    # Col_Visuals takes 4/5ths of the width (for the 6 plots)
    col_kpi, col_visuals = st.columns([1, 4])
    
    # --- 1. LEFT COLUMN: STATIC KPI CARD ---
    with col_kpi:
        st.subheader("Key Metric")
        # Replace these with real calculated values
        total_enrollment = 985
        
        # KPI Card for Total Enrollment
        st.metric(label="Total Enrollment (Headcount)", 
                  value=f"{total_enrollment}", 
                  delta="x.x% vs. Last Year", delta_color="normal")
        
        # Add a placeholder for vertical alignment or more context if needed
        st.markdown("**Status:** Enrollment period is ongoing.")

    # --- 2. RIGHT COLUMN: 6 PLOTS (2x3 GRID) ---
    with col_visuals:
        df=dataframe
        st.subheader("Enrollment Visualizations (Weekly & Program Breakdown)")
        
        # Row 1 (Visuals 1 and 2 - STATIC)
        row1_col1, row1_col2 = st.columns(2)
        
        with row1_col1:
            st.caption("Visual 1 (Static): Commuter vs. Residential Trend")
            # STATIC CHART 1: Example is now a Line Chart
            st.line_chart(np.random.rand(5, 2), use_container_width=True)
            
        with row1_col2:
            st.caption("Visual 2 (Static): Program Attendance Breakdown")
            # STATIC CHART 2: Example is now a Bar Chart
            st.bar_chart(np.random.rand(5, 4), use_container_width=True)

        # Row 2 (Visuals 3 and 4 - DYNAMIC/PLACEHOLDER)
        row2_col1, row2_col2 = st.columns(2)
        
        with row2_col1:
            st.caption("Visual 3 (Dynamic): Placeholder")
            st.info("Chart 3 will be placed here.")
            
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
