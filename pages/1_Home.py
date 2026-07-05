import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Home", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5em;
        color: #e50914;
        font-weight: 700;
        margin: 0.5rem 0;
    }
    .sub-header {
        font-size: 1.2em;
        color: #666666;
        margin-bottom: 2rem;
    }
    .kpi-card {
        background: linear-gradient(135deg, #f5f5f5 0%, #ffffff 100%);
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 4px solid #e50914;
        text-align: center;
    }
    .kpi-value {
        font-size: 2em;
        font-weight: 700;
        color: #1f1f1f;
        margin: 0.5rem 0;
    }
    .kpi-label {
        font-size: 0.9em;
        color: #666666;
    }
    .objective-box {
        background-color: #f9f9f9;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
        border-left: 4px solid #e50914;
    }
    </style>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    return pd.read_csv('data/netflix_customer_churn_unstructured.csv')

df = load_data()

# Title
st.markdown('<div class="main-header">NETFLIX CUSTOMER CHURN ANALYSIS</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Data-Driven Analytics Dashboard for Customer Retention</div>', unsafe_allow_html=True)

st.markdown("---")

# KPI Section
st.subheader("Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="kpi-card">
    <div class="kpi-label">Total Customers</div>
    <div class="kpi-value">5,000</div>
    <div class="kpi-label" style="color: #27ae60;">Active Records</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    retention_rate = ((df['churned'] == 0).sum() / len(df)) * 100
    st.markdown(f"""
    <div class="kpi-card">
    <div class="kpi-label">Retention Rate</div>
    <div class="kpi-value">{retention_rate:.1f}%</div>
    <div class="kpi-label" style="color: #27ae60;">Active Subscribers</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    churn_rate = ((df['churned'] == 1).sum() / len(df)) * 100
    st.markdown(f"""
    <div class="kpi-card">
    <div class="kpi-label">Churn Rate</div>
    <div class="kpi-value">{churn_rate:.1f}%</div>
    <div class="kpi-label" style="color: #e50914;">Cancelled</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    avg_revenue = df['monthly_fee'].mean()
    st.markdown(f"""
    <div class="kpi-card">
    <div class="kpi-label">Avg Revenue</div>
    <div class="kpi-value">${avg_revenue:.2f}</div>
    <div class="kpi-label" style="color: #27ae60;">Per Month</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Business Problem & Solution
st.subheader("Project Overview")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="objective-box">
    <h4 style="color: #e50914; margin-top: 0;">Business Challenge</h4>
    <p>Netflix faces significant customer churn with over 50% of subscribers cancelling their subscriptions. This dashboard analyzes customer behavior patterns to identify high-risk segments and provide actionable retention strategies.</p>
    <ul>
    <li>High subscriber churn rate affecting revenue</li>
    <li>Need to identify at-risk customers</li>
    <li>Require data-driven retention strategies</li>
    <li>Optimize subscription offerings</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="objective-box" style="border-left-color: #27ae60;">
    <h4 style="color: #27ae60; margin-top: 0;">Solution Approach</h4>
    <p>Comprehensive analytics platform providing deep insights into customer churn drivers and actionable recommendations for revenue optimization.</p>
    <ul>
    <li>Complete data exploration and cleaning</li>
    <li>Interactive visualizations for pattern discovery</li>
    <li>Segment analysis and profiling</li>
    <li>Strategic recommendations for retention</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Project Objectives
st.subheader("Project Objectives")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="objective-box">
    <h5 style="color: #e50914; margin-top: 0;">Objective 1</h5>
    <p>Understand the Netflix customer dataset and identify key churn drivers through comprehensive exploratory analysis.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="objective-box">
    <h5 style="color: #e50914; margin-top: 0;">Objective 2</h5>
    <p>Perform data cleaning, transformation, and feature engineering to prepare analysis-ready data.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="objective-box">
    <h5 style="color: #e50914; margin-top: 0;">Objective 3</h5>
    <p>Provide actionable business recommendations to reduce churn and increase customer lifetime value.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Dataset Summary
st.subheader("Dataset Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Records", "7,500")
with col2:
    st.metric("Unique Customers", "5,000")
with col3:
    st.metric("Features", "14")
with col4:
    st.metric("Data Points", "70,000+")

st.markdown("""
The dataset contains comprehensive customer information including:
- **Demographics**: Age, Gender, Geographic Region
- **Subscription**: Plan Type, Monthly Fee, Payment Method
- **Usage**: Watch Hours, Login Frequency, Watch Time per Day
- **Preferences**: Device Type, Favorite Genre, Number of Profiles
- **Target**: Churn Status (Active or Cancelled)
""")

st.markdown("---")

# Technologies
st.subheader("Technology Stack")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    **Data Processing**
    - Pandas for data manipulation
    - NumPy for numerical computing
    - Python 3.8+
    """)

with col2:
    st.markdown("""
    **Visualization**
    - Streamlit for dashboard
    - Plotly for interactive charts
    - Matplotlib & Seaborn for analysis
    """)

with col3:
    st.markdown("""
    **Analytics**
    - Scikit-learn for ML
    - Statistical analysis tools
    - Data validation frameworks
    """)

st.markdown("---")

# Workflow
st.subheader("Analysis Workflow")

workflow_steps = [
    ("1", "Data Loading", "Load and explore raw dataset"),
    ("2", "Data Cleaning", "Remove duplicates, handle missing values"),
    ("3", "Transformation", "Feature engineering and encoding"),
    ("4", "Visualization", "Create interactive charts and dashboards"),
    ("5", "Analysis", "Extract insights and patterns"),
    ("6", "Recommendations", "Provide actionable business strategies")
]

for step, title, desc in workflow_steps:
    col1, col2, col3 = st.columns([1, 2, 5])
    with col1:
        st.markdown(f"<div style='background-color: #e50914; color: white; padding: 0.5rem; border-radius: 50%; text-align: center; font-weight: bold;'>{step}</div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"**{title}**")
    with col3:
        st.markdown(f"{desc}")

st.markdown("---")

# Footer
st.markdown("""
<div style='text-align: center; color: #999999; font-size: 12px; padding: 2rem 0;'>
<p>Netflix Customer Churn Analysis Dashboard</p>
<p>Professional Data Analytics & Business Intelligence</p>
</div>
""", unsafe_allow_html=True)
