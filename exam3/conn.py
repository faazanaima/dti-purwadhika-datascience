import psycopg2
from psycopg2 import OperationalError
import streamlit as st

def get_connection():
    try:
        return psycopg2.connect(
            user=st.secrets["DB_USER"],
            password=st.secrets["DB_PASSWORD"],
            host=st.secrets["DB_HOST"],
            port=st.secrets["DB_PORT"],
            dbname=st.secrets["DB_NAME"]
        )

    except OperationalError as e:
        st.error(f"❌ Database connection failed: {e}")
        return None
