import pandas as pd
import numpy as np
import streamlit as st

df = pd.read_csv(r'C:\Users\geno1\OneDrive\Documents\pydocs\passing_cleaned.csv')

df.drop(columns='Unnamed: 0', inplace=True)

dfbyyear = df.groupby('Year').sum()
dfbyyear = dfbyyear[['Yds', 'TD', 'Int']]
dfbyyear['TD/Int Ratio'] = (dfbyyear['TD'] / dfbyyear['Int'])

dftransposed = dfbyyear.transpose()
st.title("NFL Passing Data (2001-2023)")
st.write(dftransposed)

df_tds = dfbyyear['TD']
df_yds = dfbyyear['Yds']
df_ints = dfbyyear['Int']
df_ratio = dfbyyear['TD/Int Ratio']
df_tdints = dfbyyear[['TD', 'Int']]
st.subheader("Have the leagues QB's improved their passing performance over the years? Lets take a look with a few graphs.")

st.header("NFL Passing TD's (2001-2023)")
st.bar_chart(df_tds)
st.caption("As we can see here, the number of passing TD's per year seems to be slightly trending upwards.")

st.header("NFL Passing Yards (2001-2023)")
st.bar_chart(df_yds)
st.caption("The number of yards per year also seems to be trending upwards.")

st.header("NFL Passing Ints (2001-2023)")
st.bar_chart(df_ints)
st.caption("The Number of Interceptions has been slowly trending downwards each year. While teams have been throwing more TD's and more Yards than ever before, they are throwing less picks than ever before as well.")

st.header("NFL TD to Int Ratio 2001-2023)")
st.bar_chart(df_ratio)
st.caption("The number of TD's thrown per interception also is on the rise over the years.")

st.subheader("Overall, it seems like NFL QB's have been increasing their performance on average each year. This may be due to a variety of factors, including rule changes that benefit offensive players more than they benefit defensive players.") 
             
st.subheader("Whatever the case may be, this data seems to conclude that the efficiency of passing in the NFL has improved consistently throughout the last two decades.")