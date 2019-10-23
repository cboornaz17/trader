"""
Runs a simulation on data in the mongo database
"""
import pymongo

# TODO: parametrize with time
def get_candles(symbol):
    pass




if __name__ == "__main__":
    
    """
    Set parameters
    """
    balance = 10000
    startDate=('2019-08-07')
    endDate=('2019-10-21')

    # change this and the other watchlist to read from a file
    watchlist = ["AAPL", "BABA", "MSFT"]  

    maxDailyVolume = 500    
    interval = 15 # minutes

    data = []
    
    portfolio = Portfolio(balance)
    """
    Run simulation
    """
    for stock in watchlist:

        """
        Check for buy signals
        """
        for candle in data:
            # check for buy signal, buy if we can
            break
        

        """
        Check for sell signals 
        """
        for asset in portfolio.holdings:
            # check for sell signals, sell if we can
            break
    


        




