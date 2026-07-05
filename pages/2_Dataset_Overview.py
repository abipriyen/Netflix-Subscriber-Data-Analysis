import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Dataset Overview", page_icon="📂", layout="wide")

st.header("📂 Dataset Overview")
st.write("Understand the structure, columns, and statistics of the Netflix customer churn dataset.")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv('data/netflix_customer_churn_unstructured.csv')

df = load_data()

st.markdown("---")

# Dataset Shape
st.subheader("📊 Dataset Shape")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Rows", f"{len(df):,}")
with col2:
    st.metric("Total Columns", df.shape[1])
with col3:
    st.metric("Data Size", f"{df.memory_usage(deep=True).sum() / 1024:.2f} KB")

st.markdown("---")

# Column Information
st.subheader("📋 Column Information")

col_info = pd.DataFrame({
    "Column Name": df.columns,
    "Data Type": df.dtypes.astype(str),
    "Non-Null Count": df.count(),
    "Missing Values": df.isnull().sum(),
    "Missing %": (df.isnull().sum() / len(df) * 100).round(2)
})

st.dataframe(col_info, use_container_width=True)

st.markdown("---")

# Dataset Preview
st.subheader("👀 Dataset Preview (First 10 Rows)")
st.dataframe(df.head(10), use_container_width=True)

st.markdown("---")

# Numerical Features
st.subheader("🔢 Numerical Features")

numerical_cols = df.select_dtypes(include=[np.number]).columns.tolist()
st.write(f"**Count**: {len(numerical_cols)} numerical features")

if numerical_cols:
    stats_df = df[numerical_cols].describe().T
    st.dataframe(stats_df, use_container_width=True)

st.markdown("---")

# Categorical Features
st.subheader("🏷 Categorical Features")

categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
st.write(f"**Count**: {len(categorical_cols)} categorical features")

for col in categorical_cols:
    st.write(f"**{col}**: {df[col].nunique()} unique values")
    st.write(df[col].value_counts())
    st.write("")

st.markdown("---")

# Missing Values Analysis
st.subheader("⚠️ Missing Values Analysis")

missing = df.isnull().sum()
missing_pct = (missing / len(df) * 100)

missing_df = pd.DataFrame({
    "Column": missing.index,
    "Missing Count": missing.values,
    "Missing %": missing_pct.values
})

missing_df = missing_df[missing_df['Missing Count'] > 0].sort_values('Missing Count', ascending=False)

if len(missing_df) > 0:
    st.dataframe(missing_df, use_container_width=True)
else:
    st.success("✅ No missing values found!")

st.markdown("---")

# Duplicate Records
st.subheader("🔁 Duplicate Records Analysis")

total_duplicates = df.duplicated().sum()
st.write(f"**Total duplicate rows**: {total_duplicates}")
st.write(f"**Duplicate %**: {(total_duplicates/len(df)*100):.2f}%")

if total_duplicates > 0:
    st.warning(f"⚠️ Found {total_duplicates} duplicate records that need to be removed!")
else:
    st.success("✅ No duplicate records found!")

st.markdown("---")

# Statistical Summary
st.subheader("📈 Statistical Summary")

st.write("### Numerical Features Statistics")
st.dataframe(df.describe().T, use_container_width=True)

st.markdown("---")

# Data Quality Report
st.subheader("🔍 Data Quality Report")

col1, col2, col3, col4 = st.columns(4)

with col1:
    quality_score = 100 - (missing_pct.sum())
    st.metric("Data Completeness", f"{quality_score:.1f}%")

with col2:
    st.metric("Unique Customers", df['customer_id'].nunique())

with col3:
    st.metric("Churn Rate", f"{(df['churned'].sum()/len(df)*100):.1f}%")

with col4:
    st.metric("Average Age", f"{df['age'].mean():.1f}")

st.markdown("---")

# Key Insights
st.subheader("💡 Key Dataset Insights")

insights = [
    f"📊 Dataset contains {len(df):,} customer records across {df.shape[1]} features",
    f"🔑 Primary key: customer_id with {df['customer_id'].nunique()} unique customers",
    f"⚠️ Missing values found in: {', '.join(missing_df[missing_df['Missing Count'] > 0]['Column'].tolist()) if len(missing_df) > 0 else 'None'}",
    f"🔁 Duplicate records: {total_duplicates} ({total_duplicates/len(df)*100:.2f}%)",
    f"👥 Age range: {df['age'].min()} to {df['age'].max()} years",
    f"💰 Monthly fees: ${df['monthly_fee'].min():.2f} to ${df['monthly_fee'].max():.2f}",
    f"📺 Watch hours: {df['watch_hours'].min():.2f} to {df['watch_hours'].max():.2f} hours/month"
]

for insight in insights:
    st.write(f"• {insight}")
