import streamlit as st
import pandas as pd
import numpy as np
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static

#Page Header
st.header("🍺Search Nearest Pubs🍺")

#Loading data
df=pd.read_csv('cleaned.csv')

#Taking input (latitude and longitude)
col1,col2=st.columns(2)
with col1:
    lat=st.number_input(label="Enter Latitude Here",min_value=49.892485,max_value=60.764969)
with col2:
    lon=st.number_input(label="Enter Longitude Here",min_value=-7.384525,max_value=1.757763)

#Entered Location
search_location=np.array((lat,lon))

#Original/available Location
original_location=np.array([df['latitude'],df['longitude']]).T

#Finding Euclidean distance
dist=np.sum((original_location-search_location)**2,axis=1)

#Adding distance column to dataframe
df['Distance']=dist

#Asking user that how many nearest Pubs they want to see
nearest=st.slider(label="How Many Nearest Pubs You Want to See",min_value=1,max_value=50,value=5)
data=df.sort_values(by='Distance',ascending=True)[:nearest]

#List of Bar Names
st.subheader(f"{nearest} Nearest Pubs:")

pub_mapping=folium.Map(location=[data['latitude'].mean(),data['longitude'].mean()],zoom_start=12)

mc=MarkerCluster()
for row in data.iterrows():
    mc.add_child(folium.Marker(location=[row[1]['latitude'],row[1]['longitude']],popup=row[1]['name']))
pub_mapping.add_child(mc)

#Displaying Nearest Pubs on Map
folium_static(pub_mapping)
