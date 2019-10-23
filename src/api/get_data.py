"""
Interfaces with db and fetching_api to get data from 
td ameritrades api and add it to our database
"""
from db import MongoWrapper
from fetching_api import Td_API

if __name__ == "__main__":
    print("get_data.py")

    watchlist = ["AAPL", "MSFT", "BABA"]
    periodType = "day"
    frequencyType = "minute"

    m = MongoWrapper("mongodb://192.168.99.100:27017")
    api = Td_API()

    for i, symbol in enumerate(watchlist):
        print("Adding symbol {}: {}".format(i, symbol))

        candles = api.get_historical_data(symbol, periodType, 15, frequencyType)

        m.add_symbol(symbol, candles)

