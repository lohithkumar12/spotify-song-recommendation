import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "spotify_recommendation"

list_of_files = [
    ".github/workflows/main.yml",
    "config/config.yaml",
    "config/schema.yaml",
    "config/params.yaml",
    "final_model/model.pkl",
    "final_model/preprocessor.pkl",
    "data/cleaned_data.csv",
    "data/song_name_mapping.csv",
    f"{project_name}/__init__.py",
    f"{project_name}/cloud/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/config/configuration.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logging/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/data_ingestion_pipeline.py",
    f"{project_name}/pipeline/data_validation_pipeline.py",
    f"{project_name}/pipeline/data_transformation_pipeline.py",
    f"{project_name}/pipeline/model_trainer_pipeline.py",
    f"{project_name}/pipeline/model_evaluation_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/common.py",
    "logs/.gitkeep",
    "notebooks/1_data_ingestion.ipynb",
    "notebooks/2_data_validation.ipynb",
    "notebooks/3_data_transformation.ipynb",
    "notebooks/4_model_trainer.ipynb",
    "prediction_output/output.csv",
    "templates/table.html",
    "tests/test_recommendation.py",
    "valid_data/test.csv",
    ".gitignore",
    "README.md",
    "requirements.txt",
    "setup.py",
    "push_data.py",
    "app.py",
    "Dockerfile",
    "main.py",
    "deploy/deploy.sh",
    "setup.sh"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"📂 Creating directory: {filedir}")

    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, "w") as f:
            pass
        logging.info(f"📝 Creating empty file: {filepath}")
    else:
        logging.info(f"✅ {filename} already exists")
