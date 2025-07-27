import streamlit as st
import mysql.connector
import pandas as pd

# -------------------------------
# ✅ DB CONNECTION
# -------------------------------
def get_connection():
    try:
        return mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="rushi@492001#",
            database="loan_dataset"
        )
    except mysql.connector.Error as err:
        st.error(f"❌ MySQL Error: {err}")
        return None

# -------------------------------
# 🔍 FETCH USER DATA
# -------------------------------
def fetch_existing_user(sk_id_prev, sk_id_curr):
    conn = get_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT * FROM historical_data
            WHERE SK_ID_PREV = %s AND SK_ID_CURR = %s
        """, (sk_id_prev, sk_id_curr))
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result
    return []

# -------------------------------
# 🚀 STREAMLIT PAGE
# -------------------------------
st.set_page_config(page_title="View Existing User", layout="centered")
st.title("🏦 Existing User Lookup")

with st.form("fetch_form"):
    sk_id_prev = st.number_input("Enter SK_ID_PREV", min_value=0)
    sk_id_curr = st.number_input("Enter SK_ID_CURR", min_value=0)
    fetch = st.form_submit_button("🔍 Fetch User")

if fetch:
    user_data = fetch_existing_user(sk_id_prev, sk_id_curr)

    if user_data:
        st.success("✅ User Found!")
        st.dataframe(pd.DataFrame(user_data))
    else:
        st.error("❌ No user found with those IDs.")
