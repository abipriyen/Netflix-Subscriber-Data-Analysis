import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Dataset Overview", layout="wide")

st.subheader("Dataset Overview")
st.write("Understanding the structure, composition, and quality of the Netflix customer churn dataset.")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv('data/netflix_customer_churn_unstructured.csv')

df = load_data()

st.markdown("---")

# Dataset Dimensions
st.subheader("Dataset Dimensions")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Rows", f"{len(df):,}")
with col2:
    st.metric("Total Columns", df.shape[1])
with col3:
    st.metric("Memory Usage", f"{df.memory_usage(deep=True).sum() / 1024:.2f} KB")

st.markdown("---")

# Column Information
st.subheader("Column Information")

col_info = pd.DataFrame({
    "Column Name": df.columns,
    "Data Type": df.dtypes.astype(str),
    "Non-Null Count": df.count(),
    "Missing Values": df.isnull().sum(),
    "Missing %": (df.isnull().sum() / len(df) * 100).round(2)
})

st.dataframe(col_info, use_container_width=True, hide_index=True)

st.markdown("---")

# Dataset Preview
st.subheader("Data Preview")

show_rows = st.slider("Number of rows to display:", 5, 50, 10)
st.dataframe(df.head(show_rows), use_container_width=True, hide_index=True)

st.markdown("---")

# Numerical Features
st.subheader("Numerical Features Analysis")

numerical_cols = df.select_dtypes(include=[np.number]).columns.tolist()
st.write(f"**Total Numerical Features**: {len(numerical_cols)}")

if numerical_cols:
    stats_df = df[numerical_cols].describe().round(2).T
    st.dataframe(stats_df, use_container_width=True)

st.markdown("---")

# Categorical Features
st.subheader("Categorical Features Analysis")

categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
st.write(f"**Total Categorical Features**: {len(categorical_cols)}")

for col in categorical_cols:
    with st.expander(f"{col} ({df[col].nunique()} unique values)"):
        value_counts = df[col].value_counts()
        col1, col2 = st.columns(2)
        with col1:
            st.dataframe(value_counts, use_container_width=True)
        with col2:
            st.bar_chart(value_counts.head(10))

st.markdown("---")

# Missing Values
st.subheader("Missing Values Analysis")

missing = df.isnull().sum()
missing_pct = (missing / len(df) * 100)

missing_df = pd.DataFrame({
    "Column": missing.index,
    "Missing Count": missing.values,
    "Missing %": missing_pct.values
}).sort_values('Missing Count', ascending=False)

missing_df = missing_df[missing_df['Missing Count'] > 0]

if len(missing_df) > 0:
    st.dataframe(missing_df, use_container_width=True, hide_index=True)
else:
    st.success("No missing values found in the dataset.")

st.markdown("---")

# Duplicates
st.subheader("Duplicate Records")

total_dup = df.duplicated().sum()
cust_dup = df['customer_id'].duplicated().sum()

col1, col2 = st.columns(2)
with col1:
    st.metric("Total Duplicate Rows", total_dup)
with col2:
    st.metric("Duplicate Customer IDs", cust_dup)

if total_dup > 0:
    st.warning(f"Found {total_dup} duplicate records ({total_dup/len(df)*100:.2f}%) that need to be removed.")

st.markdown("---")

# Statistical Summary
st.subheader("Statistical Summary")

st.dataframe(df.describe().round(2).T, use_container_width=True)

st.markdown("---")

# Data Quality Report
st.subheader("Data Quality Assessment")

quality_cols = st.columns(4)

with quality_cols[0]:
    completeness = 100 - (df.isnull().sum().sum() / (df.shape[0] * df.shape[1]) * 100)
    st.metric("Completeness", f"{completeness:.1f}%")

with quality_cols[1]:
    st.metric("Unique Customers", df['customer_id'].nunique())

with quality_cols[2]:
    st.metric("Churn Rate", f"{(df['churned'].sum()/len(df)*100):.1f}%")

with quality_cols[3]:
    st.metric("Average Age", f"{df['age'].mean():.1f}")

st.markdown("---")

# Key Insights
st.subheader("Key Dataset Insights")

insights = f"""
- Dataset contains {len(df):,} customer records across {df.shape[1]} features
- Primary key: customer_id with {df['customer_id'].nunique()} unique customers
- Missing values detected in: {', '.join(missing_df[missing_df['Missing Count'] > 0]['Column'].tolist()) if len(missing_df) > 0 else 'None'}
- Duplicate records: {total_dup} ({total_dup/len(df)*100:.2f}%)
- Age range: {df['age'].min()} to {df['age'].max()} years
- Monthly fees: ${df['monthly_fee'].min():.2f} to ${df['monthly_fee'].max():.2f}
- Watch hours: {df['watch_hours'].min():.2f} to {df['watch_hours'].max():.2f} hours/month
- Subscription types: {', '.join(df['subscription_type'].unique())}
"""

st.info(insights)
