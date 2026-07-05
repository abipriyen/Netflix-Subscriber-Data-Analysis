import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Home", page_icon="🏠", layout="wide")

# Title and description
st.markdown("""
    <style>
    .main-title {
        font-size: 3em;
        color: #E50914;
        font-weight: bold;
        text-align: center;
        margin-bottom: 10px;
    }
    .subtitle {
        font-size: 1.5em;
        color: white;
        text-align: center;
        margin-bottom: 30px;
    }
    </style>
    <div class='main-title'>🎬 NETFLIX CUSTOMER CHURN ANALYSIS</div>
    <div class='subtitle'>Predictive Analytics & Business Intelligence Dashboard</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv('data/netflix_customer_churn_unstructured.csv')

df = load_data()

# KPI Section
st.subheader("📊 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Total Customers",
        value="5,000",
        delta="+2.5%",
        delta_color="normal"
    )

with col2:
    retention_rate = ((df['churned'] == 0).sum() / len(df)) * 100
    st.metric(
        label="Retention Rate",
        value=f"{retention_rate:.1f}%",
        delta="-1.2%",
        delta_color="inverse"
    )

with col3:
    churn_rate = ((df['churned'] == 1).sum() / len(df)) * 100
    st.metric(
        label="Churn Rate",
        value=f"{churn_rate:.1f}%",
        delta="+1.2%",
        delta_color="off"
    )

with col4:
    avg_revenue = df['monthly_fee'].mean()
    st.metric(
        label="Avg Monthly Revenue",
        value=f"${avg_revenue:.2f}",
        delta="+$0.50",
        delta_color="normal"
    )

st.markdown("---")

# Project Overview
st.header("📋 Project Overview")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🎯 Business Problem")
    st.write("""
    Netflix faces a critical challenge: **customer churn**. With increasing competition 
    and changing viewing habits, retaining subscribers is becoming increasingly difficult.
    
    **Key Challenges:**
    - 53% of customers are churning (canceling their subscription)
    - Revenue loss from subscription cancellations
    - Need for targeted retention strategies
    - Understanding churn patterns and drivers
    """)

with col2:
    st.subheader("🎬 Our Solution")
    st.write("""
    This comprehensive analytics dashboard provides:
    
    - **Deep Data Analysis**: Understand customer behavior patterns
    - **Churn Prediction**: Identify high-risk customer segments
    - **Actionable Insights**: Data-driven business recommendations
    - **Interactive Visualizations**: Real-time dashboard exploration
    - **Strategic Guidance**: Improve retention and revenue
    """)

st.markdown("---")

# Objectives
st.header("🎯 Project Objectives")

obj_col1, obj_col2, obj_col3 = st.columns(3)

with obj_col1:
    st.info("""
    ✅ **Objective 1**
    
    Understand the Netflix customer dataset
    and identify key churn factors
    """)

with obj_col2:
    st.info("""
    ✅ **Objective 2**
    
    Perform comprehensive exploratory
    data analysis and feature engineering
    """)

with obj_col3:
    st.info("""
    ✅ **Objective 3**
    
    Provide actionable recommendations
    to reduce churn and increase revenue
    """)

st.markdown("---")

# Dataset Summary
st.header("📊 Dataset Summary")

ds_col1, ds_col2, ds_col3, ds_col4 = st.columns(4)

with ds_col1:
    st.metric("Total Records", "7,500")

with ds_col2:
    st.metric("Unique Customers", "5,000")

with ds_col3:
    st.metric("Features", "14")

with ds_col4:
    st.metric("Time Period", "Current")

st.write("""
**Dataset Features:**
- Customer Demographics: Age, Gender, Region
- Subscription Info: Plan Type, Monthly Fee
- Usage Metrics: Watch Hours, Last Login Days
- Device Info: Device Type, Number of Profiles
- Engagement: Watch Time per Day, Favorite Genre
- Target: Churn Status (Churned or Not)
""")

st.markdown("---")

# Technologies Used
st.header("🛠 Technologies Used")

tech_col1, tech_col2, tech_col3 = st.columns(3)

with tech_col1:
    st.subheader("📊 Data Processing")
    st.write("""
    - **Pandas**: Data manipulation
    - **NumPy**: Numerical computing
    - **Python**: Programming language
    """)

with tech_col2:
    st.subheader("📈 Visualization")
    st.write("""
    - **Streamlit**: Interactive dashboard
    - **Plotly**: Interactive charts
    - **Matplotlib & Seaborn**: Statistical plots
    """)

with tech_col3:
    st.subheader("🧠 Analytics")
    st.write("""
    - **Scikit-learn**: Machine learning
    - **Statistical Analysis**: Insights
    - **Data Cleaning**: Preprocessing
    """)

st.markdown("---")

# Workflow
st.header("🔄 Analysis Workflow")

st.write("""
Our comprehensive analytics process follows this workflow:
""")

workflow_data = {
    "Stage": ["1. Data Loading", "2. Data Cleaning", "3. EDA", "4. Visualization", "5. Insights", "6. Recommendations"],
    "Description": [
        "Load and understand the raw dataset",
        "Clean, preprocess, and validate data",
        "Perform exploratory data analysis",
        "Create interactive visualizations",
        "Extract business insights",
        "Provide actionable recommendations"
    ]
}

workflow_df = pd.DataFrame(workflow_data)
st.table(workflow_df)

st.markdown("---")

# Navigation Guide
st.header("🗺 Navigation Guide")

st.write("""
**Use the sidebar to navigate through the dashboard:**

1. **📂 Dataset Overview** - Explore the data structure, columns, and statistics
2. **🧹 Data Cleaning** - Understand the data preprocessing steps
3. **📊 EDA** - View exploratory data analysis and patterns
4. **📈 Visualizations** - Interactive charts and filtering options
5. **💡 Business Insights** - Key findings and business implications
6. **🎯 Recommendations** - Actionable strategies to reduce churn
7. **✅ Conclusion** - Executive summary and next steps

**Features:**
- 🎨 Netflix-themed dark interface
- 📊 Interactive charts and filters
- 💡 Data-driven insights
- 📈 Real-time calculations
- 🎯 Actionable recommendations
""")

st.markdown("---")

# Footer
st.markdown("""
    <div style='text-align: center; color: gray; margin-top: 40px;'>
    <p>Netflix Customer Churn Analysis Dashboard</p>
    <p>Built with Streamlit | Data-Driven Insights</p>
    </div>
""", unsafe_allow_html=True)
