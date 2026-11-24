import requests
import json
from urllib import response

def get_coordinates(city):
    url = "https://nominatim.openstreetmap.org/search"

    params = {
        "q": city,
        "format": "json",
        "limit": 1
    }

    headers = {
        "User-Agent": "MWCCHARTFORD"
    }
    response = requests.get(
        url,
        params=params,
        headers=headers
    )
    data = response.json()[0]
    print(f"Status Code: {response.status_code}")
    print(f"LATTITUDE: {data['lat']}")
    print(f"LONGITUDE: {data['lon']}")

    return data['lat'], data['lon']

def get_noaa_endpoint(lat, lon):
    url = f"https://api.weather.gov/points/{lat},{lon}"
    headers = {
        "User-Agent": "MWCCHARTFORD"
    }
    response = requests.get(
            url,
    )
    data = response.json()
def get_forcast(url):
    responce = requests.get(url)
    data = response.json()["properties"]["periods"]

    
lat, lon = get_coordinates("Gardner, MA")
get_noaa_endpoint(lat, lon)