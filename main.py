import os
import csv
from data_retrieval import get_airport_codes, get_all_airport_info, get_destinations, get_flight_pairs


if __name__ == "__main__":
    
    if not os.path.isfile('data.csv'):
        airports =  get_all_airport_info()
        codes = get_airport_codes(airports)
        pairs = get_flight_pairs(codes)
        with open('data.csv', 'w', newline='') as file:
            fieldnames = ['FROM', 'TO']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for pair in pairs:
                writer.writerow({'FROM': pair[0], 'TO': pair[1]})
    else:
        print('file exists!')


