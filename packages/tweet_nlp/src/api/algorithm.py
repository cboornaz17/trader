import math
import numpy as np 
import random 

# Return the value of the Gaussian probability function with mean 0.0
# and standard deviation 1.0 at the given x value.

def phi(x):
    return math.exp(-x * x / 2.0) / math.sqrt(2.0 * math.pi)

# Return the value of the Gaussian probability function with mean mu
# and standard deviation sigma at the given x value.

def pdf(x, mu=0.0, sigma=1.0):
    return phi((x - mu) / sigma) / sigma

# Return the value of the cumulative Gaussian distribution function
# with mean 0.0 and standard deviation 1.0 at the given z value.

def Phi(z):
    if z < -8.0: return 0.0
    if z >  8.0: return 1.0
    total = 0.0
    term = z
    i = 3
    while total != total + term:
        total += term
        term *= z * z / float(i)
        i += 2
    return 0.5 + total * phi(z)

# Return standard Gaussian cdf with mean mu and stddev sigma.
# Use Taylor approximation.

def cdf(z, mu=0.0, sigma=1.0):
    return Phi((z - mu) / sigma)

# Black-Scholes formula.

def callPrice(s, x, r, sigma, t):
    a = (math.log(s/x) + (r + sigma * sigma/2.0) * t) / \
        (sigma * math.sqrt(t))
    b = a - sigma * math.sqrt(t)
    return s * cdf(a) - x * math.exp(-r * t) * cdf(b)
    # N (d1) St - N (d2) PV (K)
    # s = St
    # PV 


def getVolatility(prices):
    """
    takes in a list of prices and calculates the volatility of the stock on the last provided day
    """
    n = len(prices)
    avg = np.average(prices)

    variance = np.sum((np.abs(n - avg) ) ** 2) / n
    print("variance: {}".format(variance))

    daily_vol = math.sqrt(variance)
    print("daily volatility: {}".format(daily_vol))


    return np.average(prices)


def getRandomPrices(steps, startPrice, changeRange):
    """
    Returns an array of random prices 
    """

    ret = [startPrice]
    curr = startPrice
    for i in range(steps):
        change = random.randint(-changeRange, changeRange)
        curr += change 
        ret.append(curr)

    return ret


if __name__ == "__main__":

    # this is wrong i think
    #print(callPrice(299.01, 302, .12, .1392, (9 / 365)))

    prices = getRandomPrices(50, 300, 5)
    print(prices[-1])

    v = getVolatility(prices)
    print(v)