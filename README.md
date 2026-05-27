# 🎬 AI Movie Recommender System

An AI-powered movie recommendation web application built using:

* Python
* Streamlit
* Sentence Transformers
* FAISS
* TMDB API
* NLP-based semantic similarity

The system recommends movies based on semantic understanding of movie descriptions instead of simple keyword matching.

---

# 🚀 Features

* Semantic movie recommendations using transformer embeddings
* Fast vector similarity search using FAISS
* Movie poster fetching using TMDB API
* Interactive Streamlit frontend
* Content-based recommendation engine
* Clean and responsive UI
* NLP preprocessing pipeline

---

# 🧠 How It Works

## 1. Data Preprocessing

Movie descriptions are cleaned using:

* Lowercasing
* Stopword removal
* Punctuation removal
* Text normalization

---

## 2. Sentence Embeddings

The project uses:

```python
SentenceTransformer('all-MiniLM-L6-v2')
```

This converts movie descriptions into:

```text
384-dimensional semantic vectors
```

Movies with similar meanings become mathematically close in vector space.

---

## 3. Vector Search with FAISS

FAISS is used for:

* Fast nearest-neighbor search
* Similarity matching
* Efficient recommendation retrieval

---

## 4. Streamlit Frontend

Users can:

* Select movies
* Get recommendations
* View movie posters
* Explore similar movies interactively

---

# 📂 Project Structure

```text
movie-recommender-system/
│
├── data/
│   ├── tmdb_5000_movies.csv
│   ├── tmdb_5000_credits.csv
│   └── preprocessed_movies.csv
│
├── models/
│   ├── embeddings.npy
│   └── movie_index.faiss
│
├── notebooks/
│   ├── data-preprocessing.ipynb
│   └── model.ipynb
│
├── venv/
│
├── app.py
├── movies.pkl
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/arushi290805/movie-recommender-system.git
```

## 2. Navigate Into Project

```bash
cd movie-recommender-system
```

## 3. Create Virtual Environment

```bash
python -m venv venv
```

## 4. Activate Virtual Environment

### Windows

```powershell
.\venv\Scripts\Activate
```

---

# 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Application

```bash
streamlit run app.py
```

The app will open at:

```text
http://localhost:8501
```

---

# 🛠️ Technologies Used

| Technology            | Purpose                    |
| --------------------- | -------------------------- |
| Python                | Core programming language  |
| Streamlit             | Frontend web app           |
| Sentence Transformers | Semantic embeddings        |
| FAISS                 | Vector similarity search   |
| Pandas                | Data processing            |
| NumPy                 | Numerical computation      |
| TMDB API              | Movie posters and metadata |
| Requests              | API communication          |

---

# 📊 Recommendation Pipeline

```text
Movie Description
        ↓
Text Preprocessing
        ↓
Sentence Transformer Embeddings
        ↓
FAISS Vector Index
        ↓
Similarity Search
        ↓
Movie Recommendations
```

---

# 🌟 Future Improvements

* Dark mode UI
* Trailer integration
* User authentication
* Collaborative filtering
* Hybrid recommendation system
* AI chatbot for movie discovery
* Voice-based search
* Personalized watchlists
* Deployment with Docker

---

# 📸 Screenshots

<img width="1475" height="930" alt="image" src="https://github.com/user-attachments/assets/13d6627b-5f8d-48c7-bfdd-40933f690c68" />


---

# 📌 Dataset

Dataset used:

* TMDB 5000 Movie Dataset

---

# 🙌 Acknowledgements

* TMDB API
* Hugging Face Sentence Transformers
* FAISS by Facebook AI
* Streamlit

---

# 📧 Contact

If you'd like to connect or discuss the project:

* [LinkedIn](https://linkedin.com/arushikhare)
* [GitHub](https://www.github.com/arushi290805)
* [Email](mailto:arushikharework@gmail.com)

---

# ⭐ If You Like This Project

Give this repository a star on GitHub.
