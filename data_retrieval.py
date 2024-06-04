"""Methods to do with data retrieval from API: https://www.postman.com/hakkotsu/workspace/ryanair/collection/5803268-7bd93177-aa05-4cb2-aed9-ed27e693f83e"""
import requests
import csv

def get_all_airport_info() -> list:
    """returns a list of full airport information.
    format: {'code': 'XRY', 'name': 'Jerez', 'seoName': 'jerez', 'aliases': [], 'base': False, 'city': {'name': 'Jerez', 'code': 'JEREZ'}, 'region': {'name': 'Andalusia', 'code': 'ANDALUSIA'}, 'country': {'code': 'es', 'iso3code': 'ESP', 'name': 'Spain', 'currency': 'EUR', 'defaultAirportCode': 'BCN', 'schengen': True}, 'coordinates': {'latitude': 36.7446, 'longitude': -6.06011}, 'timeZone': 'Europe/Madrid'}"""
    
    country_list = requests.get("https://www.ryanair.com/api/views/locate/5/airports/en/active").json()
    return country_list


def get_airport_codes(airport_info: list) -> list:
    """Returns a list of Airport codes"""

    codes = list()
    for airport in airport_info:
        try:
            codes.append(airport['code'])
        except:
            print(airport)
    return codes


def get_arrival_airport_codes(airport_info: list) -> list:
    """Returns a list of Airport codes"""

    codes = list()
    for airport in airport_info:
        try:
            codes.append(airport['arrivalAirport']['code'])
        except:
            print(airport)
    return codes


def get_destinations(origin: str) -> list:
    """Returns all destinations using an origin airport code"""

    return requests.get(f"https://www.ryanair.com/api/views/locate/searchWidget/routes/en/airport/{origin}").json()


def get_flight_pairs(airport_codes:list) -> list:
    """Finds all destinations from every airport"""

    flight_pairs = list()
    for code in airport_codes:
        destinations = get_destinations(code)
        codes = get_arrival_airport_codes(destinations)
        for dest_code in codes:
            flight_pairs.append((code, dest_code))
    return flight_pairs