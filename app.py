import streamlit as st

def convert_units(category, from_unit, to_unit, value):
    conversions = {
        "Length": {
            "Meters": 1, "Kilometers": 0.001, "Centimeters": 100, "Inches": 39.3701, "Feet": 3.28084
        },
        "Temperature": {
            "Celsius": lambda x: x, "Fahrenheit": lambda x: (x * 9/5) + 32, "Kelvin": lambda x: x + 273.15
        },
        "Weight": {
            "Kilograms": 1, "Grams": 1000, "Pounds": 2.20462, "Ounces": 35.274
        },
        "Volume": {
            "Liters": 1, "Milliliters": 1000, "Gallons": 0.264172, "Cups": 4.22675
        },
        "Time": {
            "Seconds": 1, "Minutes": 1/60, "Hours": 1/3600, "Days": 1/86400
        }
    }
    
    if category == "Temperature":
        return conversions[category][to_unit](conversions[category][from_unit](value))
    
    base_value = value / conversions[category][from_unit]
    return base_value * conversions[category][to_unit]

# Streamlit UI
st.set_page_config(page_title="Unit Converter", page_icon="⚡", layout="centered")
st.markdown("""
    <style>
        body {background-color:#f4f4f4;}
        .stApp {background-color: #505FAD; border-radius: 10px; padding: 20px;}
        h1 {color: #f5fbfa; text-align: center; background-color:#def3ef; border-radius:20px; padding: 10px;}
        .category-button {
            background-color: #ff5733;
            color: white;
            border: none;
            padding: 10px 20px;
            margin: 5px;
            cursor: pointer;
            font-size: 16px;
            border-radius: 5px;
            transition: all 0.3s ease-in-out;
        }
        .category-button:hover {
            background-color: #ff2e00;
            transform: scale(1.1);
        }
        .stSelectbox, .stNumberInput {
            background-color: #fff;
            color: black;
            border-radius: 5px;
            padding: 5px;
        }
            .result-box {
            background-color: #f39c12;
            color: white;
            padding: 10px;
            border-radius: 10px;
            font-size: 18px;
            text-align: center;
            margin-top: 10px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ Unit Converter")
st.markdown("<h3 style='text-align: center; color: #f5fbfa;'>Select a category below to start converting units easily!</h3>", unsafe_allow_html=True)

# Initialize session state for category if not already set
if "selected_category" not in st.session_state:
    st.session_state.selected_category = None

# Categories
categories = ["Length", "Temperature", "Weight", "Volume", "Time"]
col1, col2, col3 = st.columns(3)

for i, cat in enumerate(categories):
    with [col1, col2, col3][i % 3]:
        if st.button(cat, key=cat, help=f"Convert {cat} units"):
            st.session_state.selected_category = cat

if st.session_state.selected_category:
    category = st.session_state.selected_category
    unit_options = {
        "Length": ["Meters", "Kilometers", "Centimeters", "Inches", "Feet"],
        "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
        "Weight": ["Kilograms", "Grams", "Pounds", "Ounces"],
        "Volume": ["Liters", "Milliliters", "Gallons", "Cups"],
        "Time": ["Seconds", "Minutes", "Hours", "Days"]
    }

    from_unit = st.selectbox("From", unit_options[category], key="from_unit")
    to_unit = st.selectbox("To", unit_options[category], key="to_unit")
    value = st.number_input("Enter Value", min_value=0.0, format="%f", key="value")

    if st.button("Convert"):
        result = convert_units(category, from_unit, to_unit, value)
        st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)

