#  Movie Recommender System

A Machine Learning-based Movie Recommender System that suggests the **top 5 similar movies** based on user input using **content-based filtering**.

---

##  Features

-  Recommends top 5 similar movies
-  Uses content-based filtering (cosine similarity)
-  Fetches movie posters using TMDB API
-  Interactive UI built with Streamlit
-  Fast and user-friendly interface

---
##  Preview

### Sample 1
![ui](sample1.png)

### Sample 2
![ui](sample2.png)

##  Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit
- TMDB API

---

##  How It Works

The system recommends movies based on similarity scores calculated using:

- Genres  
- Keywords  
- Cast  
- Crew  

These features are combined and processed using cosine similarity to find the most relevant movies.

---

##  Run Locally

```bash
git clone https://github.com/KhushiKumari27X/Movie-recommendation-system.git
cd Movie-recommendation-system
pip install -r requirements.txt
streamlit run App.py
