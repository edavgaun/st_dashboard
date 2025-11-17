import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px
import streamlit as st

def create_stacked_bar_plot(df):
    value_vars = ['w1', 'w2', 'w3', 'w4']
    
    # Melt the DataFrame
    df=df.sort_values(['tod', 'workshop'])
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
    fig.update_yaxes(
        autorange="reversed"
    )
    return fig

def create_enrollment_timeline_plot(df):
    fig = px.line(
        df,
        x='date',            # X-axis: Time (Date)
        y='total',           # Y-axis: Enrollment Count
        color='workshop',    # Lines grouped and colored by Workshop
        title='Workshop Enrollment Trend Over Time',
        labels={'total': 'Total Enrollment (Headcount)', 'date': 'Date'},
        height=500
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Total Enrollment",
        legend_title_text='Workshop',
        hovermode="x unified"
    )
    
    fig.update_xaxes(
        dtick="M1", # Show one tick per month
        tickformat="%b %d" # Format as Month Abbreviation and Day (e.g., Feb 28)
    )

    return fig

def student_commute_plot(df_long_data, selected_date):
    """
    Creates a Dumbbell/Dot plot showing Commuter vs. Residential enrollment per week.
    
    Args:
        df_long_data (pd.DataFrame): The pre-processed data (st_long).
        selected_date (str): The selected date string from the Streamlit slider.
    """
    # 1. Filter data based on the selected date
    # Note: Use str comparison here as the input is a string
    db = df_long_data[df_long_data['date'] == selected_date]
    
    # 2. Define Plot Parameters
    s_palette = {'Residential': 'Green', 'Commuter': 'Red'}
    
    # Calculate Axis Limits using the entire dataset for consistency
    xmax = (df_long_data['count'].max() // 10 + 1) * 10
    xmin = (df_long_data['count'].min() // 10 - 1) * 10

    fig, axs = plt.subplots(figsize=(5, 2.5))

    # 3. Draw Connecting Lines and Week Labels
    for w in range(5):
        # Draw the dotted line
        sns.lineplot(data=db[db['weeks'] == w], x='count', y=w,
                     color="Black", ax=axs, lw=1, ls=":")
        
        # Add week label text
        if w < 4:
            axs.text(xmin, w + 1, "Week {}:".format(w + 1), va="center")

    # 4. Draw Scatter Plot (The Dots)
    sns.scatterplot(data=db, x='count', y="weeks",
                    hue="stype", size='count',
                    palette=s_palette,
                    sizes=(20, 200), ax=axs)

    # 5. Add Value Labels (v and vmax/vmin logic)
    for i in range(4):
        db_w = db[db['weeks'] == i + 1]
        if db_w.empty:
            continue
            
        vals = db_w['count'].values
        vmin, vmax = min(vals), max(vals)
        
        for v in vals:
            # Determine alignment based on min/max for placement
            d = 0 # Default offset
            align = 'center'
            
            if v == vmin:
                d = -1
                align = 'right'
            if v == vmax:
                d = 1
                align = 'left'

            # Get the correct color for the text
            stype_color = s_palette[db_w[db_w['count'] == v]['stype'].iloc[0]]
            
            axs.text(v + d, i + 1, v, color=stype_color,
                     va='center', fontweight="bold", ha=align)

    # 6. Final Axis Cleanup and Legend
    axs.set_xlim(xmin, xmax)
    plt.axis('off')
    axs.invert_yaxis() # Invert Y-axis so Week 1 is on top

    # Customize Title and Legend Placement
    plt.title("Weekly Attendance (Headcount) for RCEL Campers:", x=0.1, y=1.2)
    
    # Manually get handles/labels to remove the 'size' legend entries
    handles, labels = axs.get_legend_handles_labels()
    keep = ["Residential", "Commuter"]
    new_handles = [h for h, l in zip(handles, labels) if l in keep]
    new_labels = [l for l in labels if l in keep]

    # Use coordinates relative to the plot area for Bbox
    plt.legend(new_handles, new_labels, ncols=2, loc='upper left', 
               bbox_to_anchor=(0.2, 1.12), frameon=False)
               
    plt.tight_layout(pad=3) # Add padding to prevent cutoffs

    return fig
