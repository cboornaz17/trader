# trader
This project will eventually be an algorithmic options trader.


## Sub projects

### Data Collection
We need to get candle data for stocks in our watchlist for a given amount of time. Unfortunately, TD Ameritrade does not provide historical volatility data (needed for Black Scholes calculations), so we may need to search somewhere else for this.

### Indicator Generation
We will add the indicators we use to trade (RSI, SMA, etc.) and add them in place to our data tables. This will allow our algorithm to process them without needing to recalculate them at every step.

### Algorithm Creation
Our algorithm will:
- Iterate over candle and indicator data, generating a sentiment value (-1, 1) for each candle
- Make a distribution of expected price of the stock
- Iterate over a subset of available options to pick the best risk/reward contract. We need to check different expirations and different strike prices
- ...
- Given portfolio holdings, decide when to exit trades. This decision should be based on the sentiment value at that time as well as the risk/reward set for the trade on entry or simulation start.


### Algorithm Simulation
Given the algorithm, the simulation should take in a starting value and some other parameters, and tell us how the strategy did.

