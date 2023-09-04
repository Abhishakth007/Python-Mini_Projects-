import requests
import os
from twilio.rest import Client


acc_sid = #Your Acc_Sid
acc_token = #Your Auth_Token
twilio_phone_number = #Twitch Mobile_Number
my_number = #Your Mobile Number


parameters = {"lat":22.3072,
              "lon":73.1812,
              "appid":'c60316f245d845316119ffd9c7248ddb'}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast",params=parameters)

data = response.json()
weather_hourly = data["list"][:12]
# weather_hourly = data["list"][0]["weather"][0]["id"]

total_of_data = 0

for hour_data in weather_hourly:
    all_hours_data_id = hour_data["weather"][0]["id"]
    total_of_data+=all_hours_data_id

average_of_data = int(total_of_data/12)
print("Sms Has Been Sent To Your Registered Mobile_Number")
if average_of_data<700:
    print("Sms Has Been Sent To Your Registered Mobile_Number")
    client = Client(acc_sid, acc_token)
    message= client.messages \
            .create(body="Carry Your Umbrella Bro..Its Gonna Rain Today ☔",from_=twilio_phone_number,to=my_number)
