import pandas as pd
import plotly.express as px
import streamlit as st

def create_stacked_bar_plot(df):
    value_vars = ['w1', 'w2', 'w3', 'w4']
    
    # Melt the DataFrame
    df_long = df.melt(
        id_vars=['workshop'],
        value_vars=value_vars,
        var_name='Week',
        value_name='Attendance'
    )

    # --- 3. Create the Plotly Horizontal Stacked Bar Chart ---
    fig = px.bar(
        df_long,
        x='Attendance',      # X-axis: The value (the length of the bar)
        y='workshop',        # Y-axis: The categories (the workshops)
        color='Week',        # Color/Stacking Group: W1, W2, W3, W4
        orientation='h',     # Make it horizontal
        title='Weekly Enrollment Composition by Workshop',
        labels={'Attendance': 'Total Weekly Headcount', 'Workshop': 'Program Name'},
        height=500
    )

    # Optional: Customize layout for better readability
    fig.update_layout(
        legend_title_text='Week',
        xaxis_title=None,
        yaxis_title=None,
        barmode='stack',  # Ensure bars are stacked
        hovermode="y unified"
    )

    return fig
