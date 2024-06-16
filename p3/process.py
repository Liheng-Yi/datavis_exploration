import pandas as pd
from geopy.geocoders import Photon
import time  

geolocator = Photon(user_agent="geoapiExercises")
file_path = './filtered_data.csv'
df = pd.read_csv(file_path)

def get_lat_lon(county_name):
  query = f"{county_name} County, California"
  location = geolocator.geocode(query)
  return location.latitude, location.longitude

df['Latitude'], df['Longitude'] = zip(*df['County'].apply(get_lat_lon))
df.to_csv('./p3/filtered_data_with_coordinates.csv', index=False)
