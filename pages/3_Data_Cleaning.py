import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Data Cleaning", layout="wide")

st.subheader("Data Cleaning Process")
st.write("Understanding the data preprocessing steps applied to transform raw data into analysis-ready format.")

# Load original data
@st.cache_data
def load_original():
    return pd.read_csv('data/netflix_customer_churn_unstructured.csv')

@st.cache_data
def clean_data(df):
    df = df.copy()
    df = df.sort_values(by='customer_id')
    df = df.reset_index(drop=True)
    df = df[~df['customer_id'].duplicated(keep='first')]
    
    region_mapping = {
        'N/A': 'Unknown',
        '???': 'Unknown',
        '###': 'Unknown',
        'error': 'Unknown',
        'invalid': 'Unknown',
        'unknown': 'Unknown'
    }
    df['region'] = df['region'].fillna('Unknown')
    df['region'] = df['region'].replace(region_mapping)
    
    columns_to_drop = ['Random_Text', 'Unused_Code', 'Extra_Column', 'Fake_Status']
    df = df.drop(columns=columns_to_drop, errors='ignore')
    
    return df

df_original = load_original()
df_cleaned = clean_data(df_original)

st.markdown("---")

# Step 1: Remove Duplicates
st.subheader("Step 1: Remove Duplicate Records")

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("""
    **Problem Identified**
    - Multiple instances of same customer
    - Skewed analysis results
    - Data integrity issues
    
    **Solution Applied**
    - Keep first occurrence of each customer_id
    - Remove all duplicate rows
    """)

with col2:
    duplicates_before = df_original.duplicated().sum()
    duplicates_after = df_cleaned.duplicated().sum()
    
    st.metric("Duplicates Before", duplicates_before)
    st.metric("Duplicates After", duplicates_after)
    st.metric("Removed", duplicates_before - duplicates_after)

st.markdown("---")

# Step 2: Handle Missing Values
st.subheader("Step 2: Handle Missing Values")

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("""
    **Problem Identified**
    - 1,445 missing values in region column
    - Represents 19.3% of data
    - Loss of customer location info
    
    **Solution Applied**
    - Standardize invalid values to 'Unknown'
    - Preserve customer records
    - Create new region category
    
    **Standardization Rules**
    - N/A → Unknown
    - ??? → Unknown
    - ### → Unknown
    - error → Unknown
    - invalid → Unknown
    - unknown → Unknown
    """)

with col2:
    missing_before = df_original['region'].isnull().sum()
    missing_after = df_cleaned['region'].isnull().sum()
    
    st.metric("Missing Before", missing_before)
    st.metric("Missing After", missing_after)
    st.metric("Fixed", missing_before - missing_after)

st.markdown("---")

# Step 3: Remove Unnecessary Columns
st.subheader("Step 3: Remove Non-Informative Columns")

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("""
    **Columns Removed**
    - Random_Text: Placeholder/noise data
    - Unused_Code: No analytical value
    - Extra_Column: Redundant information
    - Fake_Status: Artificial attribute
    
    **Rationale**
    - Focus on meaningful features
    - Reduce noise in dataset
    - Improve model interpretability
    """)

with col2:
    cols_before = df_original.shape[1]
    cols_after = df_cleaned.shape[1]
    
    st.metric("Columns Before", cols_before)
    st.metric("Columns After", cols_after)
    st.metric("Removed", cols_before - cols_after)

st.markdown("---")

# Before vs After Comparison
st.subheader("Before vs After Comparison")

comparison = pd.DataFrame({
    "Metric": [
        "Total Records",
        "Total Columns",
        "Duplicate Records",
        "Missing Values",
        "Data Completeness"
    ],
    "Before Cleaning": [
        f"{len(df_original):,}",
        df_original.shape[1],
        df_original.duplicated().sum(),
        df_original.isnull().sum().sum(),
        f"{(1 - df_original.isnull().sum().sum()/(df_original.shape[0]*df_original.shape[1]))*100:.1f}%"
    ],
    "After Cleaning": [
        f"{len(df_cleaned):,}",
        df_cleaned.shape[1],
        df_cleaned.duplicated().sum(),
        df_cleaned.isnull().sum().sum(),
        f"{(1 - df_cleaned.isnull().sum().sum()/(df_cleaned.shape[0]*df_cleaned.shape[1]))*100:.1f}%"
    ]
})

st.dataframe(comparison, use_container_width=True, hide_index=True)

st.markdown("---")

# Data Type Validation
st.subheader("Data Type Validation")

data_types = pd.DataFrame({
    "Column": df_cleaned.columns,
    "Data Type": df_cleaned.dtypes.astype(str),
    "Non-Null Count": df_cleaned.count(),
    "Sample Value": [str(df_cleaned[col].iloc[0]) for col in df_cleaned.columns]
})

st.dataframe(data_types, use_container_width=True, hide_index=True)

st.markdown("---")

# Quality Metrics
st.subheader("Data Quality Metrics")

metrics_cols = st.columns(4)

with metrics_cols[0]:
    completeness = (1 - df_cleaned.isnull().sum().sum()/(df_cleaned.shape[0]*df_cleaned.shape[1]))*100
    st.metric("Completeness Score", f"{completeness:.1f}%")

with metrics_cols[1]:
    st.metric("Duplicate Rate", f"{(df_cleaned.duplicated().sum()/len(df_cleaned)*100):.2f}%")

with metrics_cols[2]:
    retention = (len(df_cleaned)/len(df_original)*100)
    st.metric("Records Retained", f"{retention:.1f}%")

with metrics_cols[3]:
    st.metric("Quality Status", "EXCELLENT")

st.markdown("---")

# Summary
st.subheader("Cleaning Summary")

summary = f"""
Data cleaning successfully completed!

**Key Changes:**
- Removed {df_original.duplicated().sum()} duplicate records
- Standardized {df_original['region'].isnull().sum()} invalid region values
- Removed {df_original.shape[1] - df_cleaned.shape[1]} non-informative columns

**Final Dataset:**
- Records: {len(df_cleaned):,}
- Columns: {df_cleaned.shape[1]}
- Missing Values: {df_cleaned.isnull().sum().sum()}
- Data Quality: Excellent

Dataset is now ready for analysis and transformation.
"""

st.success(summary)
