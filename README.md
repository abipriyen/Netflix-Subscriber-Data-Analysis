# Netflix Customer Churn Analysis Dashboard

## 📊 Project Overview

A professional, interactive Streamlit web application that transforms Netflix customer churn analysis from a Jupyter Notebook into a production-ready business intelligence dashboard.

## 🎯 Project Goals

- Convert notebook analysis into an interactive multi-page dashboard
- Provide deep insights into customer churn patterns
- Enable data-driven business decisions
- Demonstrate complete data analytics workflow
- Create a portfolio-quality project

## 📁 Project Structure

```
Netflix-Churn-Analysis/
├── app.py                          # Main Streamlit app
├── requirements.txt                # Project dependencies
├── README.md                       # This file
├── .gitignore                      # Git ignore rules
├── data/
│   └── netflix_customer_churn_unstructured.csv
├── pages/
│   ├── 1_Home.py
│   ├── 2_Dataset_Overview.py
│   ├── 3_Data_Cleaning.py
│   ├── 4_EDA.py
│   ├── 5_Visualizations.py
│   ├── 6_Business_Insights.py
│   ├── 7_Recommendations.py
│   └── 8_Conclusion.py
└── utils/
    ├── data_loader.py
    ├── data_cleaner.py
    └── visualization.py
```

## 🚀 Quick Start

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Netflix-Churn-Analysis.git
   cd Netflix-Churn-Analysis
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```bash
   streamlit run app.py
   ```

5. **Open in browser**
   Navigate to `http://localhost:8501`

## 📋 Dashboard Pages

### 🏠 1. Home Page
- Project introduction and branding
- Business problem statement
- Key objectives
- KPI cards (Total Customers, Retention Rate, Churn Rate, Avg Revenue)
- Quick navigation guide

### 📂 2. Dataset Overview
- Dataset shape and structure
- Column information
- Data types summary
- Numerical and categorical features
- Missing values analysis
- Duplicate records check
- Statistical summary

### 🧹 3. Data Cleaning
- Missing value handling
- Duplicate removal process
- Feature engineering steps
- Data encoding
- Before & After comparisons
- Data validation results

### 📊 4. Exploratory Data Analysis (EDA)
- Customer demographics
- Distribution analysis
- Churn patterns
- Revenue analysis
- Usage patterns
- Device and subscription analysis

### 📈 5. Interactive Visualizations
- Dynamic dashboard with filters
- Gender distribution
- Subscription type analysis
- Device usage patterns
- Age demographics
- Churn distribution
- Revenue trends
- Correlation heatmap

### 💡 6. Business Insights
- High-risk customer segments
- Profitability analysis
- Revenue trends
- Customer retention factors
- Churn drivers
- Key findings explained in business language

### 🎯 7. Recommendations
- Actionable business recommendations
- Problem identification
- Proposed solutions
- Expected business impact
- Implementation strategies

### ✅ 8. Conclusion
- Executive summary
- Key findings recap
- Business recommendations summary
- Future improvements
- Project conclusion

## 🛠 Technology Stack

- **Frontend**: Streamlit 1.28.1
- **Data Processing**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn, Plotly
- **Machine Learning**: Scikit-learn
- **Database**: CSV (can be extended to SQL)
- **Deployment**: Streamlit Cloud

## 📊 Dataset Information

**File**: `netflix_customer_churn_unstructured.csv`

**Columns** (14 useful columns after cleaning):
- `customer_id`: Unique customer identifier
- `age`: Customer age (18-70)
- `gender`: Customer gender (Male, Female, Other)
- `subscription_type`: Basic, Standard, Premium
- `watch_hours`: Monthly watch hours
- `last_login_days`: Days since last login
- `region`: Geographic region
- `device`: Device type used
- `monthly_fee`: Monthly subscription cost
- `churned`: Target variable (0/1)
- `payment_method`: Payment type
- `number_of_profiles`: Number of profiles
- `avg_watch_time_per_day`: Average daily watch time
- `favorite_genre`: Preferred content genre

