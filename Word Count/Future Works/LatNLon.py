import pandas as pd
from geopy.geocoders import Nominatim
import time

# Load your CSV file
df = pd.read_csv('C:\\Users\\vocat\\Desktop\\Prashant Final Project\\Word Count\\coffee_lat_lon.csv')
print("CSV file loaded successfully.")

# Initialize geolocator
geolocator = Nominatim(user_agent="coffee_locator")

# Function to get latitude and longitude
def get_lat_lon(location):
    try:
        time.sleep(1)  # To respect OpenStreetMap's usage policy
        loc = geolocator.geocode(location)
        if loc:
            return pd.Series([loc.latitude, loc.longitude])
        else:
            return pd.Series([None, None])
    except Exception as e:
        print(f"Error geocoding {location}: {e}")
        return pd.Series([None, None])

# Apply the function to location and origin columns
print("Geocoding locations...")
df[['Location_Latitude', 'Location_Longitude']] = df['location'].apply(get_lat_lon)
df[['Origin_Latitude', 'Origin_Longitude']] = df['origin'].apply(get_lat_lon)
print("Geocoding completed.")

# Save the updated DataFrame to a new CSV
output_path = 'C:/Users/vocat/Desktop/Prashant Final Project/Word Count/coffee_with_lat_lon.csv'
df.to_csv(output_path, index=False)
print(f"CSV file saved successfully to {output_path}.")
