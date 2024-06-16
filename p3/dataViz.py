import folium
import pandas as pd


data = pd.read_csv('./filtered_data_with_coordinates.csv')
map = folium.Map(location=[36.7783, -119.4179], zoom_start=6)


def get_color(crime):
    if crime < 500:
        return 'green'
    elif 500 <= crime < 1000:
        return 'orange'
    else:
        return 'red'
def get_radius(crime):
    base_size = 4000  
    return base_size + (crime * 5)


for index, row in data.iterrows():
    folium.Circle(
        location=[row['Latitude'], row['Longitude']],
        radius=get_radius(row['Violent crime']),  
        color=get_color(row['Violent crime']),  
        fill=True,
        fill_opacity=0.5,
        popup=f"{row['County']} County<br>Violent Crime: {row['Violent crime']}"
    ).add_to(map)


map.save("california_crime_intensity_map.html")

print("Map with crime intensity markers has been created and saved as 'california_crime_intensity_map.html'")
