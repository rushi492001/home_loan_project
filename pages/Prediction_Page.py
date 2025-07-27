import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Loan Prediction", layout="wide")
st.title("🔮 Loan Prediction Engine")

st.markdown("Fill in all applicant details to predict loan approval.")

# Load model
try:
    model = joblib.load("xgboost_home_loan_model.pkl")
except FileNotFoundError:
    st.error("❌ Model file not found! Please upload 'xgboost_home_loan_model.pkl' to the app directory.")
    st.stop()

with st.form("loan_prediction_form"):
    col1, col2 = st.columns(2)

    with col1:
        income = st.number_input("Annual Income (INR)", min_value=0.0, step=1000.0)
        credit_amt = st.number_input("Loan Credit Amount", min_value=0.0, step=1000.0)
        children = st.slider("Number of Children", 0, 10, 0)
        days_birth = st.number_input("Age in Days (Negative)", value=-12000)
        days_employed = st.number_input("Days Employed (Negative)", value=-500)
        ext_source_1 = st.number_input("External Score 1", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
        ext_source_2 = st.number_input("External Score 2", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
        ext_source_3 = st.number_input("External Score 3", min_value=0.0, max_value=1.0, value=0.5, step=0.01)

    with col2:
        education = st.selectbox("Education Level", [
            "Secondary / secondary special", 
            "Higher education", 
            "Incomplete higher", 
            "Lower secondary"
        ])
        family_status = st.selectbox("Family Status", [
            "Married", "Single / not married", "Civil marriage", "Separated"
        ])
        contract_type = st.selectbox("Contract Type", ["Cash loans", "Revolving loans"])
        gender = st.selectbox("Gender", ["Male", "Female"])
        occupation = st.selectbox("Occupation Type", [
            "Core staff", "Laborers", "Accountants", "Managers", "Drivers", "Sales staff", "Others"
        ])
        region_pop = st.number_input("Region Population Relative", min_value=0.0, max_value=1.0, value=0.01, step=0.01)
        days_publish = st.number_input("Days Since ID Published", value=-1000)
        own_car = st.selectbox("Owns a Car?", ["No", "Yes"])

    submit = st.form_submit_button("🚀 Predict")

    if submit:
        # Encode categorical values
        edu_map = {
            "Secondary / secondary special": 0,
            "Higher education": 1,
            "Incomplete higher": 2,
            "Lower secondary": 3
        }
        fam_map = {
            "Married": 0,
            "Single / not married": 1,
            "Civil marriage": 2,
            "Separated": 3
        }
        contract_map = {"Cash loans": 0, "Revolving loans": 1}
        gender_map = {"Male": 0, "Female": 1}
        occupation_map = {
            "Core staff": 0, "Laborers": 1, "Accountants": 2, "Managers": 3,
            "Drivers": 4, "Sales staff": 5, "Others": 6
        }
        car_map = {"No": 0, "Yes": 1}

        input_df = pd.DataFrame({
            "AMT_INCOME_TOTAL": [income],
            "AMT_CREDIT": [credit_amt],
            "CNT_CHILDREN": [children],
            "DAYS_BIRTH": [days_birth],
            "NAME_EDUCATION_TYPE": [edu_map[education]],
            "NAME_FAMILY_STATUS": [fam_map[family_status]],
            "NAME_CONTRACT_TYPE": [contract_map[contract_type]],
            "CODE_GENDER": [gender_map[gender]],
            "DAYS_EMPLOYED": [days_employed],
            "OCCUPATION_TYPE": [occupation_map[occupation]],
            "EXT_SOURCE_1": [ext_source_1],
            "EXT_SOURCE_2": [ext_source_2],
            "EXT_SOURCE_3": [ext_source_3],
            "REGION_POPULATION_RELATIVE": [region_pop],
            "DAYS_ID_PUBLISH": [days_publish],
            "FLAG_OWN_CAR": [car_map[own_car]]
        })

        try:
            prediction = model.predict(input_df)[0]
            result = "✅ Loan Approved" if prediction == 1 else "❌ Loan Not Approved"
            st.subheader("Prediction Result:")
            st.success(result)
        except Exception as e:
            st.error(f"🚫 Prediction failed: {e}")
