import streamlit as st
import pandas as pd

st.set_page_config(page_title="Recommendations", layout="wide")

st.subheader("Strategic Recommendations")
st.write("Actionable business strategies to reduce churn and increase revenue.")

st.markdown("---")

# Recommendation 1
with st.container():
    st.subheader("Recommendation 1: Premium Tier Upselling Program")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        **Problem Identified:**
        - Basic subscribers have 65% churn rate
        - Low revenue per user
        - Limited engagement features
        
        **Proposed Solution:**
        - Create personalized upsell campaigns
        - Offer 30-day premium trials
        - Bundle discounts for annual plans
        - Highlight premium content benefits
        
        **Implementation:**
        - Target Basic users with 15+ watch hours
        - A/B test different offer messages
        - Use email and in-app notifications
        - Track conversion rates
        """)
    
    with col2:
        st.markdown("""
        **Expected Impact:**
        
        Conservative Estimate:
        - 10% of Basic users convert to Premium
        - 500 customers × $10 premium uplift = $5,000/month
        - $60,000 additional annual revenue
        
        Optimistic Estimate:
        - 20% conversion rate
        - $120,000 additional annual revenue
        - 40% reduction in Basic tier churn
        
        **ROI: 400-600%**
        
        Implementation Cost: $15,000 (tooling + marketing)
        """)
    
    st.markdown("""
    **Success Metrics:**
    - Track conversion rate to Premium
    - Monitor average revenue per user
    - Measure Premium tier retention
    - Calculate customer lifetime value increase
    """)

st.markdown("---")

# Recommendation 2
with st.container():
    st.subheader("Recommendation 2: Inactive User Re-engagement Campaign")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        **Problem Identified:**
        - 70% of users inactive 45+ days churn
        - Lost engagement opportunity
        - Preventable customer loss
        
        **Proposed Solution:**
        - Automated re-engagement email series
        - Personalized content recommendations
        - Limited-time comeback offers
        - Push notifications for new releases
        
        **Implementation:**
        - Trigger at 20 days since last login
        - Send personalized content suggestions
        - Offer 1-month discount at day 30
        - Final retention offer at day 45
        """)
    
    with col2:
        st.markdown("""
        **Expected Impact:**
        
        Current Inactive Users: 1,500+
        
        Conservative Estimate:
        - 5% re-engagement rate
        - 75 customers retained
        - $900/month additional revenue
        - $10,800 annual revenue
        
        Optimistic Estimate:
        - 15% re-engagement rate
        - $32,400 additional annual revenue
        
        **ROI: 200-400%**
        
        Implementation Cost: $8,000 (automation + personnel)
        """)
    
    st.markdown("""
    **Success Metrics:**
    - Re-engagement rate (% reactivated)
    - Email open and click rates
    - Time to next login
    - Retention after re-engagement
    """)

st.markdown("---")

# Recommendation 3
with st.container():
    st.subheader("Recommendation 3: Personalized Content Recommendation Engine")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        **Problem Identified:**
        - Users with low watch hours (< 5 hrs/month) churn at 80%
        - Poor content discovery
        - Generic recommendation system
        
        **Proposed Solution:**
        - Implement ML-based recommendation system
        - Use genre preferences and watch history
        - Create personalized homepage
        - Suggest trending content by preference
        
        **Implementation:**
        - Analyze genre preferences
        - Build collaborative filtering model
        - Deploy recommendation algorithm
        - A/B test personalization strategies
        """)
    
    with col2:
        st.markdown("""
        **Expected Impact:**
        
        Target: 2,000 Low-Engagement Users
        
        Conservative Estimate:
        - 20% increase in watch hours
        - 15% reduction in churn rate
        - $25,000 annual revenue increase
        
        Optimistic Estimate:
        - 40% increase in watch hours
        - 25% reduction in churn rate
        - $60,000 annual revenue increase
        - Enhanced premium conversion
        
        **ROI: 150-400%**
        
        Implementation Cost: $40,000 (development + data science)
        """)
    
    st.markdown("""
    **Success Metrics:**
    - Average watch hours increase
    - Churn rate reduction
    - Content discovery improvement
    - Click-through rates on recommendations
    """)

st.markdown("---")

# Recommendation 4
with st.container():
    st.subheader("Recommendation 4: Device Experience Optimization")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        **Problem Identified:**
        - Mobile users show higher churn
        - Tablet experience suboptimal
        - Device-specific issues unaddressed
        
        **Proposed Solution:**
        - Improve mobile app performance
        - Optimize interface for tablets
        - Add offline viewing capability
        - Enhanced quality streaming options
        
        **Implementation:**
        - Performance audit for mobile app
        - UX redesign for touch interfaces
        - Implement offline cache feature
        - Test on various devices
        """)
    
    with col2:
        st.markdown("""
        **Expected Impact:**
        
        Mobile Users: 3,000+
        
        Conservative Estimate:
        - 10% reduction in mobile churn
        - 300 customers retained
        - $36,000 annual revenue increase
        
        Optimistic Estimate:
        - 20% churn reduction
        - Enhanced user satisfaction
        - Better app store ratings
        - $72,000+ annual revenue
        
        **ROI: 300-500%**
        
        Implementation Cost: $25,000 (development)
        """)
    
    st.markdown("""
    **Success Metrics:**
    - Mobile app churn rate
    - App ratings and reviews
    - Session length and frequency
    - User satisfaction scores
    """)

