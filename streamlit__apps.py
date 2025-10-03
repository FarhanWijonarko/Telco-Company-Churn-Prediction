import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model.joblib")

# Fungsi prediksi
def get_prediction(data: pd.DataFrame):
    pred = model.predict(data)
    pred_proba = model.predict_proba(data)
    return pred, pred_proba

def encode_input(
    seniorcitizen, gender, partner, dependents, multiplelines, onlinesecurity,
    onlinebackup, deviceprotection, techsupport, streamingmovies, contract,
    paperless, payment
):
    return pd.DataFrame([{
        "SeniorCitizen": seniorcitizen,
        "gender_Male": 1 if gender == "Male" else 0,
        "Partner_Yes": 1 if partner == "Yes" else 0,
        "Dependents_Yes": 1 if dependents == "Yes" else 0,
        "MultipleLines_Yes": 1 if multiplelines == "Yes" else 0,
        "OnlineSecurity_Yes": 1 if onlinesecurity == "Yes" else 0,
        "OnlineBackup_Yes": 1 if onlinebackup == "Yes" else 0,
        "DeviceProtection_Yes": 1 if deviceprotection == "Yes" else 0,
        "TechSupport_Yes": 1 if techsupport == "Yes" else 0,
        "StreamingMovies_Yes": 1 if streamingmovies == "Yes" else 0,
        "Contract_One year": 1 if contract == "One year" else 0,
        "Contract_Two year": 1 if contract == "Two year" else 0,
        "PaperlessBilling_Yes": 1 if paperless == "Yes" else 0,
        "PaymentMethod_Credit card (automatic)": 1 if payment == "Credit card (automatic)" else 0,
        "PaymentMethod_Electronic check": 1 if payment == "Electronic check" else 0,
        "PaymentMethod_Mailed check": 1 if payment == "Mailed check" else 0
    }])

# Page config
st.set_page_config(page_title="Telco Company Churn", page_icon="📉", layout="centered")

# Title
st.markdown("## 📉 Telco Company Churn Predictor")

with st.container():
    col1, col2 = st.columns(2)

    with col1:
        seniorcitizen = st.selectbox("Senior Citizen", [0, 1])
        gender = st.selectbox("Gender", ["Male", "Female"])
        partner = st.selectbox("Partner", ["Yes", "No"])
        dependents = st.selectbox("Dependents", ["Yes", "No"])
        multiplelines = st.selectbox("Multiple Lines", ["Yes", "No"])
        onlinesecurity = st.selectbox("Online Security", ["Yes", "No"])
        onlinebackup = st.selectbox("Online Backup", ["Yes", "No"])

    with col2:
        deviceprotection = st.selectbox("Device Protection", ["Yes", "No"])
        techsupport = st.selectbox("Tech Support", ["Yes", "No"])
        streamingmovies = st.selectbox("Streaming Movies", ["Yes", "No"])
        contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
        paperless = st.selectbox("Paperless Billing", ["Yes", "No"])
        payment = st.selectbox("Payment Method", [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ])

    st.markdown("---")
    if st.button("Predict"):
        data = encode_input(
            seniorcitizen, gender, partner, dependents, multiplelines, onlinesecurity,
            onlinebackup, deviceprotection, techsupport, streamingmovies, contract,
            paperless, payment
        )

        try:
            # Prediksi
            pred, pred_proba = get_prediction(data)

            if pred[0] == 1:
                st.error(f"⚠️ Prediction: Churn (Probability: {pred_proba[0][1]:.2f})")
            else:
                st.success(f"✅ Prediction: Not Churn (Probability: {pred_proba[0][0]:.2f})")
        except Exception as e:
            st.error(f"❌ Terjadi error: {e}")
