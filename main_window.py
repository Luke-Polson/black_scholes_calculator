import tkinter as tk
from functions import *


class Window(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        vars = []
        for i in range(6):
            vars.append(tk.StringVar())

        self.out_text = vars[-1]

        self.greeting = tk.Label(text = "Black Scholes Pricing", font=('',20))
        self.greeting.grid(row=0, column=0, padx=10, pady=10)

        self.stock_price_label = tk.Label(text = "Stock Price: ")
        self.stock_price_label.grid(row=1, column=0)
        self.stock_price_entry = tk.Entry(textvariable=vars[0])
        self.stock_price_entry.grid(row=1, column=1)

        self.strike_price_label = tk.Label(text = "Strike Price: ")
        self.strike_price_label.grid(row=2,column=0)
        self.strike_price_entry = tk.Entry(textvariable=vars[1])
        self.strike_price_entry.grid(row=2,column=1)

        self.time_label = tk.Label(text = "Time to Maturity (days): ")
        self.time_label.grid(row=3,column=0)
        self.time_entry = tk.Entry(textvariable=vars[2])
        self.time_entry.grid(row=3,column=1)

        self.interest_label = tk.Label(text = "Risk free interest rate: ")
        self.interest_label.grid(row=4,column=0)
        self.interest_entry = tk.Entry(textvariable=vars[3])
        self.interest_entry.grid(row=4,column=1)

        self.sigma_label = tk.Label(text = "Implied volatility: ")
        self.sigma_label.grid(row=5,column=0)
        self.sigma_entry = tk.Entry(textvariable=vars[4])
        self.sigma_entry.grid(row=5,column=1)

        self.button = tk.Button(text="Get Price", command=self.calculate_price)
        self.button.grid(row=6, column=0, pady=10)

        self.output_label = tk.Label(textvariable=vars[5])
        self.output_label.grid(row=6,column=1)

        self.mainloop()

    def calculate_price(self):

        stock_price = float(self.stock_price_entry.get())
        strike_price = float(self.strike_price_entry.get())
        t = float(self.time_entry.get())
        r = float(self.interest_entry.get())
        sigma = float(self.sigma_entry.get())

        output = "${:.3f}".format(get_black_scholes_price(stock_price, strike_price, t, r, sigma))

        self.out_text.set(output)


