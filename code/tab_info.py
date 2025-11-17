import streamlit as st

def set_layout():
    st.set_page_config(layout="wide")
    st.markdown("""
        <style>
            .block-container {
                padding-top: 4rem;
                padding-bottom: 1rem;
                padding-left: 2rem;
                padding-right: 2rem;
            }
            .css-18e3th9 {
                padding-top: 0rem !important;
            }
        </style>
    """, unsafe_allow_html=True)

def render_info():
    """Renders the content for the 'How it Works' tab."""
    st.header("Dashboard Guide: Understanding the Data")
    
    st.markdown("""
    This dashboard visualizes enrollment trends and geographic distribution for the RCEL Summer Elite Camp 2025.
    
    ### 📝 Sections:
    * **How it Works:** (You are here!) Provides context and data definitions.
    * **Analysis & KPIs:** Displays key performance indicators (KPIs) on enrollment rate, using three detailed charts that change with time.
    * **Choropleth Map:** Shows the geographical origin of our campers by state or region.
    
    ### ⚙️ Data Source:
    Data was kindly shared by the RCEL Office for this workshop.
    """)

def show_header():
    """
    Renders the consistent header with the logo on the left (small) 
    and the title/caption structure on the right (wide), using the required function name.
    """
    
    # Define columns: [Logo Column (1), Title/Caption Column (5)]
    # This ensures the logo is small and the title has the majority of the space.
    col1, col2 = st.columns([1, 5])
    
    # --- Column 1: Logo ---
    with col1:
        st.image(
            "utils/ELITE-TECH-logo.2022-logoweb.png",
            width=200,  # Explicitly set a small width for your large image
        )
        
    # --- Column 2: Title and Caption ---
    with col2:
        # Title as the main heading
        st.title("📊 RCEL Summer Camp Enrollment Dashboard")
        
        # Caption with attribution details
        st.caption("📘 Made by: Edgar Avalos-Gauna (2025), RCEL 506")
    
    # --- Separator ---
    st.markdown("---")
