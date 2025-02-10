Here is the **finalized README.md** with all necessary details, including the **Spotify API issue, Hugging Face deployment, DAGsHub MLflow integration, and CI/CD automation**.

---

# 🎵 **Spotify Song Recommendation System**

This is an **AI-powered Song Recommendation System** that clusters songs based on their audio features (danceability, energy, valence, etc.) and provides personalized song recommendations.

The project is **deployed on Hugging Face Spaces** with **CI/CD automation**, and **MLflow tracking via DAGsHub**.

🔗 **Live App** → [View Here](https://huggingface.co/spaces/lohithkumar01/spotify-song-recommendation)  
🔗 **GitHub Repository** → [View Here](https://github.com/lohithkumar12/spotify-song-recommendation)  
🔗 **MLflow Tracking (DAGsHub)** → [View Here](https://dagshub.com/vemuboddupalli/spotify-recommendation.mlflow)

---

## 🚀 **Features**
✅ **Cluster-based Song Recommendations** – Uses **K-Means clustering** to group similar songs.  
✅ **Interactive Streamlit UI** – Users can select a song and get recommendations in real-time.  
✅ **Visual Insights** – Displays **Cluster distribution & Top Albums** using charts.  
✅ **Automated Deployment (CI/CD)** – **GitHub Actions** automatically **deploys** updates to Hugging Face Spaces.  
✅ **MLOps: MLflow & Auto Data Updates** – Tracks **model experiments** & dynamically updates song data.

---

## 🔧 **Technologies Used**
- **Machine Learning**: Scikit-Learn, K-Means Clustering
- **Data Processing**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn, Streamlit
- **MLOps Tools**: GitHub Actions, MLflow, DAGsHub, Hugging Face API
- **Deployment**: Hugging Face Spaces, GitHub CI/CD

---

## **⚠️ Issue: Spotify API Audio Features Fetching**
Although we successfully fetch **song metadata** (name, album, popularity, release date), we are **unable to retrieve audio features** due to **Spotify API access restrictions**:
- **403 Forbidden Error** when calling `GET /audio-features/{id}`.
- This restricts fetching important song attributes like **danceability, energy, valence, loudness, and tempo**.

### 🔍 **Alternative Approaches**
1. **Using an Existing Dataset**  
   - Since fetching new audio features is restricted, we **continue using our initial dataset**.
   - Ensures the **project remains functional and scalable** without relying on the Spotify API.

2. **Manual Dataset Updates**  
   - In the future, audio features can be **manually added** from available **open-source datasets**.

3. **Apply Transfer Learning**  
   - Use existing song embeddings (e.g., **Spotify Million Playlist Dataset**) to infer missing features.

---

## 🛠️ **How to Run Locally**
### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/lohithkumar12/spotify-song-recommendation.git
cd spotify-song-recommendation
```

### 2️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 3️⃣ **Run the Pipeline**
- **Train the Model**
```bash
python -c "from spotify_recommendation.pipeline.model_trainer_pipeline import ModelTrainerPipeline; ModelTrainerPipeline().initiate_model_training()"
```
- **Start the Web App**
```bash
streamlit run app.py
```

---

## ⚡ **MLOps & Continuous Model Improvement**
To **automate model training and deployment**, we have integrated **MLOps principles**:

### ✅ **1. Automatic Model Retraining & Deployment**
- **GitHub Actions** triggers **data updates & model retraining** every time there is a new commit.
- **Updated models** are logged in **DAGsHub MLflow**.
- **Hugging Face Spaces** automatically deploys the latest model.

### ✅ **2. Experiment Tracking with MLflow**
- All training runs are tracked using **DAGsHub MLflow**.
- We store **model metrics, parameters, and artifacts** for future comparison.

### ✅ **3. Dynamic Data Updates**
- Spotify API fetches new song metadata **(except audio features)**.
- The system updates the dataset dynamically.

---

## 📝 **Deployment Automation (GitHub Actions)**
A **CI/CD pipeline** is set up via **GitHub Actions (`main.yml`)**:

✔ **Fetches new data** from Spotify API (**if available**)  
✔ **Retrains the model** using the latest dataset  
✔ **Logs experiments in DAGsHub MLflow**  
✔ **Deploys the updated model to Hugging Face Spaces**  

---

## 📂 **Project Structure**
```
spotify-song-recommendation/
│── spotify_recommendation/
│   ├── pipeline/                  # Data ingestion, preprocessing, training
│   ├── components/                 # Model components
│   ├── config/                     # Configuration files
│   ├── utils/                       # Helper functions
│   ├── data/                        # Training datasets
│   ├── models/                      # Trained models
│   ├── mlruns/                      # MLflow experiment tracking
│── .github/workflows/deploy.yml     # CI/CD for auto deployment
│── requirements.txt                 # Required Python packages
│── app.py                           # Streamlit app
│── README.md                        # Project Documentation
```

---

## 🔗 **Links**
- **🔗 DAGsHub MLflow Tracking** → [DAGsHub MLflow](https://dagshub.com/vemuboddupalli/spotify-recommendation.mlflow)  
- **🚀 Hugging Face Deployment** → [Hugging Face Spaces](https://huggingface.co/spaces/lohithkumar01/spotify-song-recommendation)  
- **📂 GitHub Repository** → [GitHub](https://github.com/lohithkumar12/spotify-song-recommendation)  

---

## 🎤 **Final Summary**
- **✅ Successfully trained a song recommendation model.**
- **✅ Deployed on Hugging Face with CI/CD automation.**
- **✅ Integrated DAGsHub MLflow for tracking experiments.**
- **⚠️ Spotify API issue:** Unable to fetch **audio features** (403 Forbidden).  
- **📌 Workaround:** Using pre-existing datasets instead.

