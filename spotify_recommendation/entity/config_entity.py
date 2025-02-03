from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir: Path
    dataset_path: Path


@dataclass
class DataValidationConfig:
    root_dir: Path
    status_file: Path

@dataclass
class DataTransformationConfig:
    root_dir: Path
    transformed_data: Path

@dataclass
class ModelTrainerConfig:
    root_dir: Path
    model_path: Path
    preprocessor_path: Path
    num_clusters: int
