import streamlit as st

st.set_page_config(page_title="ADAROS Bank Portal", layout="centered")

st.title("🏦 Welcome to ADAROS Bank")
st.markdown("Choose your action below:")

if st.button("👤 New User"):
    st.switch_page("pages/New_User.py")

if st.button("🔍 Existing User"):
    st.switch_page("pages/Existing_User.py")

if st.button("📊 View Power BI Dashboard"):
    st.switch_page("pages/PowerBI_Dashboard.py")
