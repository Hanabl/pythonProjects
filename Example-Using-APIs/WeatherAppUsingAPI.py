import requests , webbrowser 
from datetime import datetime , timezone
from geopy.geocoders import Nominatim


username = 'myself_abl_hana'
password = 'EtqZJ48Uf3'
currentTime = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

# Set locator using Nominatim 
geolocator = Nominatim(user_agent="MyWeatherApp/1.0 (haniyeh@gmail.com)")

# Convert address to geographic coordinates
location = geolocator.geocode("Tehran, Iran")
latitude = location.latitude
longitude = location.longitude

url = F"https://api.meteomatics.com/{currentTime}/t_2m:C/{latitude},{longitude}/html"

if location:
    print(url)
else:
    print("Not Found")
    
    
response = requests.get(url, auth=(username, password))

if response.status_code == 200:
    print(response.text)
    with open("weather.html", "w") as file:
        file.write(response.text)
    webbrowser.open("weather.html")
    
else:
    print(f"ERROR: {response.status_code}")
    print(response.text)