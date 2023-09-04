import requests

parameters = {"lat":16.941891,
              "lon":80.788300,
              "appid":'c60316f245d845316119ffd9c7248ddb'}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast",params=parameters)

data = response.json()
print(data)