import streamlit as st
import requests 

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

Options = st.selectbox("What The Options?", ["Full", "Standard"])
st.write("What The Options?:")

if st.button('Submit Car Info'):
    # Preparing the data in a dictionary format
    car_data = {
        "Year": Year,
        "Engine_Size": Engine_Size,
        "Mileage": Mileage,
        "Type": Type,
        "Make": Make,
        "Options": Options
    }
    
    # Sending a POST request to the FastAPI server
    try:
        response = requests.post("https://ml-7joy.onrender.com/predict", json=car_data)
        
        # Check the response status
        if response.status_code == 200:
            data = response.json()
            st.success("Car data sent successfully!")
            st.write("Response from FastAPI server:")
            st.json(data)
        else:
            st.error("Error sending data to the FastAPI server.")
    except requests.exceptions.RequestException as e:
        st.error(f"Request error: {e}")