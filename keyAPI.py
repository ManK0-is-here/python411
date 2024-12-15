import requests
from plyer import notification
# from urllib import response


url = r'https://api.openweathermap.org/data/2.5/weather?q=Череповец&appid=23496c2a58b99648af590ee8a29c5348&units=metric&lang=ru'

respons = requests.get(url)

weather_dict = respons.json()
# температура
temp = weather_dict['main']['temp']
# ощущение температуры
feels_like = weather_dict['main']['feels_like']
# что на улице
description =weather_dict['weather'][0]['description']

print(f"температура: {temp}, ощущается как: {feels_like}, описание: {description}")

notification.notify(
    title = "Погода в Череповце",
    message = f"температура: {temp}, ощущается как: {feels_like}, описание: {description}",
    app_name = 'Weather',
    app_icon = None
    )