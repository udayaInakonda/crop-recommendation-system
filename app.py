import streamlit as st
import numpy as np
import joblib
import pandas as pd

# Load model, scaler, and encoder
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
label_encoder = joblib.load("label_encoder.pkl")

st.title("🌾 Crop Recommendation System")
st.markdown("Enter the soil and weather conditions below:")

# UI inputs
N = st.number_input("Nitrogen (N)", 0, 140)
P = st.number_input("Phosphorus (P)", 5, 145)
K = st.number_input("Potassium (K)", 5, 205)
temperature = st.number_input("Temperature (°C)", 0.0, 50.0)
humidity = st.number_input("Humidity (%)", 10.0, 100.0)
ph = st.number_input("pH level", 3.5, 9.5)
rainfall = st.number_input("Rainfall (mm)", 10.0, 300.0)

# Predict button
if st.button("Predict Crop"):
    # Use DataFrame with correct feature names to avoid sklearn warning
    feature_names = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]
    input_df = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    input_df = pd.DataFrame(input_df, columns=feature_names)
    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)
    crop_name = label_encoder.inverse_transform(prediction)[0]
    st.success(f"✅ Recommended Crop: **{crop_name.title()}**")
