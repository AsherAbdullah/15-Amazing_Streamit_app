import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import altair as alt

# Set page configuration
st.set_page_config(
    page_title="Data Visualization Dashboard",
    page_icon="📊",
    layout="wide"
)

# Custom CSS for UV effect
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .stButton>button {
        background: linear-gradient(90deg, #4b6cb7 0%, #182848 100%);
        color: white;
    }
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #2c3e50 0%, #3498db 100%);
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.selectbox(
    "Choose a Page",
    ["Home", "Data Analysis", "Interactive Charts", "UV Index Tracker", "Machine Learning"]
)

# Home Page
if page == "Home":
    st.title("📊 Advanced Data Visualization Dashboard")
    st.write("Welcome to our interactive dashboard! This application demonstrates various Streamlit features with UV-themed visualizations.")
    
    # Create three columns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="Temperature", value="24°C", delta="1.2°C")
    
    with col2:
        st.metric(label="UV Index", value="6.8", delta="-0.5")
    
    with col3:
        st.metric(label="Cloud Cover", value="65%", delta="12%")
    
    # Sample data generation
    dates = pd.date_range(start='2024-01-01', end='2024-03-15', freq='D')
    uv_values = np.random.uniform(0, 12, size=len(dates))
    temp_values = np.random.normal(25, 5, size=len(dates))
    
    df = pd.DataFrame({
        'Date': dates,
        'UV_Index': uv_values,
        'Temperature': temp_values
    })
    
    # Create interactive chart
    fig = px.line(df, x='Date', y=['UV_Index', 'Temperature'],
                  title='UV Index and Temperature Over Time')
    st.plotly_chart(fig, use_container_width=True)

# Data Analysis Page
elif page == "Data Analysis":
    st.title("📈 Data Analysis")
    st.write("Upload your data for analysis")
    
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Data Preview:")
        st.dataframe(df.head())
        
        st.write("Basic Statistics:")
        st.write(df.describe())

# Interactive Charts Page
elif page == "Interactive Charts":
    st.title("🎨 Interactive Charts")
    
    # Generate sample data
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    # Create interactive chart
    chart_data = pd.DataFrame({
        'x': x,
        'sin(x)': y,
        'cos(x)': np.cos(x)
    })
    
    chart_type = st.selectbox("Select Chart Type", ["Line", "Scatter", "Area"])
    
    if chart_type == "Line":
        chart = alt.Chart(chart_data).mark_line().encode(
            x='x',
            y='sin(x)',
            color=alt.value("#00ff00")
        ).interactive()
        st.altair_chart(chart, use_container_width=True)
    
    elif chart_type == "Scatter":
        fig = px.scatter(chart_data, x='x', y='sin(x)', color='cos(x)')
        st.plotly_chart(fig, use_container_width=True)
    
    else:
        fig = px.area(chart_data, x='x', y='sin(x)')
        st.plotly_chart(fig, use_container_width=True)

# UV Index Tracker Page
elif page == "UV Index Tracker":
    st.title("☀️ UV Index Tracker")
    
    # Mock UV index data
    current_uv = np.random.uniform(0, 12)
    
    # UV Index gauge
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = current_uv,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Current UV Index"},
        gauge = {
            'axis': {'range': [None, 12]},
            'steps': [
                {'range': [0, 3], 'color': "lightgreen"},
                {'range': [3, 6], 'color': "yellow"},
                {'range': [6, 8], 'color': "orange"},
                {'range': [8, 11], 'color': "red"},
                {'range': [11, 12], 'color': "purple"}
            ]
        }
    ))
    st.plotly_chart(fig)
    
    # UV protection recommendations
    st.subheader("UV Protection Recommendations")
    if current_uv < 3:
        st.success("Low UV level - Basic sun protection required")
    elif current_uv < 6:
        st.warning("Moderate UV level - Take precautions")
    else:
        st.error("High UV level - Maximum protection required!")

# Machine Learning Page
elif page == "Machine Learning":
    st.title("🤖 Machine Learning Predictions")
    st.write("Simple UV Index Prediction Model")
    
    # Input features
    cloud_cover = st.slider("Cloud Cover (%)", 0, 100, 50)
    time_of_day = st.slider("Hour of Day", 0, 23, 12)
    
    # Mock prediction
    predicted_uv = max(0, min(12, (24 - abs(time_of_day - 12)) * (100 - cloud_cover) / 100))
    
    st.subheader("Predicted UV Index")
    st.write(f"{predicted_uv:.2f}")
    
    # Confidence gauge
    confidence = np.random.uniform(0.7, 0.99)
    st.progress(confidence)
    st.write(f"Prediction Confidence: {confidence:.2%}")
