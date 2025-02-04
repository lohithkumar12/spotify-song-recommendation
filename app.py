import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from spotify_recommendation.pipeline.recommendation_pipeline import RecommendationPipeline
from spotify_recommendation.config.configuration import ConfigurationManager

# Load configuration and clustered data
config = ConfigurationManager().get_recommendation_config()
df = pd.read_csv(config.clustered_data_path)

# Ensure cluster labels exist
if 'Cluster_Label' not in df.columns:
    st.error("Cluster labels not found in dataset. Please ensure clustering is completed.")
    st.stop()

# Load song name mapping
mapping_file_path = "data/song_name_mapping.csv"  # Updated mapping path to follow project structure
try:
    name_mapping = pd.read_csv(mapping_file_path)
    name_mapping = name_mapping.drop_duplicates(subset=['encoded_name'])  # Remove duplicates
    name_mapping['encoded_name'] = name_mapping['encoded_name'].astype(str)
    name_mapping.rename(columns={'encoded_name': 'encoded_song_id', 'name': 'song_name'}, inplace=True)
    df['encoded_song_id'] = df['name'].astype(str)
    name_mapping['encoded_song_id'] = name_mapping['encoded_song_id'].astype(str)  # Ensure both are strings before merging
    df = df.merge(name_mapping, on='encoded_song_id', how="left")
    df.drop(columns=['encoded_song_id'], inplace=True, errors='ignore')
    if 'song_name' in df.columns:
        df['name'] = df['song_name']
        df.drop(columns=['song_name'], inplace=True, errors='ignore')
    else:
        st.error("Error: Song name column not found after merging. Check mapping file.")
        st.stop()
except FileNotFoundError:
    st.error("Song name mapping file not found. Please regenerate it.")
    st.stop()

# Verify 'name' column exists
if 'name' not in df.columns:
    st.error("Error: 'name' column missing from dataset after merging. Check data processing steps.")
    st.stop()

# Title
st.title("🎵 Spotify Song Recommendation App")
st.write("Select a song to get similar recommendations based on clustering.")

# Dropdown for song selection
selected_song = st.selectbox("Select a Song:", df['name'].dropna().unique())

# Recommendation function
def recommend_songs(song_name, num_recommendations=5):
    song_cluster = df[df['name'] == song_name]['Cluster_Label'].values[0]
    recommendations = df[df['Cluster_Label'] == song_cluster].sample(n=num_recommendations, random_state=42)
    return recommendations[['name', 'album', 'Cluster_Label']]

# Display recommendations
if st.button("Get Recommendations"):
    recommendations = recommend_songs(selected_song, num_recommendations=5)
    st.write("### Recommended Songs:")
    st.dataframe(recommendations)

# Visualization: Cluster distribution
st.write("## Cluster Distribution")
plt.figure(figsize=(8, 4))
sns.countplot(x=df['Cluster_Label'], palette='viridis')
plt.xlabel("Cluster")
plt.ylabel("Song Count")
st.pyplot(plt)

# Visualization: Top Albums
st.write("## Top Albums by Song Count")
top_albums = df['album'].value_counts().head(10)
plt.figure(figsize=(10, 5))
sns.barplot(x=top_albums.index, y=top_albums.values, palette='coolwarm')
plt.xticks(rotation=45)
plt.xlabel("Album")
plt.ylabel("Number of Songs")
st.pyplot(plt)
