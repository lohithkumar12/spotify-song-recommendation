import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from spotify_recommendation.logging import logger
from spotify_recommendation.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def load_data(self):
        """Loads raw dataset"""
        if not os.path.exists(self.config.raw_data_path):
            raise FileNotFoundError(f"Dataset not found at {self.config.raw_data_path}")
        df = pd.read_csv(self.config.raw_data_path)
        logger.info(f"Loaded dataset with {df.shape[0]} rows and {df.shape[1]} columns")
        return df

    def drop_unnecessary_columns(self, df):
        """Remove unwanted columns"""
        drop_cols = ['Unnamed: 0', 'id', 'uri', 'track_number']
        df.drop(columns=[col for col in drop_cols if col in df.columns], inplace=True, errors='ignore')
        logger.info("Dropped unnecessary columns")
        return df

    def process_dates(self, df):
        """Convert release_date to release_year and compute song_age"""
        df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce")
        df["release_year"] = df["release_date"].dt.year
        df["song_age"] = pd.to_datetime("today").year - df["release_year"]
        df.drop(columns=["release_date"], inplace=True)
        logger.info("Processed release_date into release_year and song_age")
        return df

    def normalize_numeric_features(self, df):
        """Apply MinMax Scaling on numerical features"""
        numeric_features = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
        scaler = MinMaxScaler()
        df[numeric_features] = scaler.fit_transform(df[numeric_features])
        logger.info("Scaled numerical features")
        return df, scaler

    def encode_categorical_features(self, df):
        """Encode categorical features (song name and album)"""
        categorical_features = ['name', 'album']
        encoder = LabelEncoder()

        song_name_mapping = df[['name']].drop_duplicates().reset_index(drop=True)
        song_name_mapping['encoded_name'] = encoder.fit_transform(song_name_mapping['name'])

        df['name'] = encoder.transform(df['name'])
        df['album'] = encoder.fit_transform(df['album'])

        
        os.makedirs("data", exist_ok=True)
        mapping_path = "data/song_name_mapping.csv"
        song_name_mapping.to_csv(mapping_path, index=False)

        logger.info(f"Encoded categorical features and moved mapping to {mapping_path}")
        return df


    def remove_outliers(self, df):
        """Remove extreme outliers using IQR method"""
        numeric_features = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
        Q1 = df[numeric_features].quantile(0.25)
        Q3 = df[numeric_features].quantile(0.75)
        IQR = Q3 - Q1
        filter_outliers = ~((df[numeric_features] < (Q1 - 1.5 * IQR)) | (df[numeric_features] > (Q3 + 1.5 * IQR))).any(axis=1)
        df = df[filter_outliers]
        logger.info("Removed outliers using IQR method")
        return df
    
    def save_transformed_data(self, df):
        """Save cleaned and transformed dataset"""
        os.makedirs(self.config.root_dir, exist_ok=True)  # Ensure the directory exists
        cleaned_data_path = os.path.join(self.config.root_dir, "cleaned_rolling_stones_spotify.csv")
        df.to_csv(cleaned_data_path, index=False)
        logger.info(f"Transformed dataset saved to {cleaned_data_path}")
        return cleaned_data_path


   

    def transform_data(self):
        """Pipeline to run all transformation steps"""

        os.makedirs(self.config.root_dir, exist_ok=True)

        df = self.load_data()
        df = self.drop_unnecessary_columns(df)
        df = self.process_dates(df)
        df = self.remove_outliers(df)
        df, scaler = self.normalize_numeric_features(df)
        df = self.encode_categorical_features(df)

        return self.save_transformed_data(df)

