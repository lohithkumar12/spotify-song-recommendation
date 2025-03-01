import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Set credentials
client_id = "client_id"
client_secret = "client_secret"

# Authenticate
try:
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
    # Fetch songs from the playlist
    playlist_tracks = sp.playlist_tracks("5fCbYbykLg85EVHHYrkgLw")

    # Extract song names
    song_list = [track["track"]["name"] + " - " + track["track"]["artists"][0]["name"] for track in playlist_tracks["items"]]

    # Print the fetched songs
    print("\nLatest Songs in Playlist:")
    for idx, song in enumerate(song_list, 1):
        print(f"{idx}. {song}")

except Exception as e:
    print(f"❌ Error: {e}")


