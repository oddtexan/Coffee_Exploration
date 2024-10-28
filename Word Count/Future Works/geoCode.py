import pandas as pd
import requests
from dotenv import load_dotenv
import os

# Load your CSV file
df = pd.read_csv('C:\\Users\\vocat\\Desktop\\Prashant Final Project\\Word Count\\coffee_lat_lon.csv')
print("CSV file loaded successfully.")

# Your Geoapify API key
load_dotenv()
api_key = os.getenv("API_KEY")

# Function to get latitude and longitude using Geoapify API
def get_lat_lon(location, api_key):
    base_url = "https://api.geoapify.com/v1/geocode/search"
    params = {
        "text": location,
        "apiKey": api_key
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Check if request was successful
        results = response.json()
        if results['features']:
            # Extract latitude and longitude from the first feature
            lat = results['features'][0]['properties']['lat']
            lon = results['features'][0]['properties']['lon']
            return pd.Series([lat, lon])
        else:
            return pd.Series([None, None])
    except Exception as e:
        print(f"Error geocoding {location}: {e}")
        return pd.Series([None, None])

# Apply the function to location and origin columns
print("Geocoding locations...")
df[['Location_Latitude', 'Location_Longitude']] = df['location'].apply(get_lat_lon, api_key=api_key)
df[['Origin_Latitude', 'Origin_Longitude']] = df['origin'].apply(get_lat_lon, api_key=api_key)
print("Geocoding completed.")

# Save the updated DataFrame to a new CSV
output_path = 'C:/Users/Krissy/Bootcamp/Coffee-Exploration---Project-4/Data/coffee_with_lat_lon.csv'
df.to_csv(output_path, index=False)
print(f"CSV file saved successfully to {output_path}.")
