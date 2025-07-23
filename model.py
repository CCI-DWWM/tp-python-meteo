
import database
from database import connexion
import requests
import sys


# ---- 1. Récupère le nom de la commune depuis le code postal ----
def recup_commune(code_postal):
    db = connexion()
    cursor = db.cursor(buffered=True)  # <-- ici
    query = "SELECT nom_commune FROM communes_cd WHERE code_postal = %s"
    cursor.execute(query, (code_postal,))
    result = cursor.fetchone()
    cursor.close()
    db.close()
    return result[0] if result else None


# ---- 2. Récupère les coordonnées de la ville via l'API Nominatim ----
def get_coords(city_name):
    url = f"https://nominatim.openstreetmap.org/search?format=json&q={city_name}"
    headers = {"User-Agent": "tp-python-meteo"}
    response = requests.get(url, headers=headers)
    data = response.json()
    if data:
        return data[0]['lat'], data[0]['lon']
    return None, None


# ---- 3. Récupère la météo via l’API Open-Meteo ----
def get_meteo(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(url)
    data = response.json()
    return data.get("current_weather", {})


# ---- 4. Test en ligne de commande ----
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python model.py <code_postal>")
    else:
        code_postal = sys.argv[1]
        commune = recup_commune(code_postal)
        print(f"Commune : {commune}")

        if commune:
            lat, lon = get_coords(commune)
            print(f"Coordonnées : {lat}, {lon}")

            if lat and lon:
                meteo = get_meteo(lat, lon)
                print(f"Météo : {meteo}")
            else:
                print("Coordonnées non trouvées.")
        else:
            print("Commune introuvable.")
