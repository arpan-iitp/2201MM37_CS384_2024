import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the dataset
df = pd.read_csv(r'C:\2201EE93_CS384_2024\tut08\infy_stock.csv')

# Display the first 10 rows
print(df.head(10))

# Check for missing values
print(df.isnull().sum())

# Handling missing values (if any, you can choose to drop or fill them)
df = df.dropna()  # Option 1: Drop rows with missing data
# OR
df.fillna(method='ffill', inplace=True)  # Option 2: Forward fill missing values

# Convert Date column to datetime format for easy plotting
df['Date'] = pd.to_datetime(df['Date'])

# Plot the closing price over time
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Close'], label='Close Price')
plt.title('Closing Price Over Time')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.legend()
plt.show()

# Candlestick chart using mplfinance
import mplfinance as mpf

# Set the Date as the index
df.set_index('Date', inplace=True)

# Plotting candlestick chart
mpf.plot(df, type='candle', volume=True, style='charles', title='Candlestick Chart')

# Calculate daily return percentage
df['Daily Return (%)'] = ((df['Close'] - df['Open']) / df['Open']) * 100

# Calculate average and median of daily returns
average_return = df['Daily Return (%)'].mean()
median_return = df['Daily Return (%)'].median()

# Calculate the standard deviation of closing prices
std_close = df['Close'].std()

print(f"Average Daily Return: {average_return:.2f}%")
print(f"Median Daily Return: {median_return:.2f}%")
print(f"Standard Deviation of Close Prices: {std_close:.2f}")


# Calculate 50-day and 200-day moving averages
df['50-day MA'] = df['Close'].rolling(window=50).mean()
df['200-day MA'] = df['Close'].rolling(window=200).mean()

# Plot the closing price along with moving averages
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Close'], label='Close Price')
plt.plot(df.index, df['50-day MA'], label='50-day MA', linestyle='--')
plt.plot(df.index, df['200-day MA'], label='200-day MA', linestyle='--')
plt.title('Closing Price with Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

# Calculate rolling standard deviation (volatility) with a 30-day window
df['Volatility (30-day)'] = df['Close'].rolling(window=30).std()

# Plot the volatility
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Volatility (30-day)'], label='30-day Volatility')
plt.title('30-day Rolling Volatility')
plt.xlabel('Date')
plt.ylabel('Volatility')
plt.legend()
plt.show()

# Identify bullish and bearish trends
df['Trend'] = np.where(df['50-day MA'] > df['200-day MA'], 'Bullish', 'Bearish')

# Plotting bullish and bearish trends on the chart
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Close'], label='Close Price')
plt.plot(df.index, df['50-day MA'], label='50-day MA', linestyle='--')
plt.plot(df.index, df['200-day MA'], label='200-day MA', linestyle='--')

# Mark bullish and bearish regions
plt.fill_between(df.index, df['Close'], where=df['Trend'] == 'Bullish', color='green', alpha=0.3, label='Bullish')
plt.fill_between(df.index, df['Close'], where=df['Trend'] == 'Bearish', color='red', alpha=0.3, label='Bearish')

plt.title('Stock Trends: Bullish vs Bearish')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()
