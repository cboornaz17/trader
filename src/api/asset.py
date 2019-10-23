"""
Asset interface -- inherited by option and stock
"""
import abc

class Asset(abc.ABC):
    def __init__(self):
        pass 

    @abc.abstractmethod
    def getPrice(self):
        """
        returns the price of the asset
        """
        pass
