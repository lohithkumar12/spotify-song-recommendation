import os
import joblib
import pandas as pd
from spotify_recommendation.logging import logger
from spotify_recommendation.entity.config_entity import RecommendationConfig

class RecommendSongs:
    def __init__(self, config: RecommendationConfig):
        self.config = config
        self.model = self.load_model()
        self.df = self.load_clustered_data()

    def load_model(self):
        """Loads the trained K-Means model."""
        if not os.path.exists(self.config.model_path):
            raise FileNotFoundError(f"Model file not found at {self.config.model_path}")

        model = joblib.load(self.config.model_path)
        logger.info(f"Loaded trained model from {self.config.model_path}")
        return model

    def load_clustered_data(self):
        """Loads the clustered dataset."""
        if not os.path.exists(self.config.clustered_data_path):
            raise FileNotFoundError(f"Clustered data file not found at {self.config.clustered_data_path}")

        df = pd.read_csv(self.config.clustered_data_path)
        logger.info(f"Loaded clustered dataset with {df.shape[0]} rows and {df.shape[1]} columns")
        return df

    def get_recommendations(self, song_name, num_recommendations=5):
        """Returns similar songs based on the same cluster."""
        if song_name not in self.df['name'].values:
            raise ValueError(f"Song '{song_name}' not found in dataset!")

        # Identify the cluster for the selected song
        song_cluster = self.df[self.df['name'] == song_name]['Cluster_Label'].values[0]

        # Get songs from the same cluster
        recommendations = self.df[self.df['Cluster_Label'] == song_cluster].sample(n=num_recommendations, random_state=42)

        logger.info(f"Found {num_recommendations} similar songs for '{song_name}'")
        return recommendations[['name', 'album', 'Cluster_Label']]
