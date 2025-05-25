import streamlit as st
import home
import prediction
import about
import history
from custom_components import (
    custom_cleaning,
    ThresholdClassifier,
    drop_unwanted_columns,
    get_transformed_dataframe,
)
st.set_page_config(page_title="DeX APP: Term Deposit Bank Predictor", page_icon="🎯")
import conn

# ===== Load CSS Safely =====
def local_css(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except UnicodeDecodeError as e:
        st.error(f"❌ Error loading CSS file: {e}")
    except Exception as e:
        st.error(f"❌ General error loading CSS: {e}")

local_css("style.css")

# ===== Sidebar Menu =====
st.sidebar.title("📂 Navigation")
page = st.sidebar.selectbox("Select a Page", ("Home", "About", "Prediction", "History"), index=0)

if page == "Home":
    home.app()
elif page == "About":
    about.app()
elif page == "Prediction":
    prediction.app()
elif page == "History":
    history.app()

# ===== Sidebar Authentication =====
st.sidebar.title("👤 User Account")

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if "username" not in st.session_state:
    st.session_state["username"] = ""

if "clear_inputs" not in st.session_state:
    st.session_state["clear_inputs"] = False

# ===== DB Helper Functions =====
def authenticate_user(username, password):
    connection = conn.get_connection()
    if not connection:
        st.sidebar.error("Database connection error.")
        return False
    
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT pass FROM user_dex WHERE name = %s", (username,))
        user = cursor.fetchone()
        cursor.close()
        connection.close()
        return user and user[0] == password
    except Exception as e:
        st.sidebar.error(f"Error querying database: {e}")
        return False


def register_user(username, password):
    connection = conn.get_connection()
    if not connection:
        st.sidebar.error("Database connection error.")
        return False

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT 1 FROM user_dex WHERE name = %s", (username,))
        if cursor.fetchone():
            st.sidebar.error("Username already exists.")
            cursor.close()
            connection.close()
            return False

        cursor.execute("INSERT INTO user_dex (name, pass) VALUES (%s, %s)", (username, password))
        connection.commit()
        cursor.close()
        connection.close()
        return True
    except Exception as e:
        st.sidebar.error(f"Error registering user: {e}")
        return False

# ===== Auth Form Logic with placeholder =====
auth_placeholder = st.sidebar.empty()

if not st.session_state["authenticated"]:
    with auth_placeholder.container():
        auth_option = st.radio("Choose Option", ["Login", "Register"])

        # Set default values for inputs based on clear_inputs flag
        if st.session_state["clear_inputs"]:
            username_default = ""
            password_default = ""
            st.session_state["clear_inputs"] = False
        else:
            username_default = st.session_state.get("username_input", "")
            password_default = st.session_state.get("password_input", "")

        username_input = st.text_input("Username", value=username_default, key="username_input")
        password_input = st.text_input("Password", type="password", value=password_default, key="password_input")
        submit_clicked = st.button("Submit")

        if submit_clicked:
            if auth_option == "Login":
                if authenticate_user(username_input, password_input):
                    st.session_state["authenticated"] = True
                    st.session_state["username"] = username_input
                    st.success("✅ Login successful!")
                    st.session_state["clear_inputs"] = True  # Clear inputs on next rerun
                else:
                    st.error("❌ Incorrect username or password.")
            else:  # Register
                if register_user(username_input, password_input):
                    st.success("✅ Registration successful! Please log in.")
                    st.session_state["clear_inputs"] = True  # Clear inputs on next rerun
                else:
                    st.error("❌ Registration failed.")
else:
    with auth_placeholder.container():
        st.markdown(f"✅ Logged in as **{st.session_state['username']}**")
        if st.button("Logout"):
            st.session_state["authenticated"] = False
            st.session_state["username"] = ""
            st.success("You have been logged out.")
            st.session_state["clear_inputs"] = True  # Clear inputs on next rerun
