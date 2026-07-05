import streamlit as st
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Netflix Churn Analysis",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        background-color: #1a1a1a;
    }
    </style>
""", unsafe_allow_html=True)

# Cache data loading
@st.cache_data
def load_data():
    df = pd.read_csv('data/netflix_customer_churn_unstructured.csv')
    return df

# Main app title
st.sidebar.markdown("<h1 style='text-align: center; color: #E50914;'>🎬 Netflix Churn</h1>", unsafe_allow_html=True)
st.sidebar.markdown("---")

# Navigation info
st.sidebar.info(
    "**Navigate through the dashboard using the menu on the left.**\n\n"
    "🏠 **Home** - Project overview\n\n"
    "📂 **Dataset Overview** - Data structure\n\n"
    "🧹 **Data Cleaning** - Preprocessing steps\n\n"
    "📊 **EDA** - Exploratory analysis\n\n"
    "📈 **Visualizations** - Interactive charts\n\n"
    "💡 **Business Insights** - Key findings\n\n"
    "🎯 **Recommendations** - Action items\n\n"
    "✅ **Conclusion** - Summary"
)

st.sidebar.markdown("---")
st.sidebar.markdown("<p style='text-align: center; color: gray;'>Netflix Churn Analysis Dashboard v1.0</p>", unsafe_allow_html=True)
