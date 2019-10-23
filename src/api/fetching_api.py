"""
Has functions for fetching data from td ameritrades api
"""
import requests
import json
from authorization import get_access_token, get_config_dict
import threading

class Td_API:
    def __init__(self):    
        self.access_token = self.get_access_token("config.txt")

    def get_access_token(self, config_location):
        config_dict = get_config_dict(config_location)
        return get_access_token(config_dict["client_id"], config_dict["refresh_token"])

    def get_historical_data(self, ticker, periodType, frequency, frequencyType, period=-1, endDate=-1, startDate=-1):
        """
        @param ticker the request ticker
        @param period the number of periodTypes to load data for 
            - not needed if endDate and startDate are provided
        @param periodType the type of period to show, ex "day", "month", "year"
        @param frequency the number of frequencyTypes to load candles for
        @param frequencyType the type of frequency to load ex "minute", 
            "daily", "weekly", "monthly"
        @param endDate the last date to request data for -- not needed if period is provided
        @param startDate the first date to request data for
        """

        
        url = "https://api.tdameritrade.com/v1/marketdata/{}/pricehistory?periodType={}".format(ticker, periodType)
        url += "&frequencyType={}&frequency={}".format(frequencyType, frequency)

        if period != -1:
            url += "&period=" + period
        if endDate != -1:
            url += "&endDate=" + endDate 
        if startDate != -1:
            url += "&startDate=" + startDate

        h = {
            "content-type": 'application/x-www-form-urlencoded',
            "Authorization": "Bearer " + self.access_token
        }

        r = requests.get(url, headers=h)

        return json.loads(r.text)["candles"] 

if __name__ == "__main__":

    api = Td_API()

    response = api.get_historical_data("AAPL", "month", 1, "weekly", period=1)

