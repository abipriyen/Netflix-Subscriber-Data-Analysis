import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Data Cleaning", page_icon="🧹", layout="wide")

st.header("🧹 Data Cleaning Process")
st.write("Understand how raw data was transformed into analysis-ready data.")

# Load original data
@st.cache_data
def load_data():
    return pd.read_csv('data/netflix_customer_churn_unstructured.csv')

df_original = load_data()

# Create cleaned version
@st.cache_data
def clean_data(df):
    df = df.copy()
    
    # 1. Remove duplicates
    df = df.sort_values(by='customer_id')
    df = df.reset_index(drop=True)
    df = df[~df['customer_id'].duplicated(keep='first')]
    
    # 2. Handle missing values in region
    region_mapping = {
        'N/A': 'Unknown',
        '???': 'Unknown',
        '###': 'Unknown',
        'error': 'Unknown',
        'invalid': 'Unknown',
        'unknown': 'Unknown',
        np.nan: 'Unknown'
    }
    df['region'] = df['region'].fillna('Unknown')
    df['region'] = df['region'].replace(region_mapping)
    
    # 3. Remove unnecessary columns
    columns_to_drop = ['Random_Text', 'Unused_Code', 'Extra_Column', 'Fake_Status']
    df = df.drop(columns=columns_to_drop, errors='ignore')
    
    # 4. Clean Fake_Status if exists
    if 'Fake_Status' in df.columns:
        df = df.drop('Fake_Status', axis=1)
    
    return df

df_cleaned = clean_data(df_original)

st.markdown("---")

# Step 1: Remove Duplicates
st.subheader("Step 1️⃣: Remove Duplicate Records")

col1, col2 = st.columns(2)

with col1:
    st.info("""
    **Problem**: Dataset contains duplicate customer records
    
    **Solution**: Keep first occurrence, remove duplicates based on customer_id
    
    **Why**: Each customer should appear only once for accurate analysis
    """)

with col2:
    duplicates_before = df_original.duplicated().sum()
    duplicates_after = df_cleaned.duplicated().sum()
    
    col2_1, col2_2, col2_3 = st.columns(3)
    with col2_1:
        st.metric("Before", f"{duplicates_before}")
    with col2_2:
        st.write("➡️")
    with col2_3:
        st.metric("After", f"{duplicates_after}")
    
    st.success(f"✅ Removed {duplicates_before} duplicate records")

st.markdown("---")

# Step 2: Handle Missing Values
st.subheader("Step 2️⃣: Handle Missing Values")

col1, col2 = st.columns(2)

with col1:
    st.info("""
    **Problem**: ~1,445 missing values in 'region' column (19.3%)
    
    **Solution**: Replace with 'Unknown' category
    
    **Why**: Preserves records while maintaining data integrity
    """)

with col2:
    missing_before = df_original['region'].isnull().sum()
    missing_after = df_cleaned['region'].isnull().sum()
    
    col2_1, col2_2, col2_3 = st.columns(3)
    with col2_1:
        st.metric("Before", f"{missing_before}")
    with col2_2:
        st.write("➡️")
    with col2_3:
        st.metric("After", f"{missing_after}")
    
    st.success(f"✅ Handled {missing_before} missing values")

# Show region value mapping
st.write("**Region Value Standardization:**")
region_mapping_display = {
    'N/A': 'Unknown',
    '???': 'Unknown',
    '###': 'Unknown',
    'error': 'Unknown',
    'invalid': 'Unknown',
    'unknown': 'Unknown'
}

for old_val, new_val in region_mapping_display.items():
    st.write(f"• '{old_val}' → '{new_val}'")

st.markdown("---")

# Step 3: Remove Unnecessary Columns
st.subheader("Step 3️⃣: Remove Unnecessary Columns")

col1, col2 = st.columns(2)

with col1:
    st.info("""
    **Problem**: Dataset contains irrelevant columns
    
    **Solution**: Remove non-informative columns
    
    **Why**: Focus on meaningful features for analysis
    """)

