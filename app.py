import requests
import joblib
import pandas as pd

# Function to get Latitude and Longitude from City Name
def get_lat_long(city):
    api_key = 'a887d685616547ff8705df911a1dc2af'  # Ensure this is a valid OpenCage API key
    base_url = f'https://api.opencagedata.com/geocode/v1/json?q={city}&key={api_key}'
    
    response = requests.get(base_url)
    data = response.json()

    # Print the full response for debugging
    print(f"API Response for city '{city}':", data)
    
    if response.status_code == 200 and data['results']:
        lat = data['results'][0]['geometry']['lat']
        lon = data['results'][0]['geometry']['lng']
        return lat, lon
    else:
        print("Error: City not found or invalid API key.")
        return None, None

# Load the trained model
model = joblib.load('gradient_boosting_model.joblib')

# Function to fetch air pollution data
def fetch_air_pollution_data(lat, lon):
    url = f'http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid=08a74ea90aeda287a529e19ab5975d38'
    response = requests.get(url)
    
    if response.status_code == 200:
        result = response.json()
        rtdata = result['list'][0]['components']
        
        # Convert keys to match the training data feature names, using the requested order
        adjusted_rtdata = {
            'PM2.5': rtdata['pm2_5'],
            'PM10': rtdata['pm10'],
            'NO': rtdata['no'],
            'NO2': rtdata['no2'],
            'NH3': rtdata['nh3'],
            'CO': rtdata['co'],
            'SO2': rtdata['so2'],
            'O3': rtdata['o3'],
        }
        return adjusted_rtdata
    else:
        print("Failed to fetch air pollution data.")
        return None

# Streamlit app layout
def run_app():
    import streamlit as st # type: ignore

    st.title("AQI Prediction Based on City or Latitude and Longitude")
    st.write("You can either enter a city name or input latitude and longitude directly to get today's AQI prediction.")

    search_method = st.selectbox("Select search method", ["Search by City Name", "Search by Latitude and Longitude"])

    if search_method == "Search by City Name":
        city = st.text_input("Enter city name", "Enter city").strip().lower()  # Handle extra spaces or case sensitivity
        
        if st.button("Get AQI Prediction"):
            lat, lon = get_lat_long(city)
            
            if lat and lon:
                st.write(f"Latitude: {lat}, Longitude: {lon}")
                data = fetch_air_pollution_data(lat, lon)
                
                if data:
                    feature_order = ['PM2.5', 'PM10', 'NO', 'NO2', 'NH3', 'CO', 'SO2', 'O3']
                    data_df = pd.DataFrame([data])[feature_order]
                    aqi_prediction = model.predict(data_df)
                    st.write(f"Predicted AQI for {city}: {aqi_prediction[0]:.2f}")
                else:
                    st.error("Failed to fetch air pollution data.")
            else:
                st.error("City not found. Please try again.")
    
    elif search_method == "Search by Latitude and Longitude":
        lat = st.number_input("Enter latitude", min_value=-90.0, max_value=90.0, value=21.0, step=0.1)
        lon = st.number_input("Enter longitude", min_value=-180.0, max_value=180.0, value=77.1, step=0.1)

        if st.button("Get AQI Prediction"):
            data = fetch_air_pollution_data(lat, lon)
            
            if data:
                feature_order = ['PM2.5', 'PM10', 'NO', 'NO2', 'NH3', 'CO', 'SO2', 'O3']
                data_df = pd.DataFrame([data])[feature_order]
                aqi_prediction = model.predict(data_df)
                st.write(f"Predicted AQI for the location ({lat}, {lon}): {aqi_prediction[0]:.2f}")
            else:
                st.error("Failed to fetch air pollution data.")

if __name__ == "__main__":
    run_app()
