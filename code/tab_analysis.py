import streamlit as st
import pandas as pd
import numpy as np

def render_analysis():
    """Renders the content for the 'Analysis & KPIs' tab."""
    st.header("Enrollment Performance: Analysis & KPIs")
    
    # --- KPI CARD ---
    # Replace these with real calculated values
    enrollment_rate = 78.5
    st.metric(label="Enrollment Rate (Overall)", 
              value=f"{enrollment_rate:.1f}%", 
              delta="2.1% vs. Last Year", delta_color="normal")
    
    st.markdown("---") 

    # --- 3 VISUALS ---
    # Use columns to align the visuals nicely
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Visual 1: Commuter vs. Residential Trend")
        # Replace this with your actual chart code (e.g., Line Chart)
        st.bar_chart(np.random.rand(5, 2), use_container_width=True)
        st.caption("Weekly comparison of student commute type.")
        
    with col2:
        st.subheader("Visual 2: Program Attendance Breakdown")
        # Replace this with your actual chart code (e.g., Grouped Bar Chart)
        st.line_chart(np.random.rand(5, 4), use_container_width=True)
        st.caption("Trend across key A.M. programs.")

    st.subheader("Visual 3: Attendance by Weekday")
    # Replace this with your actual chart code (e.g., Pie Chart or Area Chart)
    st.area_chart(np.random.rand(7, 1), use_container_width=True)
    st.caption("Total attendance summed by day of the week.")
