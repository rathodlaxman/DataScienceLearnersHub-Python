pip install folium


import folium

# Create a base map centered at a specific location
map_center = [37.7749, -122.4194]  # San Francisco
my_map = folium.Map(location=map_center, zoom_start=12)

# Display the map
my_map
