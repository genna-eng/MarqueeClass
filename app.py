import streamlit as st
st.write ('IT Works!')
st.header ('Header')

categories = ['a', 'b', 'c']
st.multiselect ("Pick a category", categories)

import pandas as pd
import streamlit as st
import os

import plotly.express as px



#%% Grab all data
@st.cache
def grabAllStocks():
    files = []
    for file in os.listdir("../StockData/"):
        if file.endswith(".csv"):
            files.append(file)
            
    tableList = []
    for file in files:
        df = pd.read_csv("../StockData/" + file, parse_dates=['Date'], index_col=['Date'])
        df['Ticker'] = file.replace(".csv","")
        tableList.append(df) #storing as a list
    
    stockData = pd.concat(tableList)
    return stockData

#%% Grab Data
df = grabAllStocks()
tickers = list(df['Ticker'].unique())

#%% Streamlit Web App
st.title("Stock Analyzer")
stockPick = st.sidebar.multiselect("Pick the stocks to graph",tickers, ["AAPL"])
#Date picks
# d0 = st.date_input("Start Date", min(df.index))
# d1 = st.date_input("End Date", max(df.index))
filterDF = df[df['Ticker'].isin(stockPick)]

x = min(filterDF.index.year)
y = max(filterDF.index.year)

y0, y1= st.sidebar.slider("Pick the year range for x-axis",x,y,(x,y))
# filterDF.loc['2013':'2015']
filterDF = filterDF.loc[str(y0):str(y1)]

