import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

df_reviews = pd.read_csv('customerreviews.csv')
df_top = pd.read_csv('Top-100-Trending Books.csv')

books = df_top['book title'].unique()
book = st.sidebar.selectbox('Selecione um livro', books)

df_book = df_top[df_top['book title'] == book]
df_reviews_f = df_reviews[df_reviews['book name'] == book]  

book_title = df_book['book title'].iloc[0]
book_genre = df_book['genre'].iloc[0]
book_price = df_book['book price'].iloc[0]
book_rating = df_book['rating'].iloc[0]
book_year = df_book['year of publication'].iloc[0]

st.title(f'Revisões do livro: {book_title}', anchor=False)
st.header(f'**Gênero:** {book_genre}', anchor=False)

col1, col2, col3 = st.columns(3)
col1.metric(f'Preço: $', book_price, border=True)
col2.metric(f'Avaliação: ', book_rating, border=True)
col3.metric(f'Ano de publicação: ', book_year, border=True)

st.markdown(df_reviews_f)