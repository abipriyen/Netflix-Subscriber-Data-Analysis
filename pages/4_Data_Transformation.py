import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Data Transformation", layout="wide")

st.subheader("Data Transformation & Feature Engineering")
st.write("Creating new features and engineering variables for advanced analysis.")

# Load and clean data
@st.cache_data
def load_and_transform():
    df = pd.read_csv('data/netflix_customer_churn_unstructured.csv')
    
    # Cleaning
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
    
    # Feature Engineering
    df['age_group'] = pd.cut(df['age'], bins=[0, 18, 25, 35, 50, 100],
                            labels=['<18', '18-25', '26-35', '36-50', '50+'])
    
    df['engagement_level'] = pd.cut(df['watch_hours'], bins=[0, 5, 15, 30, 100],
                                   labels=['Low', 'Medium', 'High', 'Very High'])
    
    df['loyalty_score'] = (
        (df['watch_hours'] / df['watch_hours'].max()) * 0.4 +
        ((60 - df['last_login_days']) / 60) * 0.3 +
        (df['number_of_profiles'] / df['number_of_profiles'].max()) * 0.3
    ) * 100
    
    df['revenue_segment'] = pd.cut(df['monthly_fee'], bins=[0, 8, 13, 20],
                                  labels=['Basic', 'Standard', 'Premium'])
    
    df['inactive_risk'] = df['last_login_days'].apply(
        lambda x: 'High Risk' if x > 45 else 'Medium Risk' if x > 20 else 'Low Risk'
    )
    
    df['customer_value'] = df['monthly_fee'] * 12 * (1 - df['churned'])
    
    return df

df_transformed = load_and_transform()

st.markdown("---")

# Feature Engineering Overview
st.subheader("Feature Engineering Overview")

st.info("""
New features created for deeper analysis:
- Age Group: Categorical age segments
- Engagement Level: Customer activity classification
- Loyalty Score: Composite metric (0-100)
- Revenue Segment: Subscription tier classification
- Inactive Risk: Churn risk based on login activity
- Customer Value: Annual revenue contribution
""")

st.markdown("---")

# Feature 1: Age Group
st.subheader("Feature 1: Age Group Segmentation")

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("""
    **Transformation Logic**
    - Age < 18: <18
    - Age 18-25: 18-25
    - Age 26-35: 26-35
    - Age 36-50: 36-50
    - Age > 50: 50+
    
    **Purpose**
    - Demographic segmentation
    - Identify age-based patterns
    - Target marketing campaigns
    """)

with col2:
    age_dist = df_transformed['age_group'].value_counts()
    st.bar_chart(age_dist)

st.markdown("---")

# Feature 2: Engagement Level
st.subheader("Feature 2: Engagement Level Classification")

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("""
    **Transformation Logic**
    - Low: < 5 hours/month
    - Medium: 5-15 hours/month
    - High: 15-30 hours/month
    - Very High: > 30 hours/month
    
    **Purpose**
    - Measure customer activity
    - Identify inactive users
    - Predict retention likelihood
    """)

with col2:
    engagement_dist = df_transformed['engagement_level'].value_counts()
    st.bar_chart(engagement_dist)

st.markdown("---")

# Feature 3: Loyalty Score
st.subheader("Feature 3: Loyalty Score (Composite Metric)")

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("""
    **Calculation Formula**
    - Watch Hours (40%): Activity indicator
    - Login Recency (30%): Engagement indicator
    - Profiles Count (30%): Family sharing indicator
    
    **Score Range**: 0-100
    - 0-25: Low Loyalty
    - 25-50: Medium Loyalty
    - 50-75: High Loyalty
    - 75-100: Very High Loyalty
    
    **Purpose**
    - Single metric for customer value
    - Prioritize retention efforts
    - Identify VIP customers
    """)

with col2:
    st.write(f"**Loyalty Score Statistics**")
    loyalty_stats = pd.DataFrame({
        "Metric": ["Min", "Max", "Mean", "Median", "Std Dev"],
        "Value": [
            f"{df_transformed['loyalty_score'].min():.2f}",
            f"{df_transformed['loyalty_score'].max():.2f}",
            f"{df_transformed['loyalty_score'].mean():.2f}",
            f"{df_transformed['loyalty_score'].median():.2f}",
            f"{df_transformed['loyalty_score'].std():.2f}"
        ]
    })
    st.dataframe(loyalty_stats, use_container_width=True, hide_index=True)

st.markdown("---")

# Feature 4: Inactive Risk
st.subheader("Feature 4: Inactive Risk Assessment")

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("""
    **Risk Classification**
    - Low Risk: Last login < 20 days
    - Medium Risk: Last login 20-45 days
    - High Risk: Last login > 45 days
    
    **Purpose**
    - Identify at-risk customers
    - Target retention campaigns
    - Prioritize support efforts
    """)

with col2:
    risk_dist = df_transformed['inactive_risk'].value_counts()
    st.bar_chart(risk_dist)

st.markdown("---")

# Feature 5: Customer Value
st.subheader("Feature 5: Annual Customer Value")

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("""
    **Calculation Formula**
    Annual Revenue = Monthly Fee × 12 × Retention Factor
    
    **Purpose**
    - Quantify customer contribution
    - Prioritize high-value customers
    - Guide retention strategy ROI
    
    **Interpretation**
    - High value: Premium subscribers
    - Medium value: Standard subscribers
    - Low value: Basic subscribers
    """)

with col2:
    value_stats = pd.DataFrame({
        "Subscription": ["Basic", "Standard", "Premium"],
        "Avg Annual Value": [
            f"${(df_transformed[df_transformed['revenue_segment']=='Basic']['customer_value'].mean()):.2f}",
            f"${(df_transformed[df_transformed['revenue_segment']=='Standard']['customer_value'].mean()):.2f}",
            f"${(df_transformed[df_transformed['revenue_segment']=='Premium']['customer_value'].mean()):.2f}"
        ]
    })
    st.dataframe(value_stats, use_container_width=True, hide_index=True)

st.markdown("---")

# Transformed Data Preview
st.subheader("Transformed Dataset Preview")

columns_to_show = ['customer_id', 'age', 'age_group', 'watch_hours', 'engagement_level',
                   'loyalty_score', 'inactive_risk', 'churned']
available_cols = [col for col in columns_to_show if col in df_transformed.columns]

st.dataframe(
    df_transformed[available_cols].head(10),
    use_container_width=True,
    hide_index=True
)

st.markdown("---")

# Summary Statistics
st.subheader("Transformation Summary")

summary_cols = st.columns(3)

with summary_cols[0]:
    st.metric("Total Records Transformed", f"{len(df_transformed):,}")

with summary_cols[1]:
    st.metric("New Features Created", "6")

with summary_cols[2]:
    st.metric("Total Columns", df_transformed.shape[1])

st.success("""
Data transformation completed successfully!

New features created for deeper analysis:
1. Age Group - Demographic segmentation
2. Engagement Level - Activity classification
3. Loyalty Score - Composite customer value metric
4. Revenue Segment - Subscription tier classification
5. Inactive Risk - Churn risk assessment
6. Customer Value - Annual revenue contribution

Dataset is now enriched and ready for visualization and analysis.
""")
