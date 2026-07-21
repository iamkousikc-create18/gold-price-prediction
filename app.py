import streamlit as st
import pickle
import pandas as pd

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Gold Price Prediction",
    page_icon="🥇",
    layout="centered"
)

# ----------------------------
# Load Model
# ----------------------------
with open("rf_model.pkl", "rb") as file:
    model = pickle.load(file)

# ----------------------------
# Title
# ----------------------------
st.title("🥇 Gold Price Prediction")
st.write(
    "Enter the market values below to predict the Gold Price using the trained Random Forest model."
)

st.divider()

# ----------------------------
# User Inputs
# ----------------------------
spx = st.number_input(
    "📈 S&P 500 Index (SPX)",
    min_value=0.0,
    value=4500.0
)

uso = st.number_input(
    "🛢️ US Oil Fund (USO)",
    min_value=0.0,
    value=70.0
)

slv = st.number_input(
    "🥈 Silver Price (SLV)",
    min_value=0.0,
    value=22.0
)

eur_usd = st.number_input(
    "💶 EUR/USD Exchange Rate",
    min_value=0.0,
    value=1.10,
    format="%.4f"
)

# ----------------------------
# Prediction
# ----------------------------
if st.button("Predict Gold Price"):

    input_data = pd.DataFrame({
        "SPX": [spx],
        "USO": [uso],
        "SLV": [slv],
        "EUR/USD": [eur_usd]
    })

    prediction = model.predict(input_data)[0]

    st.success(f"💰 Predicted Gold Price: **{prediction:.2f} USD**")

    st.balloons()

st.divider()

st.caption("Developed using Streamlit & Scikit-Learn")