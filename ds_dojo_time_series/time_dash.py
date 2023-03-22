import pickle as pkl
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)

#read in the data
df = pd.read_csv('Data/AirPassengers.csv')

#read in the model
model_file = open('Model/time_series_model.pkl','rb')
model = pkl.load(model_file)
model_file.close()

#change the time column to date time
df['Month'] = pd.to_datetime(df['Month'])
df.set_index('Month',inplace =True)

#create your widget and set it to a variable
number_of_steps = st.slider('Input Number of Steps to Forecast', min_value = 1, max_value = 24, value = 12)

#forecast using the read in model
forecasts = model.forecast(number_of_steps)

#prepare the forecast dataframe
f_df = pd.DataFrame(forecasts)
#get the index with the date range function
datelist = pd.date_range(list(df.index)[-1], periods=number_of_steps, freq='MS').tolist()
#set it equal to the index
f_df.index = datelist
#rename the columns
f_df.columns = ['#Passengers']
#concat the datasets
full_df = pd.concat([df,f_df],axis=0)

#plot the past series with the forecasts
full_df.plot()
st.pyplot()
