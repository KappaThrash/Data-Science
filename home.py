import pandas as pd 
import streamlit as st
import plotly.express as px

st.set_page_config(layout='wide')

df_reviews = pd.read_csv('customerreviews.csv')
df_top = pd.read_csv('Top-100-Trending Books.csv')

topbookmin = df_top['book price'].min()
topbookmax = df_top['book price'].max()

max_price = st.sidebar.slider(label='Slider de preço dos livros', min_value=topbookmin, max_value=topbookmax, value=topbookmax)
df_bookprice_filtered = df_top[df_top['book price'] <= max_price]
df_bookprice_filtered

count_yearBooks = df_bookprice_filtered['year of publication'].value_counts()

fig1 = px.bar(count_yearBooks, title='Quantidade de livros por ano')
fig2 = px.histogram(df_bookprice_filtered['book price'], title='Distribuição de preços dos livros')

col1, col2 = st.columns(2)
col1.plotly_chart(fig1, use_container_width=True)
col2.plotly_chart(fig2, use_container_width=True)

