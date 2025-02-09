import os
import dagshub
import mlflow

# Set MLflow Tracking URI from environment
os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/vemuboddupalli/spotify-recommendation.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"] = "vemuboddupalli"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "78e1305697f7e893b4ecb7e5e8b2b276ef61c6e5"  # Fetch securely

dagshub.init(
    repo_owner="vemuboddupalli",
    repo_name="spotify-recommendation",
    mlflow=True
)

mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI"))
print(f"✅ MLflow tracking URI: {mlflow.get_tracking_uri()}")
