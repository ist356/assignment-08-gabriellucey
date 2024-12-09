'''
location_dashboard.py
'''
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
st.set_page_config(layout="wide")

df = pd.read_csv('./cache/tickets_in_top_locations.csv')

st.title('Parking Tickets in Syracuse')
st.caption('This dashboard shows the locations of parking tickets with $1,000 or more in total aggregate violation amounts.')

locations = df['location'].unique()

location = st.selectbox('Select a location', locations) 
if location:
    filtered_df = df[df['location'] == location]

    col1, col2 = st.columns(2)

    with col1:
        pass