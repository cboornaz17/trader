import abc

class Option(Asset):
    def __init__(self, ticker, strike, expirationDate):
        pass

    def getPrice(self):
        """
        Calculates the current price of the option based on the Black Scholes Model
        """

        return 10
