# Custom CSS for UI enhancement
st.markdown(
    """
    <style>
    /* Overall body styling */
    body {
        background: linear-gradient(to bottom, #e8fce8, #d4f0d4);
        font-family: 'Arial', sans-serif;
        color: #333;
    }
    .main {
        background: #ffffff;
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
