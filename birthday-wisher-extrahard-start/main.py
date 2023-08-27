import random
import pandas as pd
import datetime as dt
import smtplib

MY_EMAIL = "abhishakth007@gmail.com"
MY_PASSWORD = "dkokzpbqludxzddw"
connection  = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=MY_EMAIL,password=MY_PASSWORD)

today = dt.datetime.now()
day_today = today.day
month_today = today.month
year_today = today.year

today_in_format = (month_today, day_today)
df = pd.read_csv("birthdays.csv")

for index, datarow in df.iterrows():
    data_as_tuple = (datarow['month'], datarow['day'])
    if data_as_tuple == today_in_format:
        data_final = df.iloc[index]
        name_of_final = data_final['name']
        email_of_final = data_final['email']
        random_number = random.randint(1,3)
        with open(
                f"letter_templates/letter_{random_number}.txt") as file:
            content = file.read()
            name = name_of_final
            content = content.replace("[NAME]", name)

        connection.sendmail(from_addr=MY_EMAIL,to_addrs=email_of_final,msg=content)
        connection.close()
