from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir: Path
    dataset_path: Path


@dataclass
class DataValidationConfig:
    root_dir: Path
    dataset_path: Path 
    status_file: Path
    schema: dict  # Stores expected schema from schema.yaml


@dataclass
class DataTransformationConfig:
    root_dir: Path
    transformed_data: Path
    raw_data_path: Path
    processed_data_dir: Path
    song_mapping_path: Path



@dataclass
class ModelTrainerConfig:
    root_dir: Path
    model_path: Path
    preprocessor_path: Path
    num_clusters: int
