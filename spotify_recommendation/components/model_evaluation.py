import os
import json
import joblib
import pandas as pd
from sklearn.metrics import silhouette_score, davies_bouldin_score
from spotify_recommendation.logging import logger
from spotify_recommendation.entity.config_entity import ModelEvaluationConfig

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def load_model_and_data(self):
        """Loads the trained K-Means model and clustered dataset."""
        model_path = os.path.join("artifacts/model_trainer/kmeans_model.pkl")
        data_path = os.path.join("artifacts/model_trainer/clustered_data.csv")

        if not os.path.exists(model_path) or not os.path.exists(data_path):
            raise FileNotFoundError(" Model or clustered data not found!")

        model = joblib.load(model_path)
        df = pd.read_csv(data_path)

        logger.info(f"Loaded trained model from {model_path}")
        logger.info(f"Loaded clustered dataset with {df.shape[0]} rows and {df.shape[1]} columns")

        return model, df

    def evaluate_clusters(self, model, df):
        """Computes Silhouette Score and Davies-Bouldin Index."""
        feature_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
        cluster_labels = df["Cluster_Label"]

        silhouette = silhouette_score(df[feature_cols], cluster_labels)
        davies_bouldin = davies_bouldin_score(df[feature_cols], cluster_labels)

        logger.info(f"Silhouette Score: {silhouette:.4f}")
        logger.info(f"Davies-Bouldin Score: {davies_bouldin:.4f}")

        return {"silhouette_score": silhouette, "davies_bouldin_score": davies_bouldin}

    def save_evaluation_report(self, metrics):
        """Saves evaluation metrics to a JSON file."""
        os.makedirs(self.config.root_dir, exist_ok=True)
        report_path = self.config.evaluation_report

        with open(report_path, "w") as f:
            json.dump(metrics, f, indent=4)

        logger.info(f"Model evaluation report saved at {report_path}")

    def run_evaluation(self):
        """Runs the full evaluation pipeline."""
        model, df = self.load_model_and_data()
        metrics = self.evaluate_clusters(model, df)
        self.save_evaluation_report(metrics)
