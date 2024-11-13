import streamlit as st

st.title('Use case 4 FastAPI')

# Add a header
st.header('Welcome')

# Add some text
st.write('SFA streamlit app')

# Create an input field
Year =  st.number_input("Enter your Year", min_value=2000, max_value=2100, value=2000)

Engine_Size = st.text_input("What's your name?")

Mileage = st.text_input("What's your name?")

Type = st.text_input("What's your name?")

Make = st.text_input("What's your name?")

Options = st.text_input("What's your name?")

# Display the input
if name:
    st.write(f'Hello, {name}!')

# Add a slider
age = st.slider('Select your age', 0, 100, 25)

# Display selected age
st.write(f'You selected age: {age}')

# Add a button
if st.button('Click me'):
    st.write('You clicked the button!')

