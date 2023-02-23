import streamlit as st

# Define function for each operation
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except :
        print("Erreur")

# Main function to run the calculator
def run_calculator():
    st.title("Simple Calculator")

    # Get user inputs
    a = st.number_input("Enter first number",value=0 )
    b = st.number_input("Enter second number",value=0)

    # Select the operation
    operation = st.selectbox("Select operation", ["Addition", "Subtraction", "Multiplication", "Division"])

    result = 0

    # Perform the operation
    if operation == "Addition":
        result = add(a, b)
    elif operation == "Subtraction":
        result = subtract(a, b)
    elif operation == "Multiplication":
        result = multiply(a, b)
    elif operation == "Division":
        result = divide(a, b)

    # Display the result
    st.write("Result:", result)
    st.markdown("Thanks for :blue[visiting]")


run_calculator()
