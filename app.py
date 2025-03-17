import streamlit as st
from pint import UnitRegistry

# Initialize unit registry
ureg = UnitRegistry()

# Streamlit UI
st.title("Unit Converter App")
st.write("Convert between different units easily!")

# Conversion Categories
categories = ["Length", "Weight", "Temperature", "Speed"]
selected_category = st.selectbox("Select a category", categories)

# Define unit options based on category
unit_options = {
    "Length": ["meter", "kilometer", "mile", "yard", "foot", "inch"],
    "Weight": ["gram", "kilogram", "pound", "ounce"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Speed": ["meter per second", "kilometer per hour", "mile per hour"]
}

# User Input
input_value = st.number_input("Enter value", value=1.0, format="%.2f")
from_unit = st.selectbox("From unit", unit_options[selected_category])
to_unit = st.selectbox("To unit", unit_options[selected_category])

# Convert and Display Result
if st.button("Convert"):
    try:
        if selected_category == "Temperature":
            # Special conversion for temperature
            if from_unit == "celsius" and to_unit == "fahrenheit":
                result = (input_value * 9/5) + 32
            elif from_unit == "celsius" and to_unit == "kelvin":
                result = input_value + 273.15
            elif from_unit == "fahrenheit" and to_unit == "celsius":
                result = (input_value - 32) * 5/9
            elif from_unit == "fahrenheit" and to_unit == "kelvin":
                result = (input_value - 32) * 5/9 + 273.15
            elif from_unit == "kelvin" and to_unit == "celsius":
                result = input_value - 273.15
            elif from_unit == "kelvin" and to_unit == "fahrenheit":
                result = (input_value - 273.15) * 9/5 + 32
            else:
                result = input_value  # Same unit
        else:
            # Convert using Pint for other categories
            result = (input_value * ureg(from_unit)).to(to_unit).magnitude
        
        st.success(f"{input_value} {from_unit} = {result:.2f} {to_unit}")
    except Exception as e:
        st.error(f"Conversion error: {e}")
        
