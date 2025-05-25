import streamlit as st

def app():
    st.title("💼 DeX-APP: Smart Targeting for Term Deposit Marketing")

    st.markdown("""
    ## 🎯 About DeX-APP
    **DeX-APP (Deposit Explorer – Advanced Prediction Platform)** is a smart machine learning solution built to help banks **predict which customers are most likely to subscribe to a term deposit**, using customer and campaign data.

    It empowers marketing teams to implement **targeted, efficient, and cost-effective strategies**—maximizing results, minimizing effort.

    ---

    ## 🧠 Machine Learning Backbone
    DeX-APP is powered by:
    - 🌲 **Random Forest Classifier** — known for strong performance and interpretability.
    - 🔧 **Hyperparameter Tuning** — to find the best model configuration.
    - 🎯 **Precision-Focused Thresholding** — to reduce false positives and avoid wasting marketing efforts.

    📌 **Why Precision?**  
    Because targeting the right customer saves time, effort, and cost in real-world campaigns.

    ---

    ## 📊 Model Evaluation Highlights
    The 2008-2010 dataset contains 7,802 samples, with 6,241 (80%) used for training, ensuring the model results are representative of that year’s customer data.
    - ✅ **Precision (yes)**: 82% — high accuracy in identifying customers likely to subscribe
    - ✅ **ROC AUC**: 0.78 — good separability
    - ✅ **PR AUC (AP)**: 0.78 — reliable in identifying positive cases

    🔍 **Top Features Influencing Prediction**:
    - `poutcome_success`, `balance`, `contact_other`, `age`, `pdays`, `housing_yes`, `is_firstcontact_True`

    These features reflect customer financial behavior, previous campaign results, and interaction methods.

    ---
    
    ## 💰 Marketing Cost Impact
    The predictive model reduces **total marketing cost** by approximately **67%**. Moreover, it also reduces **wasted marketing cost** by approximately **89%**.
    This means that for every dollar spent, the bank can expect a significantly higher return on investment by targeting the right customers.

    ---

    ## 🛠️ Tech Stack & Tools Overview

    - **💻 Backend as a Service**: PostgreSQL, managed via **Supabase** (BaaS)
    - **📊 Machine Learning**: Random Forest (with Hyperparameter Tuning & Threshold Optimization)
    - **🎯 Deployment**: Streamlit Cloud
    - **🧠 IDE**: Visual Studio Code (VSCode)
    - **🔧 Project Management**: Jira Software – for task tracking, sprint planning, and agile workflow
    - **📁 Version Control**: Git & GitHub  
      🔗 Repo: 

    All data flows securely allowing real-time predictions based on customer inputs.

    ---

    ## 🗂️ Navigation Guide
    Use the **sidebar menu** to explore:
    - 📥 **Prediction**: Upload and analyze customer data
    - 📊 **Results**: View model evaluation and SHAP explanations

    ---

    ## 📌 Project Goal
    > **"To empower banks with data-driven insights that improve term deposit subscriptions while optimizing marketing efforts."**

    Ready to explore? Select a page from the sidebar and start targeting smarter!
    """)

if __name__ == "__main__":
    app()