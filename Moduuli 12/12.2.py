import requests
import json

hakusana = input('Syötä kaupunki:')
API_key = '0df93e3d51dcaad2960a6d7045efba8f'
pyyntö = f'https://api.openweathermap.org/data/2.5/weather?q={hakusana}&appid={API_key}'
vastaus = requests.get(pyyntö).json()
print(json.dumps(vastaus, indent=2))

print(f'Kaupungissa {hakusana} sää on:')
sää = vastaus["weather"][0]["description"]
celsius = vastaus["main"]["temp"]/273.15
print(sää)
print(f'{celsius:.3} C')