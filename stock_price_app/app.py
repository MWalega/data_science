import pandas as pd
import streamlit as st
import yfinance as yf


st.write("""
# Simple Stock Price App

This app shows stock **closing price** and **volume** of Google!

""")

# define the ticker symbol
ticker_symbol = 'GOOGL'

# get data on this ticker
ticker_data = yf.Ticker(ticker_symbol)

# get the historical prices for this ticker
ticker_df = ticker_data.history(period='1d', start='2011-04-13', end='2021-04-13')
# Open / High / Low / Close / Volume / Dividends / Stock Splits

st.write("""
## Closing Price
""")
st.line_chart(ticker_df.Close)
st.write("""
## Volume
""")
st.line_chart(ticker_df.Volume)