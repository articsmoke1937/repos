# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 22:09:24 2021

@author: DeveOpin
"""
# Import packages
import yfinance as yf
import pandas as pd
import matplotlib as plt

# Set the start and end date
start_date = '1990-01-01'
end_date = '2021-07-12'

# Define the ticker list
tickers_list = ['POTX', 'ASX']

# Create placeholder for data
data = pd.DataFrame(columns=tickers_list)

# Fetch the data
for ticker in tickers_list:
    data[ticker] = yf.download(ticker, 
                               start_date,
                               end_date)['Open']
    
# Print first 5 rows of the data
data.head()

# Plot all the close prices
data.plot(figsize=(10, 7))

# # Show the legend
# plt.legend()

# # Define the label for the title of the figure
# plt.title("Adjusted Close Price", fontsize=16)

# # Define the labels for x-axis and y-axis
# plt.ylabel('Price', fontsize=14)
# plt.xlabel('Year', fontsize=14)

# # Plot the grid lines
# plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
# plt.show()