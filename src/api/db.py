"""
Manages communication with our mongo database

Should support functions to find, update, etc.
"""
# from pymongo import MongoClient

# class MongoWrapper():
#
#     def __init__(self, conn_string):
#         """
#         Starts a mongo wrapper with the provided conn string
#         """
#         self.client = MongoClient(conn_string)
#         self.db = self.client.trader
#
#     def add_symbol(self, symbol, data, dropCollection=True):
#         """
#         @param symbol: the stock symbol to add data for
#         @param data: the candles list returned from tdameritrade containing
#         the candles for the symbol
#
#         Adds data to a mongo database
#         """
#         symbol_collection = self.db[symbol]
#
#         if dropCollection:
#             symbol_collection.drop()
#
#         x = symbol_collection.insert_many(data)
#
#
#     def get_symbol(self, symbol, startTime, endTime=-1):
#         """
#         @param symbol: the stock symbol to fetch for
#         @param startTime: the oldest time to fetch data from
#         @param endTime: up until when to fetch for
#         """
#         symbol_collection = self.db[symbol]

from MongoClasses import *

# needs to connect somewhere at the begining of the newly gathered data being sent to db
# like connect('trader', host='192.168.99.101', port=27018)

def add_candles(symbol, data, dropCollection=True):
    """
    @param symbol: the stock symbol to add data for
    @param data: the candles list returned from tdameritrade containing
    the candles for the symbol

    Adds data to a mongo database
    """

    # candles = Candle.objects(symbol = symbol)

    # for candle in data:
    #     create candle object
    #     generate indicators? or will this be in data already
    #     save candle object to db


def get_symbol(symbol, startTime, endTime=-1):
    """
    @param symbol: the stock symbol to fetch for
    @param startTime: the oldest time to fetch data from
    @param endTime: up until when to fetch for
    """

    # will symbol be
    # symbol_obj = Symbol.objects(symbol = symbol)
    # Candle.objects(symbol = symbol_obj.symbol)
    Candle.objects(symbol = symbol)

# find newest candle
def get_newest_candle(symbol):
    # I think that the tdapi requester should check for the newest candle of a symbol in the db to know how far back to request
    pass
