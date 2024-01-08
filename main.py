import matplotlib.pyplot as plt
import pandas as pd

df_tesla = pd.read_csv('TESLA Search Trend vs Price.csv')

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel('TSLA Stock Price', color='#E6232E')
ax2.set_ylabel('Search Trend', color='skyblue')

ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color='#E6232E', label='TSLA Stock Price')
ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, color='skyblue', label='Search Trend')


ax1.legend(loc='upper left')
ax2.legend(loc='upper right')


plt.show()

df_btc_search = pd.read_csv('Bitcoin Search Trend.csv')
df_btc_price = pd.read_csv('Daily Bitcoin Price.csv')

# Plotting for Bitcoin Search Trend
ax1 = plt.subplot(2, 2, 2)
ax1.plot(df_btc_search['MONTH'], df_btc_search['BTC_NEWS_SEARCH'], label='Search Trend', color='orange')
ax1.set_title('Bitcoin Search Trend')
ax1.set_xlabel('Month')
ax1.set_ylabel('Search Trend')
ax1.legend()

# Plotting for Daily Bitcoin Price
ax2 = plt.subplot(2, 2, 3)
ax2.plot(df_btc_price['DATE'], df_btc_price['CLOSE'], label='Bitcoin Price', color='yellow')
ax2.set_title('Daily Bitcoin Price')
ax2.set_xlabel('Date')
ax2.set_ylabel('Bitcoin Price')
ax2.legend()

# Adjust layout for better visualization
plt.tight_layout()

# Show the plots
plt.show()


df_unemployment = pd.read_csv('UE Benefits Search vs UE Rate 2004-20.csv')

# Plotting
ax1 = plt.gca()

ax1.set_ylabel('Unemployment Rate', color='#E6232E')
ax1.plot(df_unemployment['MONTH'], df_unemployment['UNRATE'], color='#E6232E', label='Unemployment Rate')

# Adding a second y-axis for Search Trend
ax2 = ax1.twinx()
ax2.set_ylabel('Search Trend', color='skyblue')
ax2.plot(df_unemployment['MONTH'], df_unemployment['UE_BENEFITS_WEB_SEARCH'], color='purple', label='Search Trend')

# Adding title and x-axis label
plt.title('Unemployment Rate and Search Trend')
plt.xlabel('Month')

# Display legends for both y-axes
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Show the plot
plt.show()


# Read the CSV files into DataFrames
df_btc_search = pd.read_csv('Bitcoin Search Trend.csv')
df_btc_price = pd.read_csv('Daily Bitcoin Price.csv')

# Create a single set of axes for both plots
fig, ax1 = plt.subplots()

# Plotting for Bitcoin Search Trend on the left y-axis
color = 'tab:orange'
ax1.set_xlabel('Month')
ax1.set_ylabel('Search Trend', color=color)
ax1.plot(df_btc_search['MONTH'], df_btc_search['BTC_NEWS_SEARCH'], label='Search Trend', color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax1.legend(loc='upper left')

# Create a secondary y-axis for Bitcoin Price on the right
ax2 = ax1.twinx()
color = 'tab:green'
ax2.set_ylabel('Bitcoin Price', color=color)
ax2.plot(df_btc_price['DATE'], df_btc_price['CLOSE'], label='Bitcoin Price', color=color)
ax2.tick_params(axis='y', labelcolor=color)
ax2.legend(loc='upper right')

# Show the plot
plt.title('Bitcoin Search Trend and Daily Bitcoin Price')
plt.show()




