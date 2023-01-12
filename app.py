import pickle
import streamlit as st
import numpy as np

popular_df = pickle.load(open('popular.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
books = pickle.load(open('books.pkl','rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl','rb'))


st.header('Book Recommender System')

selected_books = st.selectbox(
    "Select a book to see similar recommendations:",
   books["Book-Title"]
)


def recommender(book_name):
    if book_name not in pt.index:
        st.write("This book is not in our list, please try again.")
        return None
    else:
        index = np.where(pt.index == book_name)[0][0]
  # index fetch
        similar_items = sorted(list(enumerate(similarity_scores[index])), key = lambda x:x[1], reverse = True)[1:6]
        data1 = []
        data2 = []
        data3 = []

        for i in similar_items:
            item1 = []
            item2 = []
            item3 = []
            temp_df = books[books['Book-Title'] == pt.index[i[0]]]
            item1.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
            item2.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
            item3.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

            data1.append(item1)
            data2.append(item2)
            data3.append(item3)

        return data1, data2, data3

if st.button('Show Recommendations'):
    result = recommender(selected_books)
    if result:
        title, author, photo = result
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.image(photo[0],width=100)
            st.write(title[0][0])
        with col2:
            st.image(photo[1],width=100)
            st.write(title[0][0])


        with col3:
            st.image(photo[2],width=100)
            st.write(title[2][0])

        with col4:
            st.image(photo[3],width=100)
            st.write(title[3][0])

        with col5:
            st.image(photo[4],width=100)
            st.write(title[4][0])


def popular_books():
    st.header("Popular Books")
    books_df = popular_df.head(100)
    col1, col2 = st.columns(2)
    for i in range(0, 100, 2):
        with col1:
            st.image(books_df.iloc[i]["Image-URL-M"], width=150)
            st.write(books_df.iloc[i]["Book-Title"])
            st.write(books_df.iloc[i]['Book-Author'])
        with col2:
            st.image(books_df.iloc[i+1]["Image-URL-M"], width=150)
            st.write(books_df.iloc[i+1]["Book-Title"])
            st.write(books_df.iloc[i+1]['Book-Author'])



if st.sidebar.button("Popular Books"):
    popular_books()





















