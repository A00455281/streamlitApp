# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 16:50:06 2022

@author: aksha
"""


import pandas as pd
import requests
import streamlit as st
import matplotlib.pyplot as plt

st.title("SMU Assignment")
numofday = st.slider('Number of Days',min_value= 1, max_value=365, value=90)
seletedCurrency = st.radio('Currency', ['cad', 'usd', 'inr'])

API_URL = 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart'
payload = {'vs_currency': seletedCurrency, 'days': numofday,'interval':'daily'}
req = requests.get(API_URL, payload)
if req.status_code == 200:
    data = req.json()
    raw_data = data['prices']
    
priceDf = pd.DataFrame(raw_data, columns=('date', 'price'))
priceDf.date = pd.to_datetime(priceDf.date, unit='ms')

fig, ax = plt.subplots(figsize=(16, 7))
ax.plot(priceDf.date, priceDf.price)
ax.set_xlabel('DATE')
ax.set_ylabel('PRICE')
st.pyplot(fig)
st.write(f'Average price is {round(priceDf.price.mean(),2)}')   
