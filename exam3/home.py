import streamlit as st

def app():
    # Main title and subtitle
    st.title("🏦 Bank Marketing Campaign")
    st.markdown("#### Predicting Term Deposit Subscriptions with Data-Driven Insights")

    # Divider line
    st.markdown("---")

    # Main description
    st.markdown("""
    Welcome! This application helps identify which customers are likely to **subscribe to a term deposit** based on:

    - Bank client data (age, job, marital status, etc.)
    - Campaign contact history
    - Socio-economic context

    🎯 **Objective**:  
    Improve marketing efficiency and reduce costs by targeting the right customers — those most likely to convert.

    ---  
    👉 **To get started**, choose a page from the sidebar on the left!
    """)

if __name__ == "__main__":
    app()
