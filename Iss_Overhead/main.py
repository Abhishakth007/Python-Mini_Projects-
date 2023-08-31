import requests
import smtplib
import datetime as dt

today = dt.datetime.now()
year_now = today.year
month_now = today.month
day_today = today.day
time_now = today.time()
MY_LATITUDE = 22.2966
MY_LONGITUDE = 73.2375
MY_EMAIL = "abhishakth007@gmail.com"
MY_PASSWORD = "dkokzpbqludxzddw"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=MY_EMAIL,password=MY_PASSWORD)

response = requests.get("http://api.open-notify.org/iss-now.json")
iss_data = response.json()

iss_latitude = iss_data["iss_position"]["latitude"]
iss_longitude = iss_data["iss_position"]["longitude"]

my_position = (float(iss_latitude), float(iss_longitude))  # Change it to MY_LATITUDE,MY_LONGITUDE to check for your location
iss_position = (float(iss_latitude), float(iss_longitude))


if my_position == iss_position:
    connection.sendmail(from_addr=MY_EMAIL,to_addrs="abhishakth0007@gmail.com",msg=f"Subject:From..ISS\n\nAt the time {day_today}/{month_now}/{year_now} Time:{time_now} "
                                                                                   "ISS is currrently above your head")
    connection.close()
