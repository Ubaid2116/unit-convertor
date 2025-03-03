import asyncio
import sys
import streamlit as st

# Set event loop policy for Windows
if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# App Title and Description
st.title("Heavy Unit Converter")
st.write("Convert various units with ease using this app.")

# Sidebar for Conversion Category
st.sidebar.markdown("## Unit Converter")
st.sidebar.info("Select a conversion category and input values for conversion.")

# Sidebar selectbox for conversion category
conversion_category = st.sidebar.selectbox(
    "Select Conversion Category",
    ["Length", "Temperature", "Weight", "Speed"]
)

# Length Conversion Function
def convert_length(value, from_unit, to_unit):
    conversion_factors = {
        "meter": 1,
        "kilometer": 1000,
        "centimeter": 0.01,
        "millimeter": 0.001,
        "mile": 1609.34,
        "yard": 0.9144,
        "foot": 0.3048,
        "inch": 0.0254
    }
    try:
        value_in_meters = value * conversion_factors[from_unit]
        result = value_in_meters / conversion_factors[to_unit]
        return result
    except Exception as e:
        st.error("Conversion error: " + str(e))
        return None

# Temperature Conversion Function
def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        temp_c = value
    elif from_unit == "Fahrenheit":
        temp_c = (value - 32) * 5/9
    elif from_unit == "Kelvin":
        temp_c = value - 273.15

    if to_unit == "Celsius":
        return temp_c
    elif to_unit == "Fahrenheit":
        return temp_c * 9/5 + 32
    elif to_unit == "Kelvin":
        return temp_c + 273.15

# Weight Conversion Function
def convert_weight(value, from_unit, to_unit):
    conversion_factors = {
        "kilogram": 1,
        "gram": 0.001,
        "pound": 0.453592,
        "ounce": 0.0283495
    }
    try:
        value_in_kg = value * conversion_factors[from_unit]
        result = value_in_kg / conversion_factors[to_unit]
        return result
    except Exception as e:
        st.error("Conversion error: " + str(e))
        return None

# Speed Conversion Function
def convert_speed(value, from_unit, to_unit):
    conversion_factors = {
        "m/s": 1,
        "km/h": 1/3.6,
        "mph": 0.44704,
        "ft/s": 0.3048
    }
    try:
        value_in_mps = value * conversion_factors[from_unit]
        result = value_in_mps / conversion_factors[to_unit]
        return result
    except Exception as e:
        st.error("Conversion error: " + str(e))
        return None

# Category-specific UI components
if conversion_category == "Length":
    st.header("Length Conversion")
    units = ["meter", "kilometer", "centimeter", "millimeter", "mile", "yard", "foot", "inch"]
    value = st.number_input("Enter value", value=1.0)
    from_unit = st.selectbox("From", units, index=0)
    to_unit = st.selectbox("To", units, index=1)
    if st.button("Convert"):
        result = convert_length(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} = {result} {to_unit}")

elif conversion_category == "Temperature":
    st.header("Temperature Conversion")
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    value = st.number_input("Enter temperature value", value=0.0)
    from_unit = st.selectbox("From", units, index=0)
    to_unit = st.selectbox("To", units, index=1)
    if st.button("Convert"):
        result = convert_temperature(value, from_unit, to_unit)
        st.write(f"{value}° {from_unit} = {result}° {to_unit}")

elif conversion_category == "Weight":
    st.header("Weight Conversion")
    units = ["kilogram", "gram", "pound", "ounce"]
    value = st.number_input("Enter weight value", value=1.0)
    from_unit = st.selectbox("From", units, index=0)
    to_unit = st.selectbox("To", units, index=1)
    if st.button("Convert"):
        result = convert_weight(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} = {result} {to_unit}")

elif conversion_category == "Speed":
    st.header("Speed Conversion")
    units = ["m/s", "km/h", "mph", "ft/s"]
    value = st.number_input("Enter speed value", value=1.0)
    from_unit = st.selectbox("From", units, index=0)
    to_unit = st.selectbox("To", units, index=1)
    if st.button("Convert"):
        result = convert_speed(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} = {result} {to_unit}")

# Footer
st.markdown("---")
st.markdown("Developed by **Muhammad Ubaid Hussain**")

# Custom CSS for styling
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 24px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stSelectbox>div>div>select {
        padding: 10px;
        border-radius: 5px;
    }
    .stNumberInput>div>div>input {
        padding: 10px;
        border-radius: 5px;
    }
    .stMarkdown h1 {
        color: #4CAF50;
    }
    .stMarkdown h2 {
        color: #45a049;
    }
    .stMarkdown h3 {
        color: #45a049;
    }
    </style>
    """,
    unsafe_allow_html=True
)