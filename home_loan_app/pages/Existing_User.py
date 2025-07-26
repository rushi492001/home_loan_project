import streamlit as st
import pandas as pd
from utils.db_utils import fetch_existing_user

st.set_page_config(page_title="Search Existing User", layout="wide")
st.title("🔎 Lookup Existing Loan Record")

with st.form("search_form"):
    sk_id_prev = st.number_input("Enter SK_ID_PREV", min_value=0)
    sk_id_curr = st.number_input("Enter SK_ID_CURR", min_value=0)
    submitted = st.form_submit_button("Fetch Record")

    if submitted:
        data = fetch_existing_user(sk_id_prev, sk_id_curr)
        if data:
            st.success("🎯 Record Found!")
            st.dataframe(pd.DataFrame(data))
        else:
            st.warning("❌ No data found for given IDs.")
