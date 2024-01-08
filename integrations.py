import requests

WEATHER_TOKEN = "ded26c28088c4f33343d16dd29e9257a"


def get_weather_data(city):
    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_TOKEN}")
    if response.status_code == 200:
        data = response.json()
        city = data['name']
        main = data['weather'][0]['main']
        temp = round(data['main']['temp'] - 273, 2)
        speed = data['wind']['speed']
        text = (f"<b>Shahar nomi</b>: {city}\n"
                f"<u>Havo hakida</u>: {main}\n"
                f"Temperatura: {temp}gradus\n"
                f"Tezliki: {speed}")
      
    