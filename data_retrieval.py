import requests

def get_all_airport_info() -> list:
    """returns a list of full airport information.
    format: {'code': 'XRY', 'name': 'Jerez', 'seoName': 'jerez', 'aliases': [], 'base': False, 'city': {'name': 'Jerez', 'code': 'JEREZ'}, 'region': {'name': 'Andalusia', 'code': 'ANDALUSIA'}, 'country': {'code': 'es', 'iso3code': 'ESP', 'name': 'Spain', 'currency': 'EUR', 'defaultAirportCode': 'BCN', 'schengen': True}, 'coordinates': {'latitude': 36.7446, 'longitude': -6.06011}, 'timeZone': 'Europe/Madrid'}"""
    country_list = requests.get("https://www.ryanair.com/api/views/locate/5/airports/en/active").json()
    return country_list


def get_airport_codes(airport_info: list) -> list:
    """Returns a list of Airport codes"""

    return 0


def get_destinations(origin: str) -> list:
    """Returns all destinations using an origin airport code"""

    return requests.get(f"https://www.ryanair.com/api/views/locate/searchWidget/routes/en/airport/{origin}").json()

airports =  get_all_airport_info()
print(get_destinations('KUN'))