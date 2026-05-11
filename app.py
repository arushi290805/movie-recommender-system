import streamlit as st
import pickle
import pandas as pd
import numpy as np
import faiss
import requests

movies=pickle.load(open('movies.pkl','rb'))
movies_list=movies['title'].values

embeddings = np.load('models/embeddings.npy')

index = faiss.read_index('models/movie_index.faiss')

def fetch_poster(movie_id):

    try:

        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"

        response = requests.get(
            url,
            timeout=10
        )

        data = response.json()

        if data.get('poster_path'):

            return (
                "https://image.tmdb.org/t/p/w500"
                + data['poster_path']
            )

        return None

    except Exception as e:

        print("Poster fetch error:", e)

        return None

def recommend(movie_title, top_n=5):
    #we will find movie index
    movie_idx = movies[
        movies['title']==movie_title
    ].index[0]

    #find embedding
    query_vector=embeddings[movie_idx].reshape(1,-1)

    distances, indices = index.search(
        query_vector,
        top_n+1
    )
    recommendations=[]
    recommended_movies_posters=[]
    for i in indices[0][1:]:
        movie_idx=i
        recommendations.append(
            movies.iloc[i]['title']
        )
        recommended_movies_posters.append(
            fetch_poster(movies.iloc[i]['movie_id'])
        )
    return recommendations,recommended_movies_posters

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'What movie do you like?',
movies_list)


if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)
    st.write('Recommended movies:')
    col1, col2, col3, col4, col5 = st.columns(5)

    cols = [col1, col2, col3, col4, col5]

    for idx, col in enumerate(cols):

        with col:

            st.markdown(f"### {names[idx]}")

            if posters[idx]:
                st.image(posters[idx], use_container_width=True)
            else:
                st.write("Poster not available")