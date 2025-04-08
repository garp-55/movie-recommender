<<<<<<< HEAD
import pickle
import streamlit as st
import requests

# --- Poster Fetching Function ---
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
        data = requests.get(url).json()
        poster_path = data.get('poster_path', '')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            return "https://via.placeholder.com/300x450?text=No+Image"
    except:
        return "https://via.placeholder.com/300x450?text=Error"

# --- Recommendation Logic ---
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names, recommended_movie_posters

# --- Streamlit Setup ---
st.set_page_config(page_title="Movie Recommender", layout="wide")
st.title('🎬 Movie Recommender System')

# --- Load Data ---
try:
    with open('model/movie_list.pkl', 'rb') as f:
        movies = pickle.load(f)

    with open('model/similarity.pkl', 'rb') as f:
        similarity = pickle.load(f)

except FileNotFoundError:
    st.error(" Required model files not found. Make sure 'movie_list.pkl' and 'similarity.pkl' are in the 'model/' folder.")
    st.stop()

# --- Movie Selection ---
movie_list = movies['title'].values
selected_movie = st.selectbox(" Type or select a movie:", movie_list)

# --- Button and Recommendation Section ---
if st.button(' Show Recommendations'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.image(recommended_movie_posters[i], use_container_width=True)

            st.caption(recommended_movie_names[i])






=======
import pickle
import streamlit as st
import requests

# --- Poster Fetching Function ---
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
        data = requests.get(url).json()
        poster_path = data.get('poster_path', '')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            return "https://via.placeholder.com/300x450?text=No+Image"
    except:
        return "https://via.placeholder.com/300x450?text=Error"

# --- Recommendation Logic ---
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names, recommended_movie_posters

# --- Streamlit Setup ---
st.set_page_config(page_title="Movie Recommender", layout="wide")
st.title('🎬 Movie Recommender System')

# --- Load Data ---
try:
    with open('model/movie_list.pkl', 'rb') as f:
        movies = pickle.load(f)

    with open('model/similarity.pkl', 'rb') as f:
        similarity = pickle.load(f)

except FileNotFoundError:
    st.error(" Required model files not found. Make sure 'movie_list.pkl' and 'similarity.pkl' are in the 'model/' folder.")
    st.stop()

# --- Movie Selection ---
movie_list = movies['title'].values
selected_movie = st.selectbox(" Type or select a movie:", movie_list)

# --- Button and Recommendation Section ---
if st.button(' Show Recommendations'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.image(recommended_movie_posters[i], use_container_width=True)

            st.caption(recommended_movie_names[i])






>>>>>>> 32f62b70f07be769bd7875f4e809a661cc8a24c7
