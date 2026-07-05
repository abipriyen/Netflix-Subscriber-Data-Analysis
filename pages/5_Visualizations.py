import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Visualizations", layout="wide")

st.subheader("Interactive Visualizations Dashboard")
st.write("Explore customer churn patterns through interactive charts and filters.")

# Load and transform data
@st.cache_data
def load_data():
    df = pd.read_csv('data/netflix_customer_churn_unstructured.csv')
    
    df = df.sort_values(by='customer_id')
    df = df.reset_index(drop=True)
    df = df[~df['customer_id'].duplicated(keep='first')]
    
    region_mapping = {
        'N/A': 'Unknown', '???': 'Unknown', '###': 'Unknown',
        'error': 'Unknown', 'invalid': 'Unknown', 'unknown': 'Unknown'
    }
    df['region'] = df['region'].fillna('Unknown').replace(region_mapping)
    
    columns_to_drop = ['Random_Text', 'Unused_Code', 'Extra_Column', 'Fake_Status']
    df = df.drop(columns=columns_to_drop, errors='ignore')
    
    df['age_group'] = pd.cut(df['age'], bins=[0, 18, 25, 35, 50, 100],
                            labels=['<18', '18-25', '26-35', '36-50', '50+'])
    
    df['engagement_level'] = pd.cut(df['watch_hours'], bins=[0, 5, 15, 30, 100],
                                   labels=['Low', 'Medium', 'High', 'Very High'])
    
    df['churn_status'] = df['churned'].map({0: 'Active', 1: 'Churned'})
    
    return df

df = load_data()

st.markdown("---")

# Sidebar Filters
st.sidebar.subheader("Filter Options")

selected_subscription = st.sidebar.multiselect(
    "Subscription Type",
    options=df['subscription_type'].unique(),
    default=df['subscription_type'].unique()
)

selected_region = st.sidebar.multiselect(
    "Region",
    options=df['region'].unique(),
    default=df['region'].unique()[:5]
)

selected_device = st.sidebar.multiselect(
    "Device Type",
    options=df['device'].unique(),
    default=df['device'].unique()
)

# Apply filters
df_filtered = df[
    (df['subscription_type'].isin(selected_subscription)) &
    (df['region'].isin(selected_region)) &
    (df['device'].isin(selected_device))
]

st.info(f"Showing {len(df_filtered):,} records out of {len(df):,} total")

st.markdown("---")

# Row 1: Key Metrics
st.subheader("Key Metrics")

metrics_cols = st.columns(4)

with metrics_cols[0]:
    st.metric("Total Customers", f"{len(df_filtered):,}")

with metrics_cols[1]:
    active_count = (df_filtered['churned'] == 0).sum()
    st.metric("Active Customers", f"{active_count:,}")

with metrics_cols[2]:
    churn_count = (df_filtered['churned'] == 1).sum()
    st.metric("Churned Customers", f"{churn_count:,}")

with metrics_cols[3]:
    churn_pct = (churn_count / len(df_filtered) * 100) if len(df_filtered) > 0 else 0
    st.metric("Churn Rate", f"{churn_pct:.1f}%")

st.markdown("---")

# Visualizations
st.subheader("Churn Distribution")

col1, col2 = st.columns(2)

