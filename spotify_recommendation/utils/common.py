import os
import yaml
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError
from spotify_recommendation.logging import logger


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a YAML file and returns its contents as a ConfigBox object."""
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file {path_to_yaml} loaded successfully.")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f" YAML file {path_to_yaml} is empty.")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Creates directories if they do not exist."""
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """Saves data as a JSON file."""
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f" JSON file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Loads data from a JSON file."""
    with open(path, "r") as f:
        content = json.load(f)
    logger.info(f"JSON file loaded successfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """Saves data as a binary file using joblib."""
    joblib.dump(value=data, filename=path)
    logger.info(f" Binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """Loads a binary file using joblib."""
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data
