# Import necessary libraries
import streamlit as st
import pickle
import numpy as np

# Load the Random Forest model
with open('soil_fertility_rf_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Custom CSS for UI enhancement with a background image
st.markdown(
    """
    <style>
    /* Full-page background image */
    body {
        background-image: url('soil.jpeg'); /* Replace with the actual URL or local path */
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
        font-family: 'Arial', sans-serif;
        color: #333;
    }
    .main {
        background: rgba(255, 255, 255, 0.85); /* White background with transparency for readability */
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);
        margin-top: 30px;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
    }
    h1 {
        color: #2d6a4f;
        font-family: 'Trebuchet MS', sans-serif;
        text-align: center;
        font-size: 2.5em;
        margin-bottom: 20px;
        text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
    }
    h2, h3 {
        color: #40916c;
        text-align: center;
        font-size: 1.8em;
        margin-bottom: 15px;
    }
    .stButton>button {
        background: linear-gradient(to right, #52b788, #40916c);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 12px 25px;
        font-size: 18px;
        cursor: pointer;
        transition: all 0.3s ease;
        font-weight: bold;
    }
    .stButton>button:hover {
        background: linear-gradient(to right, #40916c, #1b4332);
        transform: scale(1.05);
    }
    .stNumberInput input {
        border: 2px solid #b7e4c7;
        border-radius: 10px;
        padding: 10px;
        font-size: 16px;
        color: #333;
    }
    .stNumberInput input:focus {
        border-color: #52b788;
        outline: none;
        box-shadow: 0 0 8px rgba(82, 183, 136, 0.8);
    }
    footer {
        font-family: 'Arial', sans-serif;
        color: #555;
        text-align: center;
        margin-top: 30px;
    }
    hr {
        border: 0;
        border-top: 1px solid #ddd;
        margin: 30px 0;
    }
    .css-1aumxhk {
        max-width: 800px; /* Adjust for readability on larger screens */
        margin: auto;
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
        Created using Streamlit | Powered by Machine Learning
    </p>
    """,
    unsafe_allow_html=True
)
