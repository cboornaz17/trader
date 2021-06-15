"""
Each class represents a collection in the mongoDB. Some classes are linked.
"""
from mongoengine import *

class Symbol(Document):
    symbol = StringField(required=True)
    trading = BooleanField(required=True)
    price_levels = ListField(ReferenceField(PriceLevel))
    # trades = ListField(ReferenceField(Trade))
    # trades get created with symbols and then are automatically

    meta = {"db_alias": "trader", 'collection': 'symbols'}

class PriceLevel(Document):
    # support and resistance represented by a mean price and standard deviation
    price = DecimalField(min_value=0, precision=2)
    # price_sd = DecimalField(min_value=0, precision=2)
    tests = ListField(ReferenceField(Test))

    # eventually want a function for automatically updating and creating price levels
    # same function that is creating indicators

    meta = {"db_alias": "trader", 'collection': 'priceLevels'}

class Test(Document):
    # the length of time from the start of the test to the end
    length = IntField()
    # list of candles representing this test
    candles = ListField(ReferenceField(Candle))

    # may want to represent the "strength" of this test with values like min distance, etc.
    # I think only referencing the candles leaves it up to more specfic decisions later

    meta = {"db_alias": "trader", 'collection': 'tests'}

class Candle(Document):
    # plain price stats
    open = DecimalField(min_value=0, precision=2)
    close = DecimalField(min_value=0, precision=2)
    high = DecimalField(min_value=0, precision=2)
    low = DecimalField(min_value=0, precision=2)
    # would be interesting to have a function for weighting these into a "market" for all the analysis

    volume = IntField()
    symbol = ReferenceField(WatchedSymbol)
    indicators = DictField()
    # indicators = ReferenceField(Indicators)

    meta = {"db_alias": "trader", 'collection': 'candles'}

# class Trade(Document):

# once we have the indicators decided, something like this can be used
# class Indicators(Document):
#     smas = DictField()
#     rsi = DecimalField(min_value=0, precision=2)
#     # other indicators
