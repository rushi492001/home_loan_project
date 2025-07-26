import streamlit as st

st.set_page_config(page_title="Power BI Dashboard", layout="wide")
st.title("📊 ADAROS Bank Analytics Dashboard")

powerbi_url = "https://app.powerbi.com/view?r=YOUR_EMBED_URL_HERE"

st.markdown(f"""
<iframe width="1000" height="600"
src="{powerbi_url}"
frameborder="0" allowFullScreen="true"></iframe>
""", unsafe_allow_html=True)
