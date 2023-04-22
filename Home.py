import streamlit as st
import pandas as pd
import folium
from PIL import Image

st.set_page_config(layout="wide")

df=pd.read_csv('cleaned.csv')

st.title(":red[Open Pubs Application 🍻🍻]")
image=Image.open('images/drinkers.jpg')
st.image(image,use_column_width=True)

st.markdown("## :blue[About the Dataset]")

st.markdown("###### Top Five Rows of Dataset")
st.write(df.head())

st.markdown("###### Total Number of Rows and Columns")
st.write("Total number of rows:",df.shape[0])
st.write("Total number of columns:",df.shape[1])

st.markdown("###### Null Values")
st.write(df.isnull().sum())

st.markdown("###### Duplicated Values")
st.write(df.duplicated().sum())

st.markdown("###### Top 10 Locations which have more pubs")
image=Image.open('images/pubs_by_location.png')
st.image(image,use_column_width=True)