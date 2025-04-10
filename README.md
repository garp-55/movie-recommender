# movie-recommender
# 🎬 Movie Recommender System

A content-based movie recommender system built with Streamlit that suggests similar movies based on user selection. The system uses movie metadata and natural language processing to generate recommendations.

---

##  Features

- 📽️ Recommend 5 similar movies for any selected title
- 🧠 Uses TF-IDF and cosine similarity for content-based filtering
- 🖼️ Fetches live movie posters using the TMDB API
- 🖥️ Interactive front-end built with Streamlit
- 💾 Automatically rebuilds similarity matrix if not found (for lightweight repo)

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Scikit-learn
- Pandas
- Requests
- TMDB API
- Pickle (for model persistence)

---

## 📂 Project Structure

movie-recommender/ ├── app.py # Streamlit app ├── model/ │ ├── movie_list.pkl # Pickled movie metadata (required) │ └── similarity.pkl # (Ignored if too large, rebuilds automatically) ├── requirements.txt ├── .gitignore └── README.md


---

## 🧠 How It Works

- `movie_list.pkl`: Contains metadata (title, tags, movie_id) used for generating recommendations
- If `similarity.pkl` is missing, it will be computed using `TfidfVectorizer` and `cosine_similarity` from the `tags` column
- Recommendations are ranked by similarity score
- Movie posters are pulled via the TMDB API using each movie’s `movie_id`

---

## 🔧 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender

2. Install dependencies

pip install -r requirements.txt

3. Add your TMDB API Key
Replace the placeholder API key in app.py:

api_key = "your_api_key_here"

4. Run the app
streamlit run app.py

🚫 Note on Large Files
The similarity.pkl file is excluded from version control to keep the repository lightweight. The app will automatically regenerate it on first run using movie metadata.






