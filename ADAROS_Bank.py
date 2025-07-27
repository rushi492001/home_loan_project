import streamlit as st

# -------------------------------------------
# 🔧 Page Setup
# -------------------------------------------
st.set_page_config(page_title="ADAROS Bank", page_icon="🏦")

# -------------------------------------------
# 🏦 App Header
# -------------------------------------------
st.title("🏦 ADAROS Loan System")

# -------------------------------------------
# 📄 Welcome Message
# -------------------------------------------
st.markdown("""
Welcome to the **ADAROS Loan Credit Evaluation System**.

Use the sidebar to:
- 🧍‍♂️ Apply as a **New User**
- 🔍 Search records as an **Existing User**
""")

# -------------------------------------------
# 📬 Footer / Contact Info
# -------------------------------------------
st.divider()
st.markdown("📩 For support, contact: `adaros.support@bank.com`")
