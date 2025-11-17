import streamlit as st

def render_info():
    """Renders the content for the 'How it Works' tab."""
    st.header("Dashboard Guide: Understanding the Data")
    
    st.markdown("""
    This dashboard visualizes enrollment trends and geographic distribution for the RCEL Summer Elite Camp 2025.
    
    ### 📝 Sections:
    * **How it Works:** (You are here!) Provides context and data definitions.
    * **Analysis & KPIs:** Displays key performance indicators (KPIs) on enrollment rate, and three detailed charts on weekly and program-specific attendance trends.
    * **Choropleth Map:** Shows the geographical origin of our campers by state or region.
    
    ### ⚙️ Data Source:
    Data is aggregated daily from the RCEL enrollment system and represents confirmed student headcounts.
    """)
