import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import os
from spotify_recommendation import logger

class SpotifyDataIngestion:
    def __init__(self, client_id, client_secret, output_file="artifacts/data/spotify_data.csv"):
        self.client_id = client_id
        self.client_secret = client_secret
        self.output_file = output_file
        self.sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=self.client_id, client_secret=self.client_secret))

    def fetch_tracks(self, playlist_id):
        """Fetches tracks from a Spotify playlist"""
        results = self.sp.playlist_tracks(playlist_id)
        track_data = []
        
        for item in results['items']:
            track = item['track']
            track_info = {
                "name": track["name"],
                "artist": track["artists"][0]["name"],
                "album": track["album"]["name"],
                "release_date": track["album"]["release_date"],
                "popularity": track["popularity"]
            }
            track_data.append(track_info)
        
        return track_data

    def save_data(self, playlist_id):
        """Saves fetched data to a CSV file"""
        track_data = self.fetch_tracks(playlist_id)
        df = pd.DataFrame(track_data)

        os.makedirs(os.path.dirname(self.output_file), exist_ok=True)
        df.to_csv(self.output_file, index=False)
        logger.info(f"✅ Data saved successfully: {self.output_file}")

        return self.output_file
