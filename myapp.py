import streamlit as st
import yfinance as yf
import pandas as pd

st.write("""
# Simple Stock Price App

shown are the stock price and volume of google
""" )

#define the ticker symbol

tickerSymbol = 'GOOGL'

#get data on this ticker

tickerData = yf.Ticker(tickerSymbol)

#get the historical price for this ticker

tickerDf = tickerData.history(period = '1d',start = '2010-5-31',end= '2020-5-31')

#open high          low        price       dividents   stock price

st.write("""## close value""")
st.line_chart(tickerDf.Close)

st.write("""## Volume """)
st.line_chart(tickerDf.Volume)