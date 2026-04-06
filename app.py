import streamlit as st
import pickle
import pandas as pd

model = pickle.load(open("churn_model.pkl", "rb"))

st.set_page_config(page_title="Churn Prediction", layout="wide")

# ---------- CUSTOM STYLE ---------- #
st.markdown("""
<style>
.big-title {
    font-size:40px !important;
    font-weight:700;
}
.card {
    padding:20px;
    border-radius:12px;
    background-color:#111827;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-title">📊 Customer Churn Prediction</p>', unsafe_allow_html=True)

st.markdown("### 🚀 Predict customer churn risk in real-time")

st.markdown("---")

# ---------- INPUT SECTION ---------- #

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 📈 Customer Info")
    tenure = st.slider("Tenure (months)", 0, 72, 12)
    MonthlyCharges = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)
    TotalCharges = st.number_input("Total Charges", 0.0, 10000.0, 1000.0)
    SeniorCitizen = st.selectbox("Senior Citizen", ["No", "Yes"])

with col2:
    st.markdown("#### 📡 Services")
    Contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    PaymentMethod = st.selectbox(
        "Payment Method",
        ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]
    )
    OnlineSecurity = st.selectbox("Online Security", ["No", "Yes"])
    TechSupport = st.selectbox("Tech Support", ["No", "Yes"])

st.markdown("---")

# ---------- CREATE INPUT ---------- #

input_df = pd.DataFrame(columns=model.feature_names_in_)
input_df.loc[0] = 0

input_df["tenure"] = tenure
input_df["MonthlyCharges"] = MonthlyCharges
input_df["TotalCharges"] = TotalCharges

if SeniorCitizen == "Yes":
    input_df["SeniorCitizen_1"] = 1

if Contract == "One year":
    input_df["Contract_One year"] = 1
elif Contract == "Two year":
    input_df["Contract_Two year"] = 1

if InternetService == "Fiber optic":
    input_df["InternetService_Fiber optic"] = 1
elif InternetService == "No":
    input_df["InternetService_No"] = 1

if PaymentMethod == "Electronic check":
    input_df["PaymentMethod_Electronic check"] = 1

if OnlineSecurity == "Yes":
    input_df["OnlineSecurity_Yes"] = 1

if TechSupport == "Yes":
    input_df["TechSupport_Yes"] = 1

# ---------- PREDICTION ---------- #

st.markdown("## 🔍 Prediction")

if st.button("Predict Churn"):

    prob = model.predict_proba(input_df)[0][1]

    st.markdown(f"### 🎯 Churn Probability: {prob:.2f}")

    # Progress bar
    st.progress(float(prob))

    # Risk levels
    if prob > 0.7:
        st.error("⚠️ High Risk Customer")
        st.write("👉 This customer is likely to churn. Consider retention offers.")
    elif prob > 0.4:
        st.warning("⚡ Medium Risk Customer")
        st.write("👉 Customer may churn. Monitor engagement.")
    else:
        st.success("✅ Low Risk Customer")
        st.write("👉 Customer is stable. No immediate action needed.")