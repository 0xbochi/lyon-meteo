import requests
import json

# Récupérer les données météorologiques actuelles pour Lyon
response = requests.get('https://api.open-meteo.com/v1/forecast?latitude=45.75&longitude=4.85&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m')

data = response.json()

temperature = data['current_weather']["temperature"]
windSpeed = data['current_weather']["windspeed"]
date = data['current_weather']["time"].split("T")[0]
hours = data['current_weather']["time"].split("T")[1].split(":")[0]

if temperature > 20:
    img = "sun.png"
else:
    img = "rain.png"


with open ("README.md", "w", encoding="utf-8") as f:
    f.write(f'''# METEO À LYON

Dernière update datant du {date} à {hours} heure.  
Il fait actuellement {temperature}°C et le vent souffle à {windSpeed} km/h.      

![](./.github/{img})
''')
