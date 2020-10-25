# Black-Scholes Calculator

The Black-Scholes model, is a mathematical model used to price options contracts. It takes several parameters - the current stock price, the option strike price, the time to maturity
in days, the risk free interest rate, and implied volatility.

## Some Background

The model makes certain assumptions, including:

- the fact that the contracts are European (and thus can only be exercised on the maturity date.)
- that dividends are not paid out to shareholders
- efficiency of the financial markets
- stock prices follow a lognormal distribution
- no opportunities for arbitrage

## What does this tool do?

At present, it simply calculates the price of a call option for the given parameters. In future, I hope to extend this project to also calculate put option prices, as well 
as giving the option of downloading stock info from Yahoo Finance and performing calculations on that.
