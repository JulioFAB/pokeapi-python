import requests
#Filtrar pokemon por tipo
respuesta = requests.get("https://pokeapi.co/api/v2/type/water")
datos = respuesta.json()

for p in datos["pokemon"][:3]:
    print(p["pokemon"]["name"])

#filtrar pokemon por nombre
respuesta = requests.get("https://pokeapi.co/api/v2/pokemon/charmander")
datos = respuesta.json()

print("Nombre:", datos["name"])


#Datos completos

respuesta = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
datos = respuesta.json()

print("Nombre:", datos["name"])

print("Tipos:")
for t in datos["types"]:
    print("-", t["type"]["name"])

print("Habilidades:")
for h in datos["abilities"]:
    print("-", h["ability"]["name"])

print("Movimientos:")
for m in datos["moves"][:3]:
    print("-", m["move"]["name"])

