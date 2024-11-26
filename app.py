# Import necessary libraries
import streamlit as st
import pickle
import numpy as np

# Load the Random Forest model
with open('soil_fertility_rf_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Custom CSS for UI enhancement
st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f6;
    }
    .main {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
    h1, h2, h3 {
        color: #333333;
        text-align: center;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit App Title
st.title("🌱 Soil Fertility Prediction App")

# Subtitle
st.subheader("Enter Soil Parameters Below")

# Layout with Columns for Inputs
col1, col2 = st.columns(2)

with col1:
    nitrogen = st.number_input("Nitrogen (N)", min_value=0.0, step=0.1, help="Enter the nitrogen content of the soil (in %).")
    phosphorus = st.number_input("Phosphorus (P)", min_value=0.0, step=0.1, help="Enter the phosphorus content of the soil (in %).")

with col2:
    potassium = st.number_input("Potassium (K)", min_value=0.0, step=0.1, help="Enter the potassium content of the soil (in %).")
    ph = st.number_input("pH", min_value=0.0, max_value=14.0, step=0.1, help="Enter the pH value of the soil.")

# Add space before the button
st.markdown("<br>", unsafe_allow_html=True)

# Predict Button
if st.button("🔍 Predict"):
    try:
        # Prepare features for prediction
        features = np.array([[nitrogen, phosphorus, potassium, ph]])
        
        # Make prediction
        prediction = model.predict(features)[0]
        
        # Display the prediction result with a styled message
        st.success(f"🌟 Predicted Soil Fertility: **{prediction}**")
    except Exception as e:
        st.error(f"❌ Error: {e}")

# Footer
st.markdown(
    """
    <hr>
    <p style='text-align: center; font-size: 14px; color: #666;'>
        Created using Streamlit
    </p>
    """,
    unsafe_allow_html=True
)
