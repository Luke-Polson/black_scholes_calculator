import math


def get_d1(stock_price, strike_price, t, r, sigma):

    num = math.log((stock_price/strike_price),math.e) + (r + (sigma**2) / 2) * (t/365)
    den = sigma * math.sqrt(t/365)

    return num / den


def get_d2(d1, sigma, t):

    return d1 - sigma * math.sqrt(t/365)


def N(x):
    """'Cumulative distribution function for the standard normal distribution'"""

    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def get_black_scholes_price(stock_price, strike_price, t, r, sigma):
    """

    Function to calculate the price of an option using the given arguments.

    :param stock_price: The current market price of the underlying stock.
    :param strike_price: The option strike price.
    :param t: The time to maturity, given in days.
    :param r: Risk free interest rate, given as a decimal.
    :param sigma: Implied volatility, given as a decimal.
    :return: Option price according to Black-Scholes model.
    """

    d1 = get_d1(stock_price, strike_price, t, r, sigma)
    d2 = get_d2(d1, sigma, t)

    n_1 = N(d1)
    n_2 = N(d2)

    return stock_price * n_1 - strike_price * math.pow(math.e, -r * (t/365)) * n_2










