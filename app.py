import streamlit as st
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from code.tab_info import render_info
from code.tab_analysis import render_analysis
from code.tab_map import render_map

# --- 1. CONFIGURATION ---
st.set_page_config(layout="wide")

# --- 2. HEADER BANNER (CONSTANT) ---
def render_header():
    """Renders a consistent header/banner across the top."""
    st.image("your_banner_image.png", use_column_width=True) # Replace with your image file path or URL
    st.title("📊 RCEL Summer Camp Enrollment Dashboard")
    st.markdown("---") # Visual separator

# --- 3. MAIN APP FUNCTION ---
def main():
    render_header()
    
    # Create the three tabs
    tab1, tab2, tab3 = st.tabs(["🚀 How it Works", "📈 Analysis & KPIs", "🗺️ Choropleth Map"])

    # Render content in each tab using modular functions
    with tab1:
        render_info()
    
    with tab2:
        render_analysis()
        
    with tab3:
        render_map()

if __name__ == "__main__":
    main()