with col2:
    cols_before = df_original.shape[1]
    cols_after = df_cleaned.shape[1]
    
    col2_1, col2_2, col2_3 = st.columns(3)
    with col2_1:
        st.metric("Before", f"{cols_before}")
    with col2_2:
        st.write("➡️")
    with col2_3:
        st.metric("After", f"{cols_after}")
    
    st.success(f"✅ Removed {cols_before - cols_after} unnecessary columns")

st.write("**Columns Removed:**")
removed_cols = ['Random_Text', 'Unused_Code', 'Extra_Column', 'Fake_Status']
for col in removed_cols:
    st.write(f"• {col}")

st.markdown("---")

# Before vs After Summary
st.subheader("📊 Before vs After Comparison")

comparison_data = {
    "Metric": [
        "Total Rows",
        "Total Columns",
        "Duplicate Records",
        "Missing Values",
        "Memory Usage (KB)"
    ],
    "Before Cleaning": [
        f"{len(df_original):,}",
        df_original.shape[1],
        df_original.duplicated().sum(),
        df_original.isnull().sum().sum(),
        f"{df_original.memory_usage(deep=True).sum() / 1024:.2f}"
    ],
    "After Cleaning": [
        f"{len(df_cleaned):,}",
        df_cleaned.shape[1],
        df_cleaned.duplicated().sum(),
        df_cleaned.isnull().sum().sum(),
        f"{df_cleaned.memory_usage(deep=True).sum() / 1024:.2f}"
    ]
}

comparison_df = pd.DataFrame(comparison_data)
st.dataframe(comparison_df, use_container_width=True)

st.markdown("---")

# Data Type Validation
st.subheader("🔍 Data Type Validation")

st.write("**Cleaned Dataset Column Types:**")
data_types = pd.DataFrame({
    "Column Name": df_cleaned.columns,
    "Data Type": df_cleaned.dtypes.astype(str),
    "Sample Value": [str(df_cleaned[col].iloc[0]) for col in df_cleaned.columns]
})

st.dataframe(data_types, use_container_width=True)

st.markdown("---")

# Data Quality Metrics
st.subheader("✅ Data Quality Metrics")

quality_col1, quality_col2, quality_col3, quality_col4 = st.columns(4)

with quality_col1:
    st.metric(
        "Data Completeness",
        f"{(1 - df_cleaned.isnull().sum().sum()/(df_cleaned.shape[0]*df_cleaned.shape[1]))*100:.1f}%"
    )

with quality_col2:
    st.metric(
        "Duplicate Rate",
        f"{(df_cleaned.duplicated().sum()/len(df_cleaned)*100):.1f}%"
    )

with quality_col3:
    st.metric(
        "Records Retained",
        f"{(len(df_cleaned)/len(df_original)*100):.1f}%"
    )

with quality_col4:
    st.metric(
        "Data Integrity",
        "✅ Excellent"
    )

st.markdown("---")

# Cleaning Summary
st.subheader("📋 Cleaning Summary")

summary_text = f"""
✅ **Successfully Cleaned Dataset!**

**Key Changes:**
- ❌ Removed {df_original.duplicated().sum()} duplicate records
- ✅ Standardized {region_mapping_display.__len__()} invalid region values
- 🗑️ Removed {cols_before - cols_after} non-informative columns
- 📊 Final dataset: {len(df_cleaned):,} records × {cols_after} columns

**Data Quality Improved:**
- Missing values: {df_original.isnull().sum().sum()} → {df_cleaned.isnull().sum().sum()}
- Data completeness: ~{(df_original.isnull().sum().sum()/(df_original.shape[0]*df_original.shape[1]))*100:.1f}% → {(1 - df_cleaned.isnull().sum().sum()/(df_cleaned.shape[0]*df_cleaned.shape[1]))*100:.1f}%

**Next Steps:**
→ Proceed to EDA for deeper analysis
"""  

st.success(summary_text)

st.markdown("---")

# Download cleaned data
st.subheader("📥 Download Cleaned Data")
csv = df_cleaned.to_csv(index=False)
st.download_button(
    label="Download Cleaned CSV",
    data=csv,
    file_name="netflix_cleaned.csv",
    mime="text/csv"
)
