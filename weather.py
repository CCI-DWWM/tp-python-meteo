import requests

def get_weather(city_name):
    # Étape 1 : Obtenir les coordonnées avec Nominatim
    nominatim_url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": city_name,
        "format": "json",
        "limit": 1
    }

    response = requests.get(nominatim_url, params=params, headers={"User-Agent": "tp-meteo"})
    response.raise_for_status()
    data = response.json()

    if not data:
        return {"error": "Ville non trouvée"}

    latitude = data[0]['lat']
    longitude = data[0]['lon']

    # Étape 2 : Obtenir la météo avec Open-Meteo
    meteo_url = "https://api.open-meteo.com/v1/forecast"
    meteo_params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True
    }

    meteo_response = requests.get(meteo_url, params=meteo_params)
    meteo_response.raise_for_status()
    meteo_data = meteo_response.json()

    return meteo_data["current_weather"]
