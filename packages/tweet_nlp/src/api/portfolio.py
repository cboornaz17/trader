"""
A portfolio can hold options or stocks. 
Manages balance through buys and sells
"""
class Portfolio():

    def __init__(self, start_balance):
        self.balance = start_balance
        # portfolio maps symbol to list of holdings
        self.holdings = dict()

    def buy(symbol, asset):
        """
        Adds an asset object to our portfolio and updates balance
        """
        self.balance -= asset.price
        self.holdings[symbol] = []

    
    def sell(symbol, asset):
        """
        Removes an asset object from our portfolio and updates balance
        """
        if asset in self.portfolio[symbol]:
            self.balance += asset.getPrice()
            del self.holdings[symbol]
