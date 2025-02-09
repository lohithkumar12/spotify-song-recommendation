import os
import joblib
import pandas as pd
import mlflow
import mlflow.sklearn
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.model_selection import GridSearchCV
from spotify_recommendation.logging import logger
from spotify_recommendation.entity.config_entity import ModelTrainerConfig
import dagshub

# Initialize DAGsHub MLflow Tracking
dagshub.init(repo_owner='vemuboddupalli', repo_name='spotify-recommendation', mlflow=True)

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
        """Trains K-Means clustering model with GridSearchCV for hyperparameter tuning."""
        feature_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
        X = df[feature_cols]

        # Define parameter grid for K-Means tuning
        param_grid = {
            'n_clusters': [3, 4, 5, 6, 7],  
            'init': ['k-means++', 'random']
        }

        # Corrected silhouette scorer function for GridSearchCV
        silhouette_scorer = lambda estimator, X: silhouette_score(X, estimator.fit_predict(X))

        # Use GridSearchCV to find the best cluster number
        grid_search = GridSearchCV(KMeans(random_state=42), param_grid, cv=3, scoring=silhouette_scorer)
        grid_search.fit(X)

        best_kmeans = grid_search.best_estimator_

        # Apply best model
        df["Cluster_Label"] = best_kmeans.fit_predict(X)

        return df, best_kmeans, grid_search

    def save_transformed_data(self, df):
        """Saves dataset with cluster labels."""
        output_path = os.path.join(self.config.root_dir, "clustered_data.csv")
        df.to_csv(output_path, index=False)
        logger.info(f"Clustered dataset saved at {output_path}")

    def plot_clusters(self, df):
        """Generates and logs K-Means cluster visualization."""
        plt.figure(figsize=(8, 6))
        sns.scatterplot(
            x=df["energy"], y=df["valence"], hue=df["Cluster_Label"],
            palette="viridis", alpha=0.7
        )
        plt.title("K-Means Clustering of Songs (Energy vs Valence)")
        plot_path = os.path.join(self.config.root_dir, "cluster_plot.png")
        plt.savefig(plot_path)
        plt.close()
        return plot_path

    def train_model(self):
        """Executes the full training pipeline with MLflow logging."""

        mlflow.set_experiment("Spotify Song Clustering")

        with mlflow.start_run():
            df = self.load_data()
            df, best_kmeans, grid_search = self.train_kmeans(df)  # Training and adding cluster labels
            self.save_transformed_data(df)

            # Compute metrics
            silhouette = silhouette_score(df.select_dtypes(include=['float64', 'int64']), df["Cluster_Label"])

            # Log dataset size
            mlflow.log_param("num_rows", df.shape[0])
            mlflow.log_param("num_columns", df.shape[1])

            # Log best hyperparameters
            mlflow.log_param("best_n_clusters", grid_search.best_params_['n_clusters'])
            mlflow.log_param("best_init", grid_search.best_params_['init'])
            mlflow.log_metric("silhouette_score", silhouette)

            # Log model to MLflow
            mlflow.sklearn.log_model(best_kmeans, "kmeans_model")

            # Save trained model locally
            joblib.dump(best_kmeans, self.config.model_path)

            # Log dataset sample (10 records)
            sample_data_path = os.path.join(self.config.root_dir, "sample_clustered_data.csv")
            df.sample(10).to_csv(sample_data_path, index=False)
            mlflow.log_artifact(sample_data_path, artifact_path="data_samples")
            logger.info("Logged dataset sample to MLflow.")

            # Log Cluster Visualization
            plot_path = self.plot_clusters(df)
            mlflow.log_artifact(plot_path, artifact_path="plots")
            logger.info("Cluster plot logged to MLflow.")

            logger.info("Model training completed with MLflow tracking.")
