from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="gma")

lista = ["malaspina, 396, Rio Gallegos, Argentina",
"Cristobal Colon, 107, Rio Gallegos, Argentina",
"Cecilia Grierson, 761, Rio Gallegos, Argentina",
"Estrada, 834, Rio Gallegos, Argentina",
"Hernan Cortez, 2338, Rio Gallegos, Argentina",
"Mexico, 1539, Rio Gallegos, Argentina"]

for x in lista:
    location - geolocator.geocode(x)
    print((location.latitude, location.longitude))
    print(location.address)