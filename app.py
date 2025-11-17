import streamlit as st
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from code.tab_info import set_layout, render_info, show_header
from code.tab_analysis import render_analysis
from code.tab_map import render_map

# --- 1. CONFIGURATION ---
set_layout()

# --- 2. HEADER BANNER (CONSTANT) ---
show_header()

# --- 3. MAIN APP FUNCTION ---
def main():
    
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