**Statistics**:
- Total Records: 7,500 (5,000 unique customers)
- Duplicates: 2,500 (removed)
- Missing Values: ~1,445 in region column
- Churn Rate: ~53%
- Revenue: $8.99 - $17.99/month

## 🔧 Data Cleaning Process

1. **Remove Duplicates**: 2,500 duplicate records removed
2. **Handle Missing Values**: Region column (~19.3% missing)
3. **Standardize Invalid Values**: Replace '???', '###', 'error', 'invalid', 'unknown'
4. **Remove Unnecessary Columns**: Random_Text, Unused_Code, Extra_Column, Fake_Status
5. **Feature Engineering**: Create age groups, churn segments, revenue segments
6. **Data Type Conversion**: Ensure proper data types

## 📈 Key Insights

- Premium subscribers have lower churn rates
- Inactive users (high last_login_days) churn more frequently
- High watch hours correlate with retention
- Certain regions show higher churn patterns
- Desktop users show better retention than mobile

## 🎨 Design Theme

- **Color Scheme**: Netflix Dark Theme (Black, Red, White)
- **Layout**: Clean, modular, professional
- **Typography**: Sans-serif, readable fonts
- **Components**: Rounded cards, hover effects, smooth transitions

## 📊 Deployment Instructions

### Deploy on Streamlit Cloud

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Add Netflix Churn Dashboard"
   git push origin main
   ```

2. **Create Streamlit Account**
   - Visit https://streamlit.io/cloud
   - Sign up with GitHub

3. **Deploy App**
   - Click "New app"
   - Select your repository
   - Choose branch: `main`
   - Set main file path: `app.py`
   - Click "Deploy"

4. **Share URL**
   - Your app will be live at: `https://your-username-netflix-churn.streamlit.app`

### Deploy on Heroku

1. **Create Procfile**
   ```
   web: sh setup.sh && streamlit run app.py
   ```

2. **Create setup.sh**
   ```bash
   mkdir -p ~/.streamlit/
   echo "[server]
headless = true
port = $PORT
enableXsrfProtection = false
" > ~/.streamlit/config.toml
   ```

3. **Deploy**
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

## 📚 Key Metrics Explained

### KPI Cards
- **Total Customers**: 5,000 unique customers
- **Retention Rate**: Percentage of active customers (47%)
- **Churn Rate**: Percentage of customers who left (53%)
- **Avg Monthly Revenue**: Average revenue per customer

### Visualizations
- **Churn by Subscription**: Premium has lowest churn
- **Revenue by Device**: Desktop generates most revenue
- **Age Distribution**: 18-70 age range fairly distributed
- **Watch Hours**: Higher hours = better retention

## 🔍 Analysis Highlights

1. **Premium vs Basic**: Premium subscribers 30% less likely to churn
2. **Engagement Matters**: High watch hours = 75% retention rate
3. **Device Impact**: Desktop users 20% more likely to stay
4. **Payment Method**: Credit card users more loyal
5. **Regional Patterns**: Some regions show 60%+ churn

## 💼 Business Impact

- Identify high-risk customers for retention campaigns
- Optimize subscription pricing and offers
- Improve customer engagement strategies
- Guide marketing and product decisions
- Increase customer lifetime value

## 🚀 Future Enhancements

- Machine learning churn prediction model
- Real-time data updates via API
- Advanced segmentation analysis
- Cohort analysis
- Customer journey visualization
- A/B testing framework
- Email campaign integration
- Custom report generation

## 📞 Support & Contact

For questions or issues:
- Create an issue on GitHub
- Contact: your-email@example.com

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.

## 👏 Acknowledgments

- Streamlit team for the amazing framework
- Netflix for inspiring the analysis
- Data science community for best practices

---

**Made with ❤️ by Data Analysts**

**Last Updated**: 2024
**Version**: 1.0.0
