import os
import joblib
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
from spotify_recommendation.logging import logger
from spotify_recommendation.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def load_data(self):
        """Loads transformed dataset for training."""
        if not os.path.exists(self.config.root_dir):
            os.makedirs(self.config.root_dir, exist_ok=True)

        data_path = os.path.join("artifacts/data_transformation/cleaned_rolling_stones_spotify.csv")
        if not os.path.exists(data_path):
            raise FileNotFoundError(f"Transformed dataset not found at {data_path}")

        df = pd.read_csv(data_path)
        logger.info(f"Loaded transformed dataset with {df.shape[0]} rows and {df.shape[1]} columns.")
        return df

    def train_kmeans(self, df):
        """Trains K-Means clustering model."""
        # Select numerical features only for clustering
        feature_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

        # Train K-Means model
        kmeans = KMeans(n_clusters=self.config.num_clusters, random_state=42)
        df["Cluster_Label"] = kmeans.fit_predict(df[feature_cols])

        # Save trained model
        joblib.dump(kmeans, self.config.model_path)
        logger.info(f" K-Means model trained and saved to {self.config.model_path}")

        return df

    def save_transformed_data(self, df):
        """Saves dataset with cluster labels."""
        output_path = os.path.join(self.config.root_dir, "clustered_data.csv")
        df.to_csv(output_path, index=False)
        logger.info(f"Clustered dataset saved at {output_path}")

    def train_model(self):
        """Executes the full training pipeline."""
        df = self.load_data()
        df = self.train_kmeans(df)
        self.save_transformed_data(df)
