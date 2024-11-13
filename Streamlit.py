# import streamlit as st
# import requests 

# st.title('Use case 4 FastAPI')

# # Add a header
# st.header('Welcome')

# # Add some text
# st.write('SFA streamlit app')

# # Create an input field
# Year =  st.number_input("Enter THE Year", min_value=2000, max_value=2100, value=2000)

# Engine_Size = st.number_input("Enter your Engine_Size", value=100)

# Mileage = st.number_input("Enter THE Mileage",value=0)

# Type = st.text_input("What's The Type?",value='LandCruiser')

# Make = st.text_input("What's The Brand?",value='Hyundai') 

# Options = st.selectbox("What The Options?", ["Full", "Standard"])
# st.write("What The Options?:")

# if st.button('Submit Car Info'):
#     # Preparing the data in a dictionary format
#     car_data = {
#         "Year": Year,
#         "Engine_Size": Engine_Size,
#         "Mileage": Mileage,
#         "Type": Type,
#         "Make": Make,
#         "Options": Options
#     }
    
#     # Sending a POST request to the FastAPI server
#     try:
#         response = requests.post("https://ml-7joy.onrender.com/predict", json=car_data)
        
#         # Check the response status
#         if response.status_code == 200:
#             data = response.json()
#             st.success("Car data sent successfully!")
#             st.write("Response from FastAPI server:")
#             st.json(data)
#         else:
#             st.error("Error sending data to the FastAPI server.")
#     except requests.exceptions.RequestException as e:
#         st.error(f"Request error: {e}")



import streamlit as st
import requests

#Set up the Streamlit app
st.title("Car Price Prediction")

#User inputs
year = st.number_input("Year", min_value=1980, max_value=2024, value=2020)
engine_size = st.number_input("Engine Size (L)", min_value=0.5, max_value=10.0, value=2.5)
mileage = st.number_input("Mileage", min_value=0, max_value=500000, value=15000)
car_type = st.selectbox("Type", ["Accent", "Land Cruiser"])  # Add other types as necessary
make = st.selectbox("Make", ["Hyundai", "Mercedes"])  # Add other makes as needed
options = st.selectbox("Options", ["Full", "Standard"])  # Adjust according to options in your data

#Prediction button
if st.button("Predict Price"):
    # API request URL
    url = "https://ml-7joy.onrender.com/predict"

#Data for the POST request
    data = {
        "Year": year,
        "Engine_Size": engine_size,
        "Mileage": mileage,
        "Type": car_type,
        "Make": make,
        "Options": options
    }

    # Send the POST request
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Check for request errors
        prediction = response.json()  # Parse JSON response
        # {'Cheap_Price': 0, 'Good_Price': 1, 'High_Price': 2}

        if prediction['pred'] == 0:
            prediction = "Cheap Price"
        elif prediction['pred'] == 1:
            prediction = "Good Price"
        elif prediction['pred'] == 2:
            prediction = "High Price"

        st.write(f"Estimated Price: {prediction}")
    except requests.exceptions.RequestException as e:
        st.error("Error requesting prediction from API. Please try again.")
        st.write(e)