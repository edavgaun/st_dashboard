import streamlit as st
import pandas as pd
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from code.tab_info import set_layout, render_info, show_header
from code.tab_analysis import render_analysis
from code.tab_map import render_map

@st.cache_data
def load_and_cache_data(file_path):
    """
    Loads the main data file and caches the result globally.
    """
    try:
        # Check if the file exists before attempting to read
        if not os.path.exists(file_path):
            st.error(f"Data file not found at: {file_path}")
            return pd.DataFrame() # Return an empty DataFrame on failure
        # Load the CSV file
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        st.error(f"An error occurred while loading data: {e}")
        return pd.DataFrame()

df=load_and_cache_data('data/data.csv')

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
        render_analysis(df)
        
    with tab3:
        render_map()

if __name__ == "__main__":
    main()
