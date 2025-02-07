import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = "f2e62d2b58e044bba3529a391565da78"  # Replace with your actual Client ID
CLIENT_SECRET = "4125a139a17c465b93a166b13d9f4ad3"  # Replace with your actual Client Secret

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET))

results = sp.search(q="Imagine Dragons", type="track", limit=5)
for idx, track in enumerate(results['tracks']['items']):
    print(f"{idx+1}. {track['name']} - {track['artists'][0]['name']}")
