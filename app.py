import streamlit as st
import pickle
import pandas as pd
import numpy as np
import faiss
import requests
import os
from dotenv import load_dotenv
load_dotenv('.env')

movies=pickle.load(open('movies.pkl','rb'))
movies_list=movies['title'].values

embeddings = np.load('models/embeddings.npy')

index = faiss.read_index('models/movie_index.faiss')

def fetch_poster(movie_id):
    # Get API key
    api_key = os.getenv("TMDB_API_KEY")

    if not api_key:
        try:
            api_key = st.secrets["TMDB_API_KEY"]
        except Exception:
            return None

    # Validate movie ID
    if pd.isna(movie_id):
        st.warning("Movie ID is missing.")
        return None

    url = f"https://api.themoviedb.org/3/movie/{int(movie_id)}"

    for attempts in range(2):
        try:
            response = requests.get(
                url,
                params={
                    "api_key": api_key,
                    "language": "en-US"
                },
                timeout=20
            )
            # Show API errors
            if response.status_code != 200:
                st.warning(
                    f"TMDB error for movie ID {movie_id}: "
                    f"HTTP {response.status_code}"
                )
                return None
            data = response.json()
            poster_path = data.get("poster_path")

            if poster_path:
                return f"https://image.tmdb.org/t/p/w500{poster_path}"

            st.caption(f"No poster path returned for movie ID {movie_id}.")
            return None
        except requests.RequestException:
            if attempts==1:
                return None
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