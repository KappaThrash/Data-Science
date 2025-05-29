import pandas as pd 
import streamlit as st

st.set_page_config(layout='wide')

df_reviews = pd.read_csv('customerreviews.csv')
df_top = pd.read_csv('Top-100-Trending Books.csv')

topbookmin = df_top['book price'].min()
topbookmax = df_top['book price'].max()

max_price = st.sidebar.slider(label='Slider de preço dos livros', min_value=topbookmin, max_value=topbookmax, value=topbookmax)
df_bookprice_filtered = df_top[df_top['book price'] <= max_price]
df_bookprice_filtered
