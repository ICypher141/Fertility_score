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
        background-color: #eaf7ea; /* Soft green background for a natural feel */
    }
    .main {
        background: linear-gradient(to bottom right, #ffffff, #e8f5e9);
        border-radius: 15px;
        padding: 25px;
        box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.2);
    }
    h1 {
        color: #2e7d32;
        text-align: center;
        font-family: 'Roboto', sans-serif;
        font-weight: bold;
    }
    h2, h3 {
        color: #388e3c;
        text-align: center;
        font-family: 'Roboto', sans-serif;
    }
    .stButton>button {
        background-color: #43a047;
        color: white;
        border-radius: 12px;
        border: 2px solid #388e3c;
        padding: 12px 24px;
        font-size: 18px;
        font-family: 'Arial', sans-serif;
        font-weight: bold;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #2e7d32;
        border-color: #1b5e20;
        transform: scale(1.05);
    }
    input[type="number"] {
        border: 2px solid #c8e6c9;
        border-radius: 8px;
        padding: 10px;
        font-size: 16px;
    }
    input[type="number"]:focus {
        outline: none;
        border-color: #66bb6a;
        box-shadow: 0 0 5px rgba(102, 187, 106, 0.8);
    }
    footer {
        font-family: 'Arial', sans-serif;
        color: #555;
        text-align: center;
    }
    hr {
        border: 0;
        border-top: 1px solid #ddd;
        margin: 30px 0;
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
