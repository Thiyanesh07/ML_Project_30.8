import streamlit as st
import pickle
import pandas as pd


with open('uber_fare.rrr', 'rb') as model_file:
    model = pickle.load(model_file)

st.title("Uber Fare Prediction")


distance = st.number_input("Enter distance (in km)", min_value=0.0, max_value=100.0, value=10.0)
pickup_month = st.selectbox("Select pickup month", options=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], index=9)
passenger_count = st.number_input("Enter number of passengers", min_value=1, max_value=10, value=2)


input_data = pd.DataFrame({
    'distance': [distance],
    'pickup_month': [pickup_month],
    'passenger_count': [passenger_count]
})


if st.button("Predict Fare"):
    predicted_fare = model.predict(input_data)[0]
    st.write(f"Predicted Fare Amount: ${predicted_fare:.2f}")
 