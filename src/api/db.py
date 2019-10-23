"""
Manages communication with our mongo database

Should support functions to find, update, etc.
"""
from pymongo import MongoClient

class MongoWrapper():

    def __init__(self, conn_string):
        """
        Starts a mongo wrapper with the provided conn string
        """
        self.client = MongoClient(conn_string)
        self.db = self.client.trader

    def add_symbol(self, symbol, data, dropCollection=True):
        """
        @param symbol: the stock symbol to add data for
        @param data: the candles list returned from tdameritrade containing
        the candles for the symbol

        Adds data to a mongo database
        """        
        symbol_collection = self.db[symbol]
        
        if dropCollection:
            symbol_collection.drop()
        
        x = symbol_collection.insert_many(data)


    def get_symbol(self, symbol, startTime, endTime=-1):
        """
        @param symbol: the stock symbol to fetch for
        @param startTime: the oldest time to fetch data from
        @param endTime: up until when to fetch for
        """
        symbol_collection = self.db[symbol]


    




