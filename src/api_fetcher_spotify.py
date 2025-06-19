import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

SPOTIFY_CLIENT_ID = "7b0d426cd17f4419b9756eb006c57adb"
SPOTIFY_CLIENT_SECRET = "c7b280adb5074bdba3745b97a7fd001b"

client_credentials_manager = SpotifyClientCredentials(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET
)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def fetch_artist_info_spotify(artist_name):
    result = sp.search(q=f'artist:{artist_name}', type='artist', limit=1)
    artists = result.get('artists', {}).get('items', [])

    if not artists:
        return None

    artist = artists[0]
    name = artist.get('name', 'Unknown Artist')
    images = artist.get('images', [])
    image_url = images[0]['url'] if images else None
    followers = artist.get('followers', {}).get('total', 0)
    genres = ", ".join(artist.get('genres', []))

    return {
        'name': name,
        'image_url': image_url,
        'followers': followers,
        'genres': genres
    }