st.markdown("---")

# Recommendation 5
with st.container():
    st.subheader("Recommendation 5: Loyalty Rewards Program")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        **Problem Identified:**
        - No customer loyalty incentives
        - Competitors offer rewards
        - High-value customers not recognized
        
        **Proposed Solution:**
        - Points system for engagement
        - Exclusive content for loyal users
        - Birthday/anniversary special offers
        - Referral rewards program
        
        **Implementation:**
        - Award points for watch time
        - Monthly/annual loyalty bonuses
        - Exclusive early access to content
        - Referral commission structure
        """)
    
    with col2:
        st.markdown("""
        **Expected Impact:**
        
        Active Subscriber Base: 2,350
        
        Conservative Estimate:
        - 8% increase in retention
        - 188 customers retained
        - $22,500 annual revenue
        - 15 new referral signups
        
        Optimistic Estimate:
        - 15% retention improvement
        - $45,000 annual revenue
        - 40+ referral signups
        - Increased brand advocacy
        
        **ROI: 200-350%**
        
        Implementation Cost: $20,000 (platform + incentives)
        """)
    
    st.markdown("""
    **Success Metrics:**
    - Loyalty program enrollment rate
    - Points redemption rate
    - Referral signups and conversion
    - Retention rate improvement
    """)

st.markdown("---")

# Implementation Timeline
st.subheader("Implementation Timeline & Prioritization")

timeline = pd.DataFrame({
    "Initiative": [
        "Premium Upselling",
        "Inactive User Campaign",
        "Content Recommendation",
        "Device Optimization",
        "Loyalty Program"
    ],
    "Priority": ["High", "High", "Medium", "Medium", "Low"],
    "Timeline": ["0-1 month", "0-2 weeks", "1-3 months", "2-4 months", "1-2 months"],
    "Investment": ["$15K", "$8K", "$40K", "$25K", "$20K"],
    "Expected ROI": ["400-600%", "200-400%", "150-400%", "300-500%", "200-350%"]
})

st.dataframe(timeline, use_container_width=True, hide_index=True)

st.markdown("---")

# Total Impact
st.subheader("Combined Impact Summary")

total_revenue = 60000 + 10800 + 30000 + 50000 + 30000
total_investment = 15000 + 8000 + 40000 + 25000 + 20000
roi = ((total_revenue - total_investment) / total_investment) * 100

impact_cols = st.columns(3)

with impact_cols[0]:
    st.metric("Total Investment", f"${total_investment:,}", "Conservative Estimate")

with impact_cols[1]:
    st.metric("Annual Revenue Impact", f"${total_revenue:,}", f"+{total_revenue/12:.0f}/month")

with impact_cols[2]:
    st.metric("Combined ROI", f"{roi:.0f}%", "First Year")

st.success(f"""
Implementing all recommendations would generate:
- ${total_revenue:,} additional annual revenue
- {roi:.0f}% return on investment
- 800-1,000+ additional retained customers
- Improved customer lifetime value
- Enhanced competitive positioning
""")
