import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "spotify_recommendation"

list_of_files = [
    ".github/workflows/main.yml",
    f"data/cleaned_data.csv",
    f"data/song_name_mapping.csv",
    f"recommendation/{project_name}/__init__.py",
    f"recommendation/{project_name}/clustering.py",
    f"recommendation/{project_name}/recommend.py",
    f"ui/{project_name}/__init__.py",
    f"ui/{project_name}/app.py",
    f"ui/{project_name}/components.py",
    "logs/.gitkeep",
    "notebooks/eda.ipynb",
    "templates/table.html",
    "tests/test_recommendation.py",
    ".gitignore",
    "README.md",
    "requirements.txt",
    "setup.py",
    "push_data.py",
    "deploy/deploy.sh"
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
