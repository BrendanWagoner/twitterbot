import requests
import config
from refresh import Refresh

spotify_create_playlist_url = 'https://api.spotify.com/v1/users/brendan.bw/playlists'

bot_playlist_id = "2ziA524qfG5nYWaIY2NAn8"

reference_track = 'https://open.spotify.com/track/4BXczS9XwRb5ai7f9hYioQ'
authorize = f'https://accounts.spotify.com/authorize?client_id={config.s_client_id}&response_type=code&redirect_uri=https%3A%2F%2Fbrendanwagoner.github.io%2FFinal-Website-v1%2F&scope=playlist-read-private'


def create_spotify_playlist(name, public):
    respose = requests.post(
        spotify_create_playlist_url,
        headers={
            "Authorization": f"Bearer {call_refresh()}"
        },
        json={
            "name": name,
            "public": public
        }
    )
    json_resp = respose.json()

    return json_resp


def get_tracks(playlist_id):
    spotify_get_playlist_url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks?fields=items.track(name, external_urls)'
    response = requests.get(
        spotify_get_playlist_url,
        headers={"Authorization": f"Bearer {call_refresh()}"}
        )
    json_resp = response.json()
    tracks = json_resp['items']
    track = tracks[0]
    t = track['track']
    external_url = t['external_urls']
    url = external_url['spotify']

    return url


def call_refresh():
    refresh_caller = Refresh()

    return refresh_caller.refresh()
