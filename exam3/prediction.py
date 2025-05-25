import streamlit as st
import prediction_single
import prediction_batch

def app():
    st.markdown("<h1 style='text-align: center;'>🎯DeX-APP: Term Deposit Subscription Predictor</h1>", unsafe_allow_html=True)
    st.markdown("""
    <p style='text-align: center; font-size: 16px;'>
    Use the buttons below to navigate to prediction pages.
    </p>
    <hr>
    """, unsafe_allow_html=True)

    if "page" not in st.session_state:
        st.session_state.page = "home"

    if st.session_state.page == "home":
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🧍‍♀️ Single Prediction"):
                st.session_state.page = "single"
        with col2:
            if st.button("📁 Batch Prediction"):
                st.session_state.page = "batch"

    elif st.session_state.page == "single":
        if st.button("⬅️ Back to Home"):
            st.session_state.page = "home"
        prediction_single.app()

    elif st.session_state.page == "batch":
        if st.button("⬅️ Back to Home"):
            st.session_state.page = "home"
        prediction_batch.app()

if __name__ == "__main__":
    app()
