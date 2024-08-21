import streamlit as st
import pandas as pd
import pickle

# Load the trained Random Forest model
model_filename = 'best_random_forest_model.pkl'
with open(model_filename, 'rb') as file:
    model = pickle.load(file)

st.title("Lithium Battery RUL Prediction")

# Input fields
Cycle_Index = st.number_input("Cycle Index", min_value=0)
Discharge_Time = st.number_input("Discharge Time (s)", min_value=0.0)
Decrement = st.number_input("Decrement (3.6-3.4V)", min_value=0.0)
Max_Voltage_Discharge = st.number_input("Max. Voltage Discharge (V)", min_value=0.0)
Min_Voltage_Charge = st.number_input("Min. Voltage Charge (V)", min_value=0.0)
Time = st.number_input("Time at 4.15V (s)", min_value=0.0)
Time_constant_current = st.number_input("Time constant current (s)", min_value=0.0)
Charging_time = st.number_input("Charging time (s)", min_value=0.0)

# Predict button
if st.button("Predict RUL"):
    # Create a DataFrame from the user input
    user_data = pd.DataFrame({
        'Cycle_Index': [Cycle_Index],
        'Discharge_Time': [Discharge_Time],
        'Decrement': [Decrement],
        'Max_Voltage_Discharge': [Max_Voltage_Discharge],
        'Min_Voltage_Charge': [Min_Voltage_Charge],
        'Time': [Time],
        'Time_constant_current': [Time_constant_current],
        'Charging_time': [Charging_time]
    })

    # Make prediction using the trained model
    predicted_rul = model.predict(user_data)[0]

    # Display the predicted RUL
    st.success(f"Predicted Remaining Useful Life (RUL): {predicted_rul:.2f} cycles")
