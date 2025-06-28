import streamlit as st
import joblib

st.title("🇳🇿 NZ Tax Phishing Detector")

model = joblib.load("phishing_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

text = st.text_area("Enter message text:")

if st.button("Check"):
    text_vector = vectorizer.transform([text])
    prediction = model.predict(text_vector)
    if prediction[0] == 1:
        st.error("🚨 PHISHING Message Detected!")
    else:
        st.success("✅ Legitimate Message.")
