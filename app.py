import streamlit as st
import pandas as pd
import joblib

model = joblib.load("trader_model_pipeline.pkl")

st.title("Trader Profitability Predictor")

size = st.number_input("Average Position Size (USD)")
win = st.slider("Win Rate", 0.0, 1.0)
trades = st.number_input("Trades per Day")

sentiment = st.selectbox(
    "Market Sentiment",
    ["Extreme Fear","Fear","Neutral","Greed","Extreme Greed"]
)

if st.button("Predict"):
    input_df = pd.DataFrame([{
        "Size USD": size,
        "win": win,
        "Direction": trades,
        "classification": sentiment
    }])
    
    prediction = model.predict(input_df)[0]
    
    if prediction == 1:
        st.success("Likely Profitable Day ✅")
    else:
        st.error("Likely Loss Day ❌")
