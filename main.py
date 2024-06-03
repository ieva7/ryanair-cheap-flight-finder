from data_retrieval import get_airport_codes, get_all_airport_info, get_destinations

if __name__ == "__main__":
    
    airports =  get_all_airport_info()
    codes = get_airport_codes(airports)
    print(codes)


