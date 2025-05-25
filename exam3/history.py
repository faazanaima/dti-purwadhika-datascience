import streamlit as st
import conn 

def app():
    st.title("History: User Actions")

    if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
        st.warning("⚠️ Please log in first to see your history.")
        return

    username = st.session_state["username"]
    connection = conn.get_connection()
    if not connection:
        st.error("Database connection error.")
        return

    try:
        cursor = connection.cursor()
        # Get user_id from username
        cursor.execute("SELECT user_id FROM user_dex WHERE name = %s", (username,))
        user_id_row = cursor.fetchone()
        if not user_id_row:
            st.error("User ID not found.")
            cursor.close()
            connection.close()
            return

        user_id = user_id_row[0]

        # Fetch history for this user_id
        cursor.execute("SELECT * FROM history_dex WHERE user_id = %s ORDER BY date DESC LIMIT 20", (user_id,))
        records = cursor.fetchall()
        colnames = [desc[0] for desc in cursor.description]

        cursor.close()
        connection.close()

        if records:
            st.write(f"History for user: **{username}**")
            # Show table with column names and records
            import pandas as pd
            df = pd.DataFrame(records, columns=colnames)
            st.dataframe(df)
        else:
            st.info("No history records found.")
    except Exception as e:
        st.error(f"Error fetching history data: {e}")
