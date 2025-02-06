---
title: Spotify Recommandation
emoji: 🐨
colorFrom: blue
colorTo: yellow
sdk: streamlit
sdk_version: 1.42.0
app_file: app.py
pinned: false
---
# 🎵 Spotify Song Recommendation System

This is an **AI-powered Song Recommendation System** that clusters songs based on their audio features like danceability, energy, valence, etc., and provides song recommendations.  
The project is deployed using **Streamlit** on **Hugging Face Spaces** with CI/CD automation.

🔗 **Live App** → [View Here](https://huggingface.co/spaces/lohithkumar01/spotify-song-recommendation)  

---

## Features
✅ **Cluster-based Song Recommendations** – Uses K-Means clustering to group similar songs.  
✅ **Interactive Streamlit UI** – Users can select a song and get recommendations in real-time.  
✅ **Visual Insights** – Displays **Cluster distribution & Top Albums** using charts.  
✅ **Automated Deployment (CI/CD)** – GitHub Actions **automatically deploys** updates to Hugging Face Spaces.  
✅ **MLOps: MLflow & Auto Data Updates** – Tracks **model experiments** & dynamically updates song data.

---

## **Technologies Used**
- **Machine Learning:** Scikit-Learn, K-Means Clustering
- **Data Processing:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn, Streamlit
- **MLOps Tools:** GitHub Actions, MLflow, Hugging Face API
- **Deployment:** Hugging Face Spaces, GitHub CI/CD

---

## **Installation & Setup**
You can run this project locally using **Python & Streamlit**.

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/lohithkumar12/spotify-song-recommendation.git
cd spotify-song-recommendation