with col1:
    churn_counts = df_filtered['churn_status'].value_counts()
    fig1 = px.pie(
        values=churn_counts.values,
        names=churn_counts.index,
        title="Customer Status Distribution",
        color_discrete_map={'Active': '#27ae60', 'Churned': '#e50914'}
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    churn_by_sub = df_filtered.groupby('subscription_type')['churned'].agg(['sum', 'count'])
    churn_by_sub['churn_rate'] = (churn_by_sub['sum'] / churn_by_sub['count'] * 100)
    
    fig2 = px.bar(
        churn_by_sub.reset_index(),
        x='subscription_type',
        y='churn_rate',
        title="Churn Rate by Subscription Type",
        labels={'subscription_type': 'Subscription Type', 'churn_rate': 'Churn Rate (%)'},
        color='churn_rate',
        color_continuous_scale='Reds'
    )
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

st.subheader("Customer Demographics")

col1, col2 = st.columns(2)

with col1:
    age_churn = df_filtered.groupby('age_group')['churned'].agg(['sum', 'count'])
    age_churn['churn_rate'] = (age_churn['sum'] / age_churn['count'] * 100)
    
    fig3 = px.bar(
        age_churn.reset_index(),
        x='age_group',
        y='churn_rate',
        title="Churn Rate by Age Group",
        labels={'age_group': 'Age Group', 'churn_rate': 'Churn Rate (%)'},
        color='churn_rate',
        color_continuous_scale='RdYlGn_r'
    )
    st.plotly_chart(fig3, use_container_width=True)

with col2:
    gender_churn = df_filtered.groupby('gender')['churned'].agg(['sum', 'count'])
    gender_churn['churn_rate'] = (gender_churn['sum'] / gender_churn['count'] * 100)
    
    fig4 = px.bar(
        gender_churn.reset_index(),
        x='gender',
        y='churn_rate',
        title="Churn Rate by Gender",
        labels={'gender': 'Gender', 'churn_rate': 'Churn Rate (%)'},
        color='churn_rate',
        color_continuous_scale='Blues'
    )
    st.plotly_chart(fig4, use_container_width=True)

st.markdown("---")

st.subheader("Usage Patterns")

col1, col2 = st.columns(2)

with col1:
    fig5 = px.histogram(
        df_filtered,
        x='watch_hours',
        color='churn_status',
        title="Watch Hours Distribution by Churn Status",
        labels={'watch_hours': 'Monthly Watch Hours', 'count': 'Number of Customers'},
        color_discrete_map={'Active': '#27ae60', 'Churned': '#e50914'},
        nbins=30
    )
    st.plotly_chart(fig5, use_container_width=True)

with col2:
    fig6 = px.histogram(
        df_filtered,
        x='last_login_days',
        color='churn_status',
        title="Days Since Last Login Distribution",
        labels={'last_login_days': 'Days Since Last Login', 'count': 'Number of Customers'},
        color_discrete_map={'Active': '#27ae60', 'Churned': '#e50914'},
        nbins=30
    )
    st.plotly_chart(fig6, use_container_width=True)

st.markdown("---")

st.subheader("Device and Payment Analysis")

col1, col2 = st.columns(2)

with col1:
    device_churn = df_filtered.groupby('device')['churned'].agg(['sum', 'count'])
    device_churn['churn_rate'] = (device_churn['sum'] / device_churn['count'] * 100)
    
    fig7 = px.bar(
        device_churn.reset_index(),
        x='device',
        y='churn_rate',
        title="Churn Rate by Device Type",
        labels={'device': 'Device', 'churn_rate': 'Churn Rate (%)'},
        color='churn_rate',
        color_continuous_scale='Purples'
    )
    st.plotly_chart(fig7, use_container_width=True)

with col2:
    payment_churn = df_filtered.groupby('payment_method')['churned'].agg(['sum', 'count'])
    payment_churn['churn_rate'] = (payment_churn['sum'] / payment_churn['count'] * 100)
    
    fig8 = px.bar(
        payment_churn.reset_index(),
        x='payment_method',
        y='churn_rate',
        title="Churn Rate by Payment Method",
        labels={'payment_method': 'Payment Method', 'churn_rate': 'Churn Rate (%)'},
        color='churn_rate',
        color_continuous_scale='Oranges'
    )
    st.plotly_chart(fig8, use_container_width=True)

st.markdown("---")

st.subheader("Revenue Analysis")

col1, col2 = st.columns(2)

with col1:
    revenue_by_sub = df_filtered.groupby('subscription_type')['monthly_fee'].sum()
    
    fig9 = px.pie(
        values=revenue_by_sub.values,
        names=revenue_by_sub.index,
        title="Monthly Revenue by Subscription Type"
    )
    st.plotly_chart(fig9, use_container_width=True)

with col2:
    avg_revenue = df_filtered.groupby('subscription_type')['monthly_fee'].mean()
    
    fig10 = px.bar(
        x=avg_revenue.index,
        y=avg_revenue.values,
        title="Average Monthly Revenue per Subscription",
        labels={'x': 'Subscription Type', 'y': 'Average Monthly Fee ($)'},
        text=avg_revenue.values
    )
    fig10.update_traces(texttemplate='$%{text:.2f}', textposition='outside')
    st.plotly_chart(fig10, use_container_width=True)
