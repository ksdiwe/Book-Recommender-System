# Book Recommender System

### 𝗖𝗼𝗹𝗹𝗮𝗯𝗼𝗿𝗮𝘁𝗶𝘃𝗲 𝗙𝗶𝗹𝘁𝗲𝗿𝗶𝗻𝗴-𝗕𝗮𝘀𝗲𝗱 𝗥𝗲𝗰𝗼𝗺𝗺𝗲𝗻𝗱𝗲𝗿 𝗦𝘆𝘀𝘁𝗲𝗺

[Web App](https://ksdiwe-book-recommender-system-app-kbvyvw.streamlit.app/)

Dataset: https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset

Approach:
- I first filtered the data by considering only those users who have rated more than 200 books and only those books that have received more than 50 ratings.
- This step helped in reducing the noise and sparsity in the data by focusing on users and books that have a significant number of ratings.
- Next, calculated the similarity scores between the books using the Euclidean distance similarity measure.
- This approach calculates the distance between the ratings of two books, which helps in identifying the books that are similar in terms of their ratings.
Finally, based on the similarity scores, generated recommendations for a selected book. By considering the books with the highest similarity scores to the selected book, were able to recommend other books that users with similar tastes might also enjoy.

# Blog
[Book-Recommender-System](https://medium.com/@ksdiwe2615/book-recommender-system-6c73e93ab80f)

https://user-images.githubusercontent.com/20944950/212302482-62189718-76d9-490b-b6a2-3015d20fde43.mp4

