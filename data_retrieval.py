import requests

def get_flight_info():
    return requests.get("https://www.ryanair.com/api/views/locate/5/airports/en/active").json()


print(get_flight_info())