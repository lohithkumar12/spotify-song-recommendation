import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Set credentials
client_id = "f2e62d2b58e044bba3529a391565da78"
client_secret = "4125a139a17c465b93a166b13d9f4ad3"

# Authenticate
try:
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
    print("✅ Authentication Successful!")
    
    # Fetch playlist details
    playlist_id = "5fCbYbykLg85EVHHYrkgLw"
    playlist = sp.playlist_tracks(playlist_id)
    print(f"✅ Fetched {len(playlist['items'])} tracks successfully!")

except Exception as e:
    print(f"❌ Error: {e}")
