import streamlit as st
import pickle
import pandas as pd
import requests
import gzip

# -------------------- FETCH POSTER --------------------
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=5e560991829e30cd4b660f0e518e79dc&language=en-US"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get('poster_path')

        if poster_path:
            return "https://image.tmdb.org/t/p/w185/" + poster_path
        else:
            return "https://via.placeholder.com/185x278?text=No+Poster"

    except requests.exceptions.RequestException:
        return "https://via.placeholder.com/185x278?text=Error"


# -------------------- LOAD DATA (CACHED) --------------------
@st.cache_data
def load_data():
    # Load movies data
    movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)

    # Load compressed similarity matrix
    with gzip.open('similarity_compressed.pkl.gz', 'rb') as f:
        similarity = pickle.load(f)

    return movies, similarity


movies, similarity = load_data()


# -------------------- RECOMMEND FUNCTION --------------------
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters


# -------------------- UI --------------------
st.title('🎬 Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select a movie',
    movies['title'].values
)

if st.button('Recommend'):
    with st.spinner('Fetching recommendations...'):
        names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])

