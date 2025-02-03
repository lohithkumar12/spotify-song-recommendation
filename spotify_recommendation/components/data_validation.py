import os
import pandas as pd
from spotify_recommendation.logging import logger
from spotify_recommendation.entity.config_entity import DataValidationConfig
from spotify_recommendation.utils.common import read_yaml

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
        self.schema = config.schema  # Load schema from DataValidationConfig

    def validate_columns(self, df):
        """Ensure dataset has expected columns based on schema.yaml."""
        expected_columns = set(self.schema.keys())
        actual_columns = set(df.columns)

        if expected_columns != actual_columns:
            missing_cols = expected_columns - actual_columns
            extra_cols = actual_columns - expected_columns
            raise ValueError(f" Column Mismatch!\nMissing: {missing_cols}\nExtra: {extra_cols}")

        logger.info("Column validation passed!")

    def validate_data(self):
        """Validates dataset structure."""
        if not os.path.exists(self.config.root_dir):
            os.makedirs(self.config.root_dir, exist_ok=True)

        df = pd.read_csv(self.config.dataset_path)

        # 🔹 Drop 'Unnamed: 0' if it exists
        if "Unnamed: 0" in df.columns:
            df.drop(columns=["Unnamed: 0"], inplace=True)
            logger.info("Dropped unnecessary column: 'Unnamed: 0'")

        self.validate_columns(df)

        # Write validation status
        with open(self.config.status_file, "w") as f:
            f.write("Validation Passed")

        logger.info(f"Data validation completed successfully! Status saved in {self.config.status_file}")
        return df  # Return validated data for further processing
