import requests

pixela_url = "https://pixe.la/v1/users"
pixela_token = "abhishakth@99"
pixela_username = "abhishakth"
import datetime as dt

login_credentials = {
    "token": pixela_token,
    "username": pixela_username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_url,json=login_credentials)
# print(response.text)


my_graphs_end_point = f"{pixela_url}/{pixela_username}/graphs"

graphs_token = {
    "X-USER-TOKEN": pixela_token
}

graph_credentials = {"id": "screentimer",
                     "name": "Youtube_Screen_Time",
                     "unit": "minute",
                     "type": "int",
                     "color": "sora",
                     }

# response = requests.post(url=my_graphs_end_point,json=graph_credentials,headers=graphs_token)
# print(response.text)

date = dt.datetime.now()
year_today = date.year
month_today = date.month
day_today = date.day

# formatted_date = f"{year_today}0{month_today}0{day_today}"

graph_values = {"date": "20230730",
                "quantity": "128"
                }


graph_data_url = f"{my_graphs_end_point}/screentimer"

response = requests.post(url=graph_data_url,json=graph_values,headers=graphs_token)

print(response.text)