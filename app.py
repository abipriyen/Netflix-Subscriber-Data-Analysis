import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Netflix Churn Analysis Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional CSS styling
st.markdown("""
    <style>
    * {
        margin: 0;
        padding: 0;
    }
    
    [data-testid="stSidebar"] {
        background-color: #f5f5f5;
    }
    
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
        color: #1f1f1f;
    }
    
    [data-testid="stMainBlockContainer"] {
        padding: 2rem 3rem;
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: #1f1f1f;
        font-weight: 600;
    }
    
    .stMetric {
        background-color: #f9f9f9;
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 4px solid #e50914;
    }
    
    .metric-label {
        color: #666666;
        font-size: 14px;
    }
    
    .metric-value {
        color: #1f1f1f;
        font-size: 24px;
        font-weight: 600;
    }
    
    .info-card {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 4px solid #e50914;
        margin: 1rem 0;
    }
    
    .success-card {
        background-color: #f0f8f4;
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 4px solid #27ae60;
    }
    
    .warning-card {
        background-color: #fef5e7;
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 4px solid #f39c12;
    }
    
    .dataframe {
        font-size: 14px;
    }
    
    .stTabs [data-baseweb="tab-list"] button {
        color: #1f1f1f;
    }
    
    .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {
        border-bottom-color: #e50914;
        color: #e50914;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar configuration
st.sidebar.markdown("""
    <div style='text-align: center; padding: 2rem 0;'>
    <h2 style='color: #e50914; margin: 0;'>NETFLIX CHURN</h2>
    <p style='color: #666666; margin: 0.5rem 0 0 0;'>Analysis Dashboard</p>
    </div>
    <hr style='margin: 2rem 0;'>
""", unsafe_allow_html=True)

# Cache data loading
@st.cache_data
def load_data():
    try:
        df = pd.read_csv('data/netflix_customer_churn_unstructured.csv')
        return df
    except FileNotFoundError:
        st.error("Data file not found. Please ensure 'netflix_customer_churn_unstructured.csv' exists in the 'data' folder.")
        return None

# Navigation info
st.sidebar.markdown("""
<div style='background-color: #f9f9f9; padding: 1rem; border-radius: 8px; border-left: 4px solid #e50914;'>
<p style='color: #1f1f1f; font-weight: 600; margin: 0 0 0.5rem 0;'>Dashboard Pages</p>
<ul style='color: #666666; margin-left: 1.5rem;'>
<li>Home - Project Overview</li>
<li>Dataset Overview - Data Structure</li>
<li>Data Cleaning - Preprocessing Steps</li>
<li>Data Transformation - Feature Engineering</li>
<li>Visualizations - Interactive Charts</li>
<li>Business Insights - Key Findings</li>
<li>Recommendations - Action Items</li>
<li>Conclusion - Summary</li>
</ul>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.markdown("""
<p style='text-align: center; color: #999999; font-size: 12px; margin-top: 2rem;'>
Netflix Churn Analysis Dashboard v1.0<br>
Built with Streamlit
</p>
""", unsafe_allow_html=True)
