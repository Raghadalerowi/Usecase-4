import streamlit as st

st.title('Use case 4 FastAPI')

# Add a header
st.header('Welcome')

# Add some text
st.write('SFA streamlit app')

# Create an input field
Year =  st.number_input("Enter THE Year", min_value=2000, max_value=2100, value=2000)

Engine_Size = st.number_input("Enter your Engine_Size", value=100)

Mileage = st.number_input("Enter THE Mileage",value=0)

Type = st.text_input("What's The Type?",value='LandCruiser')

Make = st.text_input("What's The Brand?",value='Hyundai') 

Options = st.text_input("What's It's Options?")

Options = st.selectbox("What The Options?", ["Full", "Standard"])
st.write("What The Options?:")


# Add a slider
age = st.slider('Select your age', 0, 100, 25)

# Display selected age
st.write(f'You selected age: {age}')

# Add a button
if st.button('Click me'):
    st.write('You clicked the button!')

