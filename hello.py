import asyncio
import sys

if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Ab baaki imports aur Streamlit code
import streamlit as st

st.title("Heavy Unit Converter")
st.write("Is app ke zariye aap mukhtalif units ka conversion kar sakte hain.")

# Sidebar se conversion category select karen
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

# Sidebar Information
st.sidebar.markdown("## Unit Converter")
st.sidebar.info("Conversion category select karen aur values input karen conversion ke liye.")
