import pickle
import streamlit as st
import numpy as np

popular_df = pickle.load(open('popular.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
books = pickle.load(open('books.pkl','rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl','rb'))

st.header('Book Recommender System')

selected_books = st.selectbox(
    "Select a book or type book name to see similar recommendations:",
    books["Book-Title"]
)

def recommender(book_name):
    if book_name not in pt.index:
        st.write("This book is not in our list, please try again.")
        return None
    else:
        index = pt.index.get_loc(book_name)
        similar_items = np.argsort(similarity_scores[index])[-6:][::-1]
        similar_book_titles = pt.index[similar_items]
        similar_books = books[books['Book-Title'].isin(similar_book_titles)]
        return similar_books

if st.button('Show Recommendations'):
    result = recommender(selected_books)
    if result is not None:
        col1, col2, col3 = st.columns(3)
        for i in range(len(result)):
            if i % 3 == 0:
                with col1:
                    st.image(result.iloc[i, result.columns.get_loc('Image-URL-M')], width=150)
                    st.write(result.iloc[i, result.columns.get_loc('Book-Title')])
                    st.write(result.iloc[i, result.columns.get_loc('Book-Author')])
            elif i % 3 == 1:
                with col2:
                    st.image(result.iloc[i, result.columns.get_loc('Image-URL-M')], width=150)
                    st.write(result.iloc[i, result.columns.get_loc('Book-Title')])
                    st.write(result.iloc[i, result.columns.get_loc('Book-Author')])
            else:
                with col3:
                    st.image(result.iloc[i, result.columns.get_loc('Image-URL-M')], width=150)
                    st.write(result.iloc[i, result.columns.get_loc('Book-Title')])
                    st.write(result.iloc[i, result.columns.get_loc('Book-Author')])
def popular_books():
    st.header("Popular Books")
    books_df = popular_df.head(100)
    col1, col2 = st.columns(2)
    for i in range(0, books_df.shape[0], 2):
        if i + 1 < books_df.shape[0]:
            with col1:
                st.image(books_df.iloc[i]["Image-URL-M"], width=150)
                st.write(books_df.iloc[i]["Book-Title"])
                st.write(books_df.iloc[i]['Book-Author'])
            with col2:
                st.image(books_df.iloc[i + 1]["Image-URL-M"], width=150)
                st.write(books_df.iloc[i + 1]["Book-Title"])
                st.write(books_df.iloc[i + 1]['Book-Author'])


if st.sidebar.button("Popular Books"):
    popular_books()
