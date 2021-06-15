import abc

class Option(Asset):
    def __init__(self, ticker, strike, expirationDate):
        self.ticker = ticker
        self.strike = strike
        self.expirationDate = expirationDate
        
    def getPrice(self):
        """
        Calculates the current price of the option based on the Black Scholes Model
        """

        return 10
