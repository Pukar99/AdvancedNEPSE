import numpy as np 
import pandas as pd
import os
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import streamlit as st
import matplotlib.pyplot as plt

## load Model

model = load_model('Nepse_Index_Predication_Model.keras')

st.header('Nepse Index Prediction Model')
st.subheader('Nepse Index Data')

data = pd.read_csv('../../datasrc/nepseready.csv')
# # Convert the date column to datetime format
# data['date'] = pd.to_datetime(data['date'])

# Set the date column as the index of the DataFrame
data.set_index('date', inplace=True)
data.drop(columns = ['SN','pct_change','change'], inplace=True)
st.write(data)


# # set the line chart here 
# st.subheader('Line Chart of NEPSE index')
# data= data.reset_index()
# data.drop(columns = ['open','high','turnover','low','date'], inplace=True)
# st.line_chart(data)


# plt.figure(figsize=(8,10))
# plt.plot(data)
# plt.show()